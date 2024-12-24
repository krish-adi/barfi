import pytest
import json
from dataclasses import asdict
from barfi.flow.flow.types import build_flow_schema_from_dict


def load_schema():
    with open("tests/assets/schema_wall.json", "r") as f:
        return json.load(f)


@pytest.fixture
def editor_schema():
    return build_flow_schema_from_dict(load_schema().get("editor_schema"))


def test_flow_schema_export(editor_schema):
    _schema_lhs = asdict(editor_schema)
    _schema_lhs.pop("_block_map", None)
    _schema_rhs = editor_schema.export()

    assert _schema_lhs.keys() == _schema_rhs.keys()
    assert _schema_lhs == _schema_rhs
