# SPDX-License-Identifier: Apache-2.0
# Standard
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from importlib import resources
from typing import Iterable, Optional
import math
import os.path

# Third Party
from datasets import Dataset, concatenate_datasets
from openai import OpenAI
import yaml

# First Party
from instructlab.sdg.utils import pandas

# Local
from . import filterblock, importblock, llmblock, utilblocks
from .block import Block
from .logger_config import setup_logger

logger = setup_logger(__name__)


# This is part of the public API.
class EmptyDatasetError(Exception):
    pass


# This is part of the public API.
@dataclass
class PipelineContext:  # pylint: disable=too-many-instance-attributes
    """
    A PipelineContext holds the common attributes needed between blocks in a
    pipeline

    client: The OpenAI client handle.
    model_id: The ID of the teacher model to be used for client calls.
    model_family: The family identifier for the model being updated.
    num_instructions_to_generate: The total number of instructions the user
        wants to generate during this run.
    batch_size: The size of the dataset batches for parallel generation. Set to
        0 to disable batching.
    batch_num_workers: The number of worker threads/processes to maintain in the
        central executor pool.
    dataset_num_procs: The number of processes to use when performing parallel
       map operations on individual datasets.
    """

    # The default batch size of 8 has been determined as a good default for
    # standard instructlab workloads when running with vllm batching.
    DEFAULT_BATCH_SIZE = 8

    # The default number of processes to use when performing parallel operations
    # on individual datasets
    DEFAULT_DATASET_NUM_PROCS = 8

    client: OpenAI
    model_family: str
    model_id: str
    num_instructions_to_generate: int
    dataset_num_procs: Optional[int] = DEFAULT_DATASET_NUM_PROCS
    batch_size: int = DEFAULT_BATCH_SIZE
    batch_num_workers: Optional[int] = None

    @property
    def batching_enabled(self) -> bool:
        """Batching is enabled IFF the batch size is specified and the number of
        workers is not set explicitly to 1
        """
        return self.batch_size > 0 and self.batch_num_workers != 1


# This is part of the public API.
class PipelineBlockError(Exception):
    """A PipelineBlockError occurs when a block generates an exception during
    generation. It contains information about which block failed and why.
    """

    def __init__(
        self,
        exception: Exception,
        *,
        block: Optional[Block] = None,
        block_name: Optional[str] = None,
        block_type: Optional[str] = None,
    ):
        self.exception = exception
        self.block = block
        self.block_name = block_name or (block.block_name if block else None)
        self.block_type = block_type or (block.__class__.__name__ if block else None)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.block_type}/{self.block_name}): {self.exception_message}"

    @property
    def exception_message(self) -> str:
        return str(self.exception)


