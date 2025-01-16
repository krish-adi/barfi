import pytest
import json
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
    return schema_manager.load_schema("async-math")


@pytest.fixture
def editor_schema():
    with open("tests/assets/schema_wall_async.json", "r") as f:
        load_schema = json.load(f)
    return build_flow_schema_from_dict(load_schema.get("editor_schema"))


@pytest.mark.asyncio
async def test_async_execution(compute_engine, editor_schema):
    # Execute the async flow
    await compute_engine.async_execute(editor_schema)

    _map_node_block = editor_schema._block_map

    # Verify blocks were created and executed
    assert len(_map_node_block) == 6


def test_sync_execution(compute_engine, editor_schema):
    # Execute the async flow
    compute_engine.execute(editor_schema)

    _map_node_block = editor_schema._block_map

    # Verify blocks were created and executed
    assert len(_map_node_block) == 6
