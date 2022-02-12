import sys
sys.path.append('../')
from test_blocks import feed, result, mixer, splitter
import streamlit as st
from barfi import st_barfi
from matplotlib import pyplot as plt
import networkx as nx
import copy

blocks = [feed, result, mixer, splitter]

editor_preset = {'nodes': [{'type': 'Feed', 'id': 'node_16421654445600', 'name': 'Feed-1', 'options': [], 'state': {}, 'interfaces': [['Output 1', {'id': 'ni_16421654445601', 'value': None}]], 'position': {'x': 53.10270771798835, 'y': 103.53598351788409}, 'width': 200, 'twoColumn': False, 'customClasses': ''}, {'type': 'Feed', 'id': 'node_16421655709876', 'name': 'Feed-2', 'options': [], 'state': {}, 'interfaces': [['Output 1', {'id': 'ni_16421655709877', 'value': None}]], 'position': {'x': -110.96319142010879, 'y': 354.1711813273622}, 'width': 200, 'twoColumn': False, 'customClasses': ''}, {'type': 'Splitter', 'id': 'node_16421655753058', 'name': 'Splitter-1', 'options': [], 'state': {}, 'interfaces': [['Input 1', {'id': 'ni_16421655753069', 'value': None}], ['Output 1', {'id': 'ni_164216557530610', 'value': None}], ['Output 2', {'id': 'ni_164216557530611', 'value': None}]], 'position': {'x': 160.08999419005372, 'y': 242.060177855096}, 'width': 200, 'twoColumn': False, 'customClasses': ''}, {'type': 'Mixer', 'id': 'node_164216557860312', 'name': 'Mixer-1',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                'options': [], 'state': {}, 'interfaces': [['Input 1', {'id': 'ni_164216557860313', 'value': None}], ['Input 2', {'id': 'ni_164216557860314', 'value': None}], ['Output 1', {'id': 'ni_164216557860315', 'value': None}]], 'position': {'x': 428.30492654775384, 'y': 112.91965486805523}, 'width': 200, 'twoColumn': False, 'customClasses': ''}, {'type': 'Result', 'id': 'node_164216558728816', 'name': 'Result-1', 'options': [], 'state': {}, 'interfaces': [['Input 1', {'id': 'ni_164216558728817', 'value': None}]], 'position': {'x': 426.88579992152256, 'y': 335.7225351863563}, 'width': 200, 'twoColumn': False, 'customClasses': ''}], 'connections': [{'id': '164216559410520', 'from': 'ni_16421654445601', 'to': 'ni_164216557860313'}, {'id': '164216559592723', 'from': 'ni_164216557530610', 'to': 'ni_164216557860314'}, {'id': '164216559830026', 'from': 'ni_164216557530611', 'to': 'ni_164216558728817'}, {'id': '164216560187829', 'from': 'ni_16421655709877', 'to': 'ni_16421655753069'}], 'panning': {'x': 163.41400013998373, 'y': 110.67177791961308}, 'scaling': 0.7761150375278565}

# # With loops
# editor_preset = {'nodes': [{'type': 'Feed', 'id': 'node_16421654445600', 'name': 'Feed', 'options': [], 'state': {}, 'interfaces': [['Output 1', {'id': 'ni_16421654445601', 'value': None}]], 'position': {'x': 53.10270771798835, 'y': 103.53598351788409}, 'width': 200, 'twoColumn': False, 'customClasses': ''}, {'type': 'Feed', 'id': 'node_16421655709876', 'name': 'Feed', 'options': [], 'state': {}, 'interfaces': [['Output 1', {'id': 'ni_16421655709877', 'value': None}]], 'position': {'x': -395.9608670807274, 'y': 296.0466553702624}, 'width': 200, 'twoColumn': False, 'customClasses': ''}, {'type': 'Splitter', 'id': 'node_16421655753058', 'name': 'Splitter', 'options': [], 'state': {}, 'interfaces': [['Input 1', {'id': 'ni_16421655753069', 'value': None}], ['Output 1', {'id': 'ni_164216557530610', 'value': None}], ['Output 2', {'id': 'ni_164216557530611', 'value': None}]], 'position': {'x': 160.08999419005372, 'y': 242.060177855096}, 'width': 200, 'twoColumn': False, 'customClasses': ''}, {'type': 'Mixer', 'id': 'node_164216557860312', 'name': 'Mixer', 'options': [], 'state': {}, 'interfaces': [['Input 1', {'id': 'ni_164216557860313', 'value': None}], ['Input 2', {'id': 'ni_164216557860314', 'value': None}], ['Output 1', {'id': 'ni_164216557860315', 'value': None}]], 'position': {'x': 428.30492654775384, 'y': 112.91965486805523}, 'width': 200, 'twoColumn': False, 'customClasses': ''}, {'type': 'Result', 'id': 'node_164216558728816', 'name': 'Result', 'options': [], 'state': {}, 'interfaces': [['Input 1', {'id': 'ni_164216558728817', 'value': None}]], 'position': {'x': 698.7229579146288,
#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   'y': 245.71451925962754}, 'width': 200, 'twoColumn': False, 'customClasses': ''}, {'type': 'Mixer', 'id': 'node_164233731511530', 'name': 'Mixer', 'options': [], 'state': {}, 'interfaces': [['Input 1', {'id': 'ni_164233731511631', 'value': None}], ['Input 2', {'id': 'ni_164233731511632', 'value': None}], ['Output 1', {'id': 'ni_164233731511633', 'value': None}]], 'position': {'x': -112.723576361132, 'y': 375.92941903750454}, 'width': 200, 'twoColumn': False, 'customClasses': ''}, {'type': 'Splitter', 'id': 'node_164233736008643', 'name': 'Splitter', 'options': [], 'state': {}, 'interfaces': [['Input 1', {'id': 'ni_164233736008644', 'value': None}], ['Output 1', {'id': 'ni_164233736008645', 'value': None}], ['Output 2', {'id': 'ni_164233736008646', 'value': None}]], 'position': {'x': 421.64706550252777, 'y': 310.3049542472305}, 'width': 200, 'twoColumn': False, 'customClasses': ''}], 'connections': [{'id': '164216559410520', 'from': 'ni_16421654445601', 'to': 'ni_164216557860313'}, {'id': '164216559592723', 'from': 'ni_164216557530610', 'to': 'ni_164216557860314'}, {'id': '164233732351836', 'from': 'ni_164233731511633', 'to': 'ni_16421655753069'}, {'id': '164233734787542', 'from': 'ni_16421655709877', 'to': 'ni_164233731511631'}, {'id': '164233736975950', 'from': 'ni_164216557530611', 'to': 'ni_164233736008644'}, {'id': '164233738304254', 'from': 'ni_164233736008645', 'to': 'ni_164216558728817'}, {'id': '164233739219957', 'from': 'ni_164233736008646', 'to': 'ni_164233731511632'}], 'panning': {'x': 462.8955070935626, 'y': 373.0757152670363}, 'scaling': 0.4821928840637319}

