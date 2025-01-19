import time
import pytest
import json
import asyncio
from .assets.blocks import base_blocks
from barfi.flow.schema.manage import SchemaManager
from barfi.flow.compute.base import ComputeEngine
from barfi.flow.schema.types import build_flow_schema_from_dict


@pytest.fixture
def compute_engine() -> ComputeEngine:
    return ComputeEngine(base_blocks)


@pytest.fixture
def load_schema():
    schema_manager = SchemaManager(filepath="./tests/assets/")
    return schema_manager.load_schema("async-math-deep")


@pytest.fixture
def editor_schema():
    with open("tests/assets/schema_wall_parallel_deep.json", "r") as f:
        load_schema = json.load(f)
    return build_flow_schema_from_dict(load_schema.get("editor_schema"))


def test_make_parallel_execution_graph(compute_engine, editor_schema):
    graph, levels = compute_engine._make_parallel_execution_graph(editor_schema)
    # pprint(graph)
    # pprint(levels)


@pytest.mark.asyncio
async def test_async_parallel_execution(compute_engine, editor_schema):
    # Time the execution
    start_time = asyncio.get_event_loop().time()

    await compute_engine.async_execute(editor_schema)

    end_time = asyncio.get_event_loop().time()
    execution_time = end_time - start_time

    # Since we have 7 blocks with 0.1s sleep each, 4, 2, 1 in parallel,
    # the total time should be close to 0.3s rather than 0.7s
    assert execution_time < 0.33  # Adding some buffer for execution overhead


def test_sync_parallel_execution(compute_engine, editor_schema):
    # Time the execution
    start_time = time.time()

    # Run the sync execution in an async context
    compute_engine.execute(editor_schema)

    end_time = time.time()
    execution_time = end_time - start_time

    # Since we have 7 blocks with 0.1s sleep each, 4, 2, 1 in parallel,
    # the total time should be close to 0.3s rather than 0.7s
    assert execution_time < 0.33  # Adding some buffer for execution overhead
