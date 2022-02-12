import networkx as nx
import copy
from .block_builder import Block
from typing import List


class ComputeEngine(object):
    def __init__(self, blocks: List[Block] = [], **kwargs) -> None:
        # Initialise the Compute Enginge

        self._blocks = blocks

    def compute_engine(blocks, editor_state):
        active_blocks = {}
        # Mapping from to for block id and interface id
        _map_block_id_name = {}
        _map_interface_id_block_id = {}
        _map_interface_id_name = {}
        _map_link_interface_id_from_to = {}

        # Create a directed-acyclic-graph of the blocks and links
        G = nx.DiGraph()

        for _block in editor_state['nodes']:

            # Map the active block id to its name
            _map_block_id_name[_block['id']] = _block['name']

            # Map the active interfaces/Links to the active block
            _block_interfaces = {}
            for _interface in _block['interfaces']:
                _map_interface_id_block_id[_interface[1]['id']] = _block['id']
                _map_interface_id_name[_interface[1]['id']] = _interface[0]
                _block_interfaces[_interface[0]] = _interface[1]

            # Create a child block object for the active the block and associate with its id
            _parent_block = next(
                _b for _b in blocks if _b._type == _block['type'])
            # Create an independent deep copy of the parent block type
            _child_block = copy.deepcopy(_parent_block)
            _child_block._name = _block['name']
            _child_block._interface_value = _block_interfaces

            # Change name TODO
            active_blocks[_block['id']] = {
                'block': _child_block, 'interfaces': _block_interfaces, 'type': _block['type'], 'name': _block['name']}

            # Add block to the DAG as a node
            G.add_node(_block['id'], name=_block['name'])

        for _connection in editor_state['connections']:
            from_node = _map_interface_id_block_id[_connection['from']]
            to_node = _map_interface_id_block_id[_connection['to']]
            _map_link_interface_id_from_to[_connection['from']
                                           ] = _connection['to']

            # Add the _connection to the DAG as an edge
            G.add_edge(from_node, to_node, edge_id=_connection['id'])

        if not nx.is_directed_acyclic_graph(G):
            raise('Cycle(s) detected. Not supported by `barfi` at the moment.')
        else:
            _compu_order = [node for node in nx.topological_sort(G)]

        for node in nx.topological_sort(G):
            active_blocks[node]['block']._on_calculate()
            for key, value in active_blocks[node]['block']._interface_value.items():
                try:
                    find_to = _map_link_interface_id_from_to[value['id']]
                    find_to_block = _map_interface_id_block_id[find_to]
                    active_blocks[find_to_block]['block'].set_interface(
                        name=_map_interface_id_name[find_to], value=value['value'])
                except:
                    pass