[editor_state, active_blocks, active_connections] = st_barfi(
    blocks, load_data=editor_preset)

# st.write("Active blocks")
# st.write(active_blocks)
# st.write("Active connections")
# st.write(active_connections)
# st.markdown(editor_state)

if bool(editor_state):
    active_blocks = {}
    # change all these variable names to _map block to label, block to id, and blah blah,
    # and put all maps as a single map object dict
    _map_block_id_name = {}
    _map_interface_id_block_id = {}
    _map_interface_id_name = {}
    _map_link_interface_id_from_to = {}
    _map_link_interface_id_to_from = {}

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
        _map_link_interface_id_from_to[_connection['from']] = _connection['to']
        _map_link_interface_id_to_from[_connection['to']] = _connection['from']

        # Add the _connection to the DAG as an edge
        G.add_edge(from_node, to_node, edge_id=_connection['id'])

    if not nx.is_directed_acyclic_graph(G):
        raise('Cycle(s) detected. Not supported by `barfi` at the moment.')
    else:
        _compu_order = [_map_block_id_name[node] for node in nx.topological_sort(G)]
        
    st.write('### DAG Graph of the computational block-link')
    fig, ax = plt.subplots(figsize=(12, 6))
    nx.draw(G, with_labels=True, node_color='lightblue',
            node_size=500, labels=_map_block_id_name)
    st.pyplot(fig)

    st.write('### Computational order')
    st.write(_compu_order)

    st.write('### Performing the computation')
    # st.write(active_blocks[_compu_order[0]]['block']._interface_value)
    # active_blocks[_compu_order[0]]['block']._on_calculate()
    # st.write(active_blocks[_compu_order[0]]['block']._interface_value)

    # for key, value in active_blocks[_compu_order[0]]['block']._interface_value.items():
    #     find_to = _map_link_interface_id_from_to[value['id']]
    #     find_to_block = _map_interface_id_block_id[find_to]
    #     st.write(active_blocks[find_to_block])
    #     active_blocks[find_to_block]['block'].set_interface(name=_map_interface_id_name[find_to], value=value['value'])
    #     st.write(active_blocks[find_to_block])

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

    # st.write(active_blocks)
    # st.write(_map_block_id_name)
    # st.write(_map_interface_id_block_id)
    # st.write(_map_interface_id_name)
    # st.write(_map_link_interface_id_from_to)
    # st.write(_map_link_interface_id_to_from)

    result = {}
    for block_id, block in active_blocks.items():
        result[block['name']] = {'block': block['block'],
                                 'type': block['type'],
                                 'interfaces': {}}
        for link_id, link in block['interfaces'].items():
            result[block['name']]['interfaces'][link_id] = {'value': link['value']}
            _interface_id = link['id']

            if _interface_id in _map_link_interface_id_from_to:
                result[block['name']]['interfaces'][link_id]['type'] = 'output'
                result[block['name']]['interfaces'][link_id]['to'] = {}
                to_id = _map_link_interface_id_from_to[_interface_id]
                to_name = _map_interface_id_name[to_id]
                to_block_id = _map_interface_id_block_id[to_id]
                to_block_name = _map_block_id_name[to_block_id]
                result[block['name']]['interfaces'][link_id]['to'][to_block_name] = to_name

            if _interface_id in _map_link_interface_id_to_from:
                result[block['name']]['interfaces'][link_id]['type'] = 'intput'
                result[block['name']]['interfaces'][link_id]['from'] = {}
                from_id = _map_link_interface_id_to_from[_interface_id]
                from_name = _map_interface_id_name[from_id]
                from_block_id = _map_interface_id_block_id[from_id]
                from_block_name = _map_block_id_name[from_block_id]
                result[block['name']]['interfaces'][link_id]['from'][from_block_name] = from_name
    
    st.write(result)