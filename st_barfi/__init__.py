# import streamlit as st
import streamlit.components.v1 as components

from block import Block

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
    component_value = _component_func(
        blocks=blocks_data, load_data=load_data, key=key, default={})
    return component_value

# We use the special "key" argument to assign a fixed identity to this
# component instance. By default, when a component's arguments change,
# it is considered a new instance and will be re-mounted on the frontend
# and lose its current state. In this case, we want to vary the component's
# "name" argument without having it get recreated.


feed = Block(name='Feed')
feed.add_output()
feed.add_output()
feed.add_option(name='a-check-box-option', type='checkbox', value=True)
feed.add_option(name='a-text-input-option',
               type='input', value="enter text here")
feed.add_option(name='an-integer-intput-option',
               type='integer', value=5, min=1, max=10)
feed.add_option(name='a-number-intput-option',
               type='number', value=2.5, min=0, max=5)
feed.add_option(name='a-select-item-option', type='select',
               value='item 1', items=['item 1', 'item 2', 'item 3'])
feed.add_option(name='a-slider-option', type='slider', value=5, min = 0, max=10)
feed.add_option(name='a-display-option', type='display',
               value='some text to be displayed here.')


result = Block(name='Result')
result.add_input()

blocks = [feed, result]

output_dict = st_barfi(blocks)
# st.markdown(output_dict)