# This is part of the public API.
class Pipeline:
    def __init__(
        self,
        ctx: PipelineContext,
        config_path: str,
        chained_blocks: list[dict],
    ) -> None:
        """
        Initialize the Pipeline class with a configuration dictionary.
        config_dict: the run config py or yaml loaded into a dictionary
        """
        # ctx is a PipelineContext object that supplies context configuration to every block
        self.ctx = ctx
        # config_path is the path of the pipeline config file used to create this pipeline
        self.config_path = config_path
        # pipeline config is the run configuration that consists of the pipeline steps
        self.chained_blocks = chained_blocks

    @classmethod
    def from_file(cls, ctx, pipeline_yaml):
        if not os.path.isabs(pipeline_yaml):
            pipeline_yaml = os.path.join(resources.files(__package__), pipeline_yaml)
        return cls(ctx, pipeline_yaml, _parse_pipeline_config_file(pipeline_yaml))

    def generate(self, dataset) -> Dataset:
        """
        Generate the dataset by running the pipeline steps.
        dataset: the input dataset
        """
        # If not batching, simply delegate to _generate_single
        if not self.ctx.batching_enabled:
            logger.info("Running pipeline single-threaded")
            return self._generate_single(dataset)

        # Otherwise, split the dataset into batches and run each batch as a
        # future in the thread pool
        logger.info(
            "Running pipeline with multi-threaded batching. Using %s workers for batches of size %s",
            self.ctx.batch_num_workers,
            self.ctx.batch_size,
        )
        input_splits = self._split_dataset(dataset)
        with ThreadPoolExecutor(max_workers=self.ctx.batch_num_workers) as executor:
            futures = [
                executor.submit(self._generate_single, input_split)
                for input_split in input_splits
            ]

            # Collect the results of each batch as they finish. This needs to
            # wait for them all, so the order of waiting doesn't matter
            output_splits = [future.result() for future in futures]

        return concatenate_datasets(output_splits)

    ## Implementation Details ##

    def _generate_single(self, dataset) -> Dataset:
        """Generate a single dataset by running the pipeline steps."""
        for block_prop in self.chained_blocks:
            # Initialize arguments for error handling to None
            block, block_name, block_type = None, None, None
            try:
                # Parse and instantiate the block
                block_name = block_prop["name"]
                block_type = _lookup_block_type(block_prop["type"])
                block_config = block_prop["config"]
                drop_columns = block_prop.get("drop_columns", [])
                drop_duplicates_cols = block_prop.get("drop_duplicates", False)
                block = block_type(self.ctx, self, block_name, **block_config)
                logger.info("Running block: %s", block_name)
                logger.info(dataset)

                # Execute the block and wrap errors with the block name/type
                dataset = block.generate(dataset)
            except Exception as err:
                raise PipelineBlockError(
                    exception=err,
                    block=block,
                    block_name=block_name,
                    block_type=block_type,
                ) from err

            # If at any point we end up with an empty data set, the pipeline has failed
            if len(dataset) == 0:
                return dataset

            drop_columns_in_ds = [e for e in drop_columns if e in dataset.column_names]
            if drop_columns:
                dataset = dataset.remove_columns(drop_columns_in_ds)

            if drop_duplicates_cols:
                dataset = self._drop_duplicates(dataset, cols=drop_duplicates_cols)

        return dataset

    def _drop_duplicates(self, dataset, cols):
        """
        Drop duplicates from the dataset based on the columns provided.
        """
        df = dataset.to_pandas()
        df = df.drop_duplicates(subset=cols)
        ds = pandas.dataset_from_pandas_dataframe(df)

        return ds

    def _split_dataset(self, dataset: Dataset) -> list[Dataset]:
        """Split the dataset into smaller batches."""
        assert (
            self.ctx.batch_size is not None
        ), "Programming Error: Should not call _split_dataset if batching disabled"
        total_size = len(dataset)
        num_batches = math.ceil(total_size / self.ctx.batch_size)
        batches = [
            dataset.select(self._get_batch_indices(i, total_size))
            for i in range(num_batches)
        ]
        return batches

    def _get_batch_indices(self, batch_index: int, total_size: int) -> Iterable[int]:
        assert (
            self.ctx.batch_size is not None
        ), "Programming Error: Should not call _get_batch_indices if batching disabled"
        return range(
            # Start index offset by the batch size
            batch_index * self.ctx.batch_size,
            # End index is the next batch offset or the end of the dataset
            min((batch_index + 1) * self.ctx.batch_size, total_size),
        )


_block_types = {
    "CombineColumnsBlock": utilblocks.CombineColumnsBlock,
    "ConditionalLLMBlock": llmblock.ConditionalLLMBlock,
    "DuplicateColumnsBlock": utilblocks.DuplicateColumnsBlock,
    "FilterByValueBlock": filterblock.FilterByValueBlock,
    "FlattenColumnsBlock": utilblocks.FlattenColumnsBlock,
    "ImportBlock": importblock.ImportBlock,
    "LLMBlock": llmblock.LLMBlock,
    "RenameColumnsBlock": utilblocks.RenameColumnsBlock,
    "SamplePopulatorBlock": utilblocks.SamplePopulatorBlock,
    "SelectorBlock": utilblocks.SelectorBlock,
    "SetToMajorityValueBlock": utilblocks.SetToMajorityValueBlock,
}


def _lookup_block_type(block_type):
    if not block_type in _block_types:
        raise PipelineConfigParserError(f"Unknown block type {block_type}")
    return _block_types[block_type]


_PIPELINE_CONFIG_PARSER_MAJOR = 1
_PIPELINE_CONFIG_PARSER_MINOR = 0


# This is part of the public API.
class PipelineConfigParserError(Exception):
    """An exception raised while parsing a pipline config file."""


def _parse_pipeline_config_file(pipeline_yaml):
    with open(pipeline_yaml, "r", encoding="utf-8") as pipeline_file:
        content = yaml.safe_load(pipeline_file)

    version = content["version"]
    major, minor = map(int, version.split("."))

    if major > _PIPELINE_CONFIG_PARSER_MAJOR:
        raise PipelineConfigParserError(
            "The pipeline config file format is from a future major version."
        )
    if major <= _PIPELINE_CONFIG_PARSER_MAJOR and minor > _PIPELINE_CONFIG_PARSER_MINOR:
        logger.warning(
            "The pipeline config file may have new features that will be ignored."
        )

    if not "blocks" in content:
        raise PipelineConfigParserError(
            "The pipeline config file contains no 'blocks' section"
        )

    return content["blocks"]


# This is part of the public API.
SIMPLE_PIPELINES_PACKAGE = "instructlab.sdg.pipelines.simple"
FULL_PIPELINES_PACKAGE = "instructlab.sdg.pipelines.full"
EVAL_PIPELINES_PKG = "instructlab.sdg.pipelines.eval"
