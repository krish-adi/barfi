import networkx as nx
import copy
from .block_builder import Block
from typing import List, Dict


class ComputeEngine(object):
    def __init__(self, blocks: List[Block] = [], **kwargs) -> None:
        # Initialise the Compute Enginge
        # The primitive block types that are tied to this compute engine
        self._blocks = blocks

        # The state of the editor that is stored as JSON/Dict that represents
        # the active blocks and links on the editor
        self._editor_state = {}

        # Active blocks extracted from the editor_state.
        self._active_blocks = {}

        # Mapping all the active blocks and connections to their id and names
        self._map_block_id_name = {}
        self._map_interface_id_block_id = {}
        self._map_interface_id_name = {}
        self._map_link_interface_id_from_to = {}
        self._map_link_interface_id_to_from = {}

        # Create a directed-acyclic-graph of the blocks and links
        # The computational graph
        self._graph = nx.DiGraph()

        # Result from the execution for the compute engine
        self._result = {}

    def add_editor_state(self, editor_state):
        self._editor_state = editor_state

    def get_result(self) -> Dict:
        # return self._active_blocks
        return self._result

    def _map_block_link(self):
        if bool(self._editor_state):

            for _block in self._editor_state['nodes']:

                # Create a child block object for the active the block and associate with its id
                _parent_block = next(
                    _b for _b in self._blocks if _b._type == _block['type'])
                # Create an independent deep copy of the parent block type
                _child_block = copy.deepcopy(_parent_block)
                _child_block._name = _block['name']

                # Map the active block id to its name
                self._map_block_id_name[_block['id']] = _block['name']

                # Map the active interfaces/Links to the active block
                _block_interfaces = {}
                for _interface in _block['interfaces']:
                    self._map_interface_id_block_id[_interface[1]
                                                    ['id']] = _block['id']
                    self._map_interface_id_name[_interface[1]
                                                ['id']] = _interface[0]
                    _child_block.set_interface(
                        name=_interface[0], id=_interface[1]['id'])
                    _block_interfaces[_interface[0]] = _interface[1]

                # _block_interfaces = {'Input 1': {'id': 'asdas', 'value': None}}

                # Active blocks build from the base-blocks and editor-state
                self._active_blocks[_block['id']] = {
                    'block': _child_block, 'interfaces': _block_interfaces, 'type': _block['type'], 'name': _block['name']}

                # Add block to the DAG as a node
                self._graph.add_node(_block['id'], name=_block['name'])

            for _connection in self._editor_state['connections']:
                from_node = self._map_interface_id_block_id[_connection['from']]
                to_node = self._map_interface_id_block_id[_connection['to']]
                if _connection['from'] not in self._map_link_interface_id_from_to:
                    self._map_link_interface_id_from_to[_connection['from']] = [
                    ]
                self._map_link_interface_id_from_to[_connection['from']].append(
                    _connection['to'])
                self._map_link_interface_id_to_from[_connection['to']
                                                    ] = _connection['from']

                # Add the _connection to the DAG as an edge
                self._graph.add_edge(from_node, to_node,
                                     edge_id=_connection['id'])

            if not nx.is_directed_acyclic_graph(self._graph):
                raise('Cycle(s) detected. Not supported by `barfi` at the moment.')
            else:
                _compu_order = [self._map_block_id_name[node]
                                for node in nx.topological_sort(self._graph)]

            # TODO morph _result to _active_blocks and have only one of them.
            # TODO add the interface info to the block
            for block_id, block in self._active_blocks.items():
                self._result[block['name']] = {'block': block['block'],
                                               'type': block['type'],
                                               'interfaces': {}}
                for link_id, link in block['interfaces'].items():
                    self._result[block['name']]['interfaces'][link_id] = {}
                    _interface_id = link['id']

                    if _interface_id in self._map_link_interface_id_from_to:
                        self._result[block['name']
                                     ]['interfaces'][link_id]['type'] = 'output'
                        self._result[block['name']
                                     ]['interfaces'][link_id]['to'] = {}
                        for to_id in self._map_link_interface_id_from_to[_interface_id]:
                            to_name = self._map_interface_id_name[to_id]
                            to_block_id = self._map_interface_id_block_id[to_id]
                            to_block_name = self._map_block_id_name[to_block_id]
                            self._result[block['name']
                                         ]['interfaces'][link_id]['to'][to_block_name] = to_name

                    if _interface_id in self._map_link_interface_id_to_from:
                        self._result[block['name']
                                     ]['interfaces'][link_id]['type'] = 'intput'
                        self._result[block['name']
                                     ]['interfaces'][link_id]['from'] = {}
                        from_id = self._map_link_interface_id_to_from[_interface_id]
                        from_name = self._map_interface_id_name[from_id]
                        from_block_id = self._map_interface_id_block_id[from_id]
                        from_block_name = self._map_block_id_name[from_block_id]
                        self._result[block['name']
                                     ]['interfaces'][link_id]['from'][from_block_name] = from_name

    def _execute_compute(self):
        if bool(self._editor_state):

            for node in nx.topological_sort(self._graph):
                self._active_blocks[node]['block']._on_compute()
                for key, value in self._active_blocks[node]['block']._outputs.items():
                    try:
                        for find_to in self._map_link_interface_id_from_to[value['id']]:
                            find_to_block = self._map_interface_id_block_id[find_to]
                            self._active_blocks[find_to_block]['block'].set_interface(
                                name=self._map_interface_id_name[find_to], value=value['value'])
                    except:
                        pass
