import streamlit as st
import streamlit.components.v1 as components
import networkx as nx

# import barfi components
from .block_builder import Block
from .compute_engine import ComputeEngine

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

# We use the special "key" argument to assign a fixed identity to this
# component instance. By default, when a component's arguments change,
# it is considered a new instance and will be re-mounted on the frontend
# and lose its current state. In this case, we want to vary the component's
# "name" argument without having it get recreated.


def st_barfi(blocks, load_data=None, key=None):
    blocks_data = [block._export() for block in blocks]
    editor_state = _component_func(
        blocks=blocks_data, load_data=load_data, key=key, default={})

    active_blocks = []
    active_connections = []

    if bool(editor_state):
        for block in editor_state['nodes']:
            active_blocks.append({'name': block['type'], 'id': block['id'],
                                  'title': block['name'], 'interfaces': block['interfaces']})
        active_connections = editor_state['connections']

    active_blocks = {}
    block_label = {}  # Only for testing
    interface_block_id = {}
    active_connections = []

    if bool(editor_state):
        for block in editor_state['nodes']:
            interfaces = {}
            for interface in block['interfaces']:
                interface_block_id[interface[1]['id']] = block['id']
                interfaces[interface[1]['id']] = interface[1]['value']
            active_blocks[block['id']] = {
                'type': block['type'], 'name': block['name'], 'interfaces': interfaces}
            block_label[block['id']] = block['name']
            # active_blocks[block['id']] = {'name': block['type'], 'id': block['id'], 'title': block['name'], 'interfaces': interfaces , 'interfaces_data': block['interfaces']}
        active_connections = editor_state['connections']

    return [editor_state, active_blocks, active_connections]



    