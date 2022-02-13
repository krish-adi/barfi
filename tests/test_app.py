import sys
sys.path.append('../')
from test_blocks import feed, result, mixer, splitter
import streamlit as st
from barfi import compute_engine, st_barfi, ComputeEngine
from matplotlib import pyplot as plt
import networkx as nx
import copy

blocks = [feed, result, mixer, splitter]
ce = ComputeEngine(blocks=blocks)

editor_preset = {'nodes': [{'type': 'Feed', 'id': 'node_16421654445600', 'name': 'Feed-1', 'options': [], 'state': {}, 'interfaces': [['Output 1', {'id': 'ni_16421654445601', 'value': None}]], 'position': {'x': 53.10270771798835, 'y': 103.53598351788409}, 'width': 200, 'twoColumn': False, 'customClasses': ''}, {'type': 'Feed', 'id': 'node_16421655709876', 'name': 'Feed-2', 'options': [], 'state': {}, 'interfaces': [['Output 1', {'id': 'ni_16421655709877', 'value': None}]], 'position': {'x': -110.96319142010879, 'y': 354.1711813273622}, 'width': 200, 'twoColumn': False, 'customClasses': ''}, {'type': 'Splitter', 'id': 'node_16421655753058', 'name': 'Splitter-1', 'options': [], 'state': {}, 'interfaces': [['Input 1', {'id': 'ni_16421655753069', 'value': None}], ['Output 1', {'id': 'ni_164216557530610', 'value': None}], ['Output 2', {'id': 'ni_164216557530611', 'value': None}]], 'position': {'x': 160.08999419005372, 'y': 242.060177855096}, 'width': 200, 'twoColumn': False, 'customClasses': ''}, {'type': 'Mixer', 'id': 'node_164216557860312', 'name': 'Mixer-1',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                'options': [], 'state': {}, 'interfaces': [['Input 1', {'id': 'ni_164216557860313', 'value': None}], ['Input 2', {'id': 'ni_164216557860314', 'value': None}], ['Output 1', {'id': 'ni_164216557860315', 'value': None}]], 'position': {'x': 428.30492654775384, 'y': 112.91965486805523}, 'width': 200, 'twoColumn': False, 'customClasses': ''}, {'type': 'Result', 'id': 'node_164216558728816', 'name': 'Result-1', 'options': [], 'state': {}, 'interfaces': [['Input 1', {'id': 'ni_164216558728817', 'value': None}]], 'position': {'x': 426.88579992152256, 'y': 335.7225351863563}, 'width': 200, 'twoColumn': False, 'customClasses': ''}], 'connections': [{'id': '164216559410520', 'from': 'ni_16421654445601', 'to': 'ni_164216557860313'}, {'id': '164216559592723', 'from': 'ni_164216557530610', 'to': 'ni_164216557860314'}, {'id': '164216559830026', 'from': 'ni_164216557530611', 'to': 'ni_164216558728817'}, {'id': '164216560187829', 'from': 'ni_16421655709877', 'to': 'ni_16421655753069'}], 'panning': {'x': 163.41400013998373, 'y': 110.67177791961308}, 'scaling': 0.7761150375278565}

result = st_barfi(base_blocks=blocks, compute_engine=ce, load_data=editor_preset, load_schema='schema-4')
st.write(result)

# st.write('### DAG Graph of the computational block-link')
# fig, ax = plt.subplots(figsize=(12, 6))
# nx.draw(self._graph, with_labels=True, node_color='lightblue',
#         node_size=500, labels=self._map_block_id_name)
# st.pyplot(fig)

# st.write(_compu_order)

# st.write(self._active_blocks)
# st.write(self._map_block_id_name)
# st.write(self._map_interface_id_block_id)
# st.write(self._map_interface_id_name)
# st.write(self._map_link_interface_id_from_to)
# st.write(self._map_link_interface_id_to_from)
