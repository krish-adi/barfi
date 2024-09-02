"""
This module contains functions for migrating data from old versions of Barfi to new versions.
"""

from typing import List, Dict
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
        for _noption in _node_options:
            _noption["value"] = _node_options_value_map[_noption["name"]]

        _node_interfaces_map = {_intf[0]: _intf[1] for _intf in node["interfaces"]}

        _node_inputs = _node_base_block["inputs"]
        for _ninput in _node_inputs:
            _ninput["id"] = _node_interfaces_map[_ninput["name"]]["id"]
            _ninput["value"] = _node_interfaces_map[_ninput["name"]]["value"]
        _node_outputs = _node_base_block["outputs"]
        for _noutput in _node_outputs:
            _noutput["id"] = _node_interfaces_map[_noutput["name"]]["id"]
            _noutput["value"] = _node_interfaces_map[_noutput["name"]]["value"]

        _return_nodes.append(
            {
                "id": node["id"],
                "type": "custom",
                "data": {
                    "blockData": {
                        # TODO: resolve name type label conflict
                        "name": node["type"],
                        "label": node["name"],
                        "options": _node_options,
                        "inputs": _node_inputs,
                        "outputs": _node_outputs,
                    },
                },
                "position": {
                    "x": node["position"]["x"],
                    "y": node["position"]["y"],
                },
            }
        )

    return _return_nodes
