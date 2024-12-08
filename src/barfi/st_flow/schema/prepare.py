from dataclasses import asdict
from typing import Dict, List, Any
from barfi.st_flow.flow.types import FlowSchema, FlowConnection


def _factory_connection_export(connection: FlowConnection):
    return {
        "id": connection.id,
        "source": connection.outputNode,
        "sourceHandler": connection.outputNodeInterface,
        "target": connection.inputNode,
        "targetHandler": connection.inputNodeInterface,
    }


def export_schema_to_ui(
    flow_schema: FlowSchema, base_blocks_data: List[Dict[str, Any]]
) -> Dict[str, List]:
    editor_schema = {
        "nodes": [asdict(node) for node in flow_schema.nodes],
        "connections": [
            _factory_connection_export(connection)
            for connection in flow_schema.connections
        ],
        "viewport": asdict(flow_schema.viewport),
    }

    return editor_schema
