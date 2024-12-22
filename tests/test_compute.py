from pprint import pprint
import pytest
from dataclasses import asdict
from barfi.st_flow.schema.manage import SchemaManager
from barfi.st_flow.flow.types import FlowSchema, FlowViewport
from .assets.blocks import base_blocks


@pytest.fixture
def editor_schema():
    schema_manager = SchemaManager(filepath="./tests/assets/")
    return schema_manager.load_schema("math-muldiv")


def test_compute(editor_schema):
    schema_obj = asdict(editor_schema)
    pprint(schema_obj)
