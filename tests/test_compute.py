import pytest
import json
from barfi.st_flow.block import Block
from .assets.blocks import base_blocks
from barfi.st_flow.schema.manage import SchemaManager
from barfi.st_flow.compute.base import ComputeEngine
from barfi.st_flow.flow.types import build_flow_schema_from_dict


@pytest.fixture
def compute_engine():
    return ComputeEngine(base_blocks)


@pytest.fixture
def load_schema():
    schema_manager = SchemaManager(filepath="./tests/assets/")
    return schema_manager.load_schema("math-muldiv")
    # return schema_manager.load_schema("options-all")


@pytest.fixture
def editor_schema():
    with open("tests/assets/schema_wall.json", "r") as f:
        load_schema = json.load(f)
    return build_flow_schema_from_dict(load_schema().get("editor_schema"))


def test_make_map_node_block(compute_engine, load_schema):
    _map = compute_engine._make_map_node_block(load_schema)

    # Assert that _map is a dictionary
    assert isinstance(_map, dict)

    # Assert that all values in _map are Block instances
    for block in _map.values():
        assert isinstance(block, Block)

    # Assert that each key in _map corresponds to a node ID from the schema
    schema_node_ids = {node.id for node in load_schema.nodes}
    assert set(_map.keys()) == schema_node_ids

    # Assert that each block in _map has the correct type matching its schema node
    for node in load_schema.nodes:
        if node.id in _map:
            assert _map[node.id]._type == node.type


def test_make_execution_graph(compute_engine, load_schema):
    _graph, _root_nodes = compute_engine._make_execution_graph(load_schema)
    assert isinstance(_graph, dict)
    assert all(isinstance(node_id, str) for node_id in _graph.keys())
    assert all(isinstance(children, list) for children in _graph.values())

    # Assert that the root nodes are correctly identified
    # Check that root nodes have no incoming connections
    for node_id in _root_nodes:
        assert not any(node_id in children for children in _graph.values())


def test_execute(compute_engine, load_schema):
    compute_engine.execute(load_schema)

    _map_node_block = load_schema.block_map

    # Assert that we get a dictionary of Block instances
    assert isinstance(_map_node_block, dict)
    assert all(isinstance(block, Block) for block in _map_node_block.values())

    # Verify that all nodes from schema are present in the result
    assert set(_map_node_block.keys()) == {node.id for node in load_schema.nodes}

    # Verify that the computation results are correct
    # For each node in the schema, check that:
    # 1. Its interfaces match the schema
    # 2. The computed values are correct based on the math operations
    for node in load_schema.nodes:
        block = _map_node_block[node.id]

        # Check that all input interfaces exist and have values
        for interface in node.inputs:
            assert block.get_interface(interface.name) is not None
            assert interface.value == block.get_interface(interface.name)

        # Check that all output interfaces exist and have values
        for interface in node.outputs:
            assert block.get_interface(interface.name) is not None
            assert interface.value == block.get_interface(interface.name)

    # Verify that the connections are correctly set
    for connection in load_schema.connections:
        assert _map_node_block[connection.outputNode].get_interface(
            connection.outputNodeInterface
        ) == _map_node_block[connection.inputNode].get_interface(
            connection.inputNodeInterface
        )
