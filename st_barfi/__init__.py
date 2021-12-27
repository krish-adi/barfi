# import streamlit as st
import streamlit.components.v1 as components

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
    component_value = _component_func(blocks=blocks, load_data=load_data, key=key, default={})
    return component_value

# We use the special "key" argument to assign a fixed identity to this
# component instance. By default, when a component's arguments change,
# it is considered a new instance and will be re-mounted on the frontend
# and lose its current state. In this case, we want to vary the component's
# "name" argument without having it get recreated.

feed = {'Name': 'Feed',
        'InputsInfo': [],
        'OutputsInfo': [{'name': 'Output'}]}
splitter = {'Name': 'Splitter',
            'InputsInfo': [{'name': 'Input'}],
            'OutputsInfo': [{'name': 'Output 1'}, {'name': 'Output 2'}]}
mixer = {'Name': 'Mixer',
         'InputsInfo': [{'name': 'Input 1'}, {'name': 'Input 2'}],
         'OutputsInfo': [{'name': 'Output'}]}
result = {'Name': 'Result',
          'InputsInfo': [{'name': 'Input'}],
          'OutputsInfo': []}

blocks = [feed, splitter, mixer, result]

loads = {'nodes': [{'type': 'Feed', 'id': 'node_16391710737910', 'name': 'Feed', 'options': [], 'state': {}, 'interfaces': [['Output', {'id': 'ni_16391710737911', 'value': None}]], 'position': {'x': 73, 'y': 177}, 'width': 200, 'twoColumn': False, 'customClasses': ''}, {'type': 'Result', 'id': 'node_16391710817562', 'name': 'Result', 'options': [], 'state': {}, 'interfaces': [['Input', {'id': 'ni_16391710817563', 'value': None}]], 'position': {'x': 443, 'y': 274}, 'width': 200, 'twoColumn': False, 'customClasses': ''}], 'connections': [{'id': '16391710884286', 'from': 'ni_16391710737911', 'to': 'ni_16391710817563'}], 'panning': {'x': 0, 'y': 0}, 'scaling': 1}

output_dict = st_barfi(blocks, load_data=loads)
# st.markdown(output_dict)

# Import 
# from .block_builder import BlockBuilder