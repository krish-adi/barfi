"""
This module contains functions for migrating data from old versions of Barfi to new versions.
"""

from typing import List, Dict, Any
from copy import deepcopy


def migrate_connections_to_ui(nodes: List[Dict], connections: List[Dict]):
    map_node_interfaces = {}
    for node in nodes:
        for interface in node["interfaces"]:
            map_node_interfaces[interface[1]["id"]] = {
                "node_id": node["id"],
                "node_name": node["name"],
                "node_handle": interface[0],
            }
    for cnn in connections:
        cnn["source"] = map_node_interfaces[cnn["from"]]["node_id"]
        cnn["sourceHandle"] = map_node_interfaces[cnn["from"]]["node_handle"]
        cnn["target"] = map_node_interfaces[cnn["to"]]["node_id"]
        cnn["targetHandle"] = map_node_interfaces[cnn["to"]]["node_handle"]
        cnn["animated"] = True

    return connections


def migrate_nodes_to_ui(nodes: List[Dict], base_blocks: List[Dict]):
    _return_nodes = []
    _base_block_map = {base_block["name"]: base_block for base_block in base_blocks}

    for node in nodes:
        _node_base_block = deepcopy(_base_block_map[node["type"]])
        _node_options_value_map = {_opt[0]: _opt[1] for _opt in node["options"]}
        _node_options = _node_base_block["options"]
        _node_options_tuple = []
        for _noption in _node_options:
            _noption["value"] = _node_options_value_map[_noption["name"]]
            _node_options_tuple.append((_noption["name"], _noption["value"]))

        _node_interfaces_map = {_intf[0]: _intf[1] for _intf in node["interfaces"]}
        _node_inputs = _node_base_block["inputs"]
        _node_inputs_tuple = []
        for _ninput in _node_inputs:
            _ninput["id"] = _node_interfaces_map[_ninput["name"]]["id"]
            _ninput["value"] = _node_interfaces_map[_ninput["name"]]["value"]
            _node_inputs_tuple.append((_ninput["name"], _ninput["value"]))
        _node_outputs = _node_base_block["outputs"]
        _node_outputs_tuple = []
        for _noutput in _node_outputs:
            _noutput["id"] = _node_interfaces_map[_noutput["name"]]["id"]
            _noutput["value"] = _node_interfaces_map[_noutput["name"]]["value"]
            _node_outputs_tuple.append((_noutput["name"], _noutput["value"]))

        _return_nodes.append(
            {
                "id": node["id"],
                "type": "baseBlock",
                "data": {
                    "blockData": {
                        # TODO: resolve name type label conflict
                        "name": node["type"],
                        "label": node["name"],
                        "options": _node_options,
                        "inputs": _node_inputs,
                        "outputs": _node_outputs,
                        # "options": _node_options_tuple,
                        # "inputs": _node_inputs_tuple,
                        # "outputs": _node_outputs_tuple,
                    },
                },
                "position": {
                    "x": node["position"]["x"],
                    "y": node["position"]["y"],
                },
            }
        )

    return _return_nodes


def migrate_state_from_ui(
    base_blocks: List[Dict],
    nodes: List[Dict[str, Any]],
    connections: List[Dict[str, Any]],
) -> Dict[str, Any]:
    block_data_map = {base_block["name"]: base_block for base_block in base_blocks}

    flow_state_nodes = []
    for node in nodes:
        block_data = block_data_map[node["type"]]
        _node_inputs_map = {_input[0]: _input[1] for _input in node["inputs"]}
        _node_outputs_map = {_output[0]: _output[1] for _output in node["outputs"]}
        input_interfaces = [
            (
                item["name"],
                {
                    "id": f'{node["id"]}__{item["name"]}',
                    "value": _node_inputs_map[item["name"]],
                },
            )
            for item in block_data["inputs"]
        ]
        output_interfaces = [
            (
                item["name"],
                {
                    "id": f'{node["id"]}__{item["name"]}',
                    "value": _node_outputs_map[item["name"]],
                },
            )
            for item in block_data["outputs"]
        ]

        flow_state_nodes.append(
            {
                "id": node["id"],
                "type": node["type"],
                "name": node["name"],
                "options": node["options"],
                "interfaces": input_interfaces + output_interfaces,
                "position": node["position"],
                "measured": node["measured"],
            }
        )

    flow_state_connections = [
        {
            "id": conn["id"],
            "from": f'{conn["source"]}__{conn["sourceHandle"]}',
            "to": f'{conn["target"]}__{conn["targetHandle"]}',
            "source": conn["source"],
            "target": conn["target"],
            "sourceHandle": conn["sourceHandle"],
            "targetHandle": conn["targetHandle"],
        }
        for conn in connections
    ]

    return {"nodes": flow_state_nodes, "connections": flow_state_connections}
