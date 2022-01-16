import sys
sys.path.append('../')
import streamlit as st
from st_barfi import Block, st_barfi

feed = Block(name='Feed')
feed.add_output()

splitter = Block(name='Splitter')
splitter.add_input()
splitter.add_output()
splitter.add_output()

mixer = Block(name='Mixer')
mixer.add_input()
mixer.add_input()
mixer.add_output()

result = Block(name='Result')
result.add_input()

blocks = [feed, result, mixer, splitter]

editor_preset = {'nodes': [{'type': 'Feed', 'id': 'node_16421654445600', 'name': 'Feed', 'options': [], 'state': {}, 'interfaces': [['Output 1', {'id': 'ni_16421654445601', 'value': None}]], 'position': {'x': 53.10270771798835, 'y': 103.53598351788409}, 'width': 200, 'twoColumn': False, 'customClasses': ''}, {'type': 'Feed', 'id': 'node_16421655709876', 'name': 'Feed', 'options': [], 'state': {}, 'interfaces': [['Output 1', {'id': 'ni_16421655709877', 'value': None}]], 'position': {'x': -110.96319142010879, 'y': 354.1711813273622}, 'width': 200, 'twoColumn': False, 'customClasses': ''}, {'type': 'Splitter', 'id': 'node_16421655753058', 'name': 'Splitter', 'options': [], 'state': {}, 'interfaces': [['Input 1', {'id': 'ni_16421655753069', 'value': None}], ['Output 1', {'id': 'ni_164216557530610', 'value': None}], ['Output 2', {'id': 'ni_164216557530611', 'value': None}]], 'position': {'x': 160.08999419005372, 'y': 242.060177855096}, 'width': 200, 'twoColumn': False, 'customClasses': ''}, {'type': 'Mixer', 'id': 'node_164216557860312', 'name': 'Mixer',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          'options': [], 'state': {}, 'interfaces': [['Input 1', {'id': 'ni_164216557860313', 'value': None}], ['Input 2', {'id': 'ni_164216557860314', 'value': None}], ['Output 1', {'id': 'ni_164216557860315', 'value': None}]], 'position': {'x': 428.30492654775384, 'y': 112.91965486805523}, 'width': 200, 'twoColumn': False, 'customClasses': ''}, {'type': 'Result', 'id': 'node_164216558728816', 'name': 'Result', 'options': [], 'state': {}, 'interfaces': [['Input 1', {'id': 'ni_164216558728817', 'value': None}]], 'position': {'x': 426.88579992152256, 'y': 335.7225351863563}, 'width': 200, 'twoColumn': False, 'customClasses': ''}], 'connections': [{'id': '164216559410520', 'from': 'ni_16421654445601', 'to': 'ni_164216557860313'}, {'id': '164216559592723', 'from': 'ni_164216557530610', 'to': 'ni_164216557860314'}, {'id': '164216559830026', 'from': 'ni_164216557530611', 'to': 'ni_164216558728817'}, {'id': '164216560187829', 'from': 'ni_16421655709877', 'to': 'ni_16421655753069'}], 'panning': {'x': 163.41400013998373, 'y': 110.67177791961308}, 'scaling': 0.7761150375278565}

[editor_state, active_blocks, active_connections] = st_barfi(
    blocks, load_data=editor_preset)

st.write("Active blocks")
st.write(active_blocks)
st.write("Active connections")
st.write(active_connections)
st.markdown(editor_state)
