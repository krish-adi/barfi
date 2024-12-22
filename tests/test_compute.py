from pprint import pprint
import pytest
from barfi.st_flow.block import Block
from .assets.blocks import base_blocks
from barfi.st_flow.schema.manage import SchemaManager
from barfi.st_flow.compute.base import ComputeEngine


@pytest.fixture
def compute_engine():
    return ComputeEngine(base_blocks)


@pytest.fixture
def load_schema():
    schema_manager = SchemaManager(filepath="./tests/assets/")
    return schema_manager.load_schema("math-muldiv")
    # return schema_manager.load_schema("options-all")


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
    _map_node_block = compute_engine.execute(load_schema)
    for node in load_schema.nodes:
        print(node, _map_node_block[node.id])
        print("\n\n")
