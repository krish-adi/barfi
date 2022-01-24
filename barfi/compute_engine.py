import networkx as nx
import copy

def compute_engine(blocks, editor_state):

    active_blocks = {}
    # change all these variable names to _map block to label, block to id, and blah blah,
    # and put all maps as a single map object dict
    block_label = {}
    interface_block_id = {}
    active_connections = []
    _map_interface_id_to_name = {}

    G = nx.DiGraph()

    if bool(editor_state):
        for block in editor_state['nodes']:
            interfaces = {}
            for interface in block['interfaces']:
                interface_block_id[interface[1]['id']] = block['id']
                interfaces[interface[0]] = interface[1]
                _map_interface_id_to_name[interface[1]['id']] = interface[0]
            parent_block = next(
                _b for _b in blocks if _b._type == block['type'])
            child_block = copy.deepcopy(parent_block)
            child_block._name = block['name']
            child_block._interface_value = interfaces
            active_blocks[block['id']] = {
                'block': child_block, 'interfaces': interfaces, 'type': block['type'], 'name': block['name']}
            block_label[block['id']] = block['name']
            # active_blocks[block['id']] = {'name': block['type'], 'id': block['id'], 'title': block['name'], 'interfaces': interfaces , 'interfaces_data': block['interfaces']}
        active_connections = editor_state['connections']

        for block_id, block_value in active_blocks.items():
            G.add_node(block_id, name=block_value['name'])

    ni_from_to = {}
    for connection in active_connections:
        from_node = interface_block_id[connection['from']]
        to_node = interface_block_id[connection['to']]
        ni_from_to[connection['from']] = connection['to']
        G.add_edge(from_node, to_node, edge_id=connection['id'])

    if not nx.is_directed_acyclic_graph(G):
        print('Cycle(s) detected. Not supported by `barfi` at the moment.')
    else:
        _compu_order = [node for node in nx.topological_sort(G)]
