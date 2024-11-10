from typing import Dict, List, Any
from barfi.st_flow.schema import load_schema_name
from barfi.utils.migration import (
    migrate_connections_to_ui,
    migrate_nodes_to_ui,
)


def prepare_editor_schema(
    load_schema: str, base_blocks_data: List[Dict[str, Any]]
) -> Dict[str, List]:
    if load_schema:
        editor_schema = load_schema_name(load_schema)
        editor_schema["connections"] = migrate_connections_to_ui(
            editor_schema["nodes"], editor_schema["connections"]
        )
        editor_schema["nodes"] = migrate_nodes_to_ui(
            editor_schema["nodes"], base_blocks_data
        )
    else:
        editor_schema = {"nodes": [], "connections": []}

    return editor_schema
