import streamlit as st
import streamlit.components.v1 as components

from block_builder import Block

import os

_RELEASE = False

# Declare a Streamlit component. `declare_component` returns a function
# that is used to create instances of the component. We're naming this
# function "_component_func", with an underscore prefix, because we don't want
# to expose it directly to users. Instead, we will create a custom wrapper
# function, below, that will serve as our component's public API.

# It's worth noting that this call to `declare_component` is the
# *only thing* you need to do to create the binding between Streamlit and
# your component frontend. Everything else we do in this file is simply a
# best practice.

if not _RELEASE:
    _component_func = components.declare_component(
        "st_barfi",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/dist")
    _component_func = components.declare_component(
        "st_barfi", path=build_dir)

# Create a wrapper function for the component. This is an optional
# best practice - we could simply expose the component function returned by
# `declare_component` and call it done. The wrapper allows us to customize
# our component's API: we can pre-process its input args, post-process its
# output value, and add a docstring for users.


def st_barfi(blocks, load_data=None, key=None):
    blocks_data = []
    for block in blocks:
        blocks_data.append(block._export())
    editor_state = _component_func(
        blocks=blocks_data, load_data=load_data, key=key, default={})
    active_blocks = []
    active_connections = []

    print(editor_state)

    if bool(editor_state):
        for block in editor_state['nodes']:
            active_blocks.append({'name': block['type'], 'id': block['id'],
                                  'title': block['name'], 'interfaces': block['interfaces']})
        active_connections = editor_state['connections']

    return [editor_state, active_blocks, active_connections]

# We use the special "key" argument to assign a fixed identity to this
# component instance. By default, when a component's arguments change,
# it is considered a new instance and will be re-mounted on the frontend
# and lose its current state. In this case, we want to vary the component's
# "name" argument without having it get recreated.


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
