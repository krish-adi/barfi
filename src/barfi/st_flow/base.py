import os
import streamlit.components.v1 as components
from typing import List, Dict, Union

# import st_flow components
from barfi.config import RELEASE
from barfi.st_flow.block import Block
from barfi.st_flow.block.prepare import prepare_blocks_export
from barfi.st_flow.flow.types import build_streamlit_flow_response

_RELEASE = RELEASE

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
        "st_flow",
        url="http://localhost:3001",
    )
else:
    st_barfi_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(st_barfi_dir, "static")
    _component_func = components.declare_component("st_flow", path=build_dir)

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


def st_flow(
    base_blocks: Union[List[Block], Dict[str, List[Block]]],
    editor_schema: str = None,
    commands: List[str] = ["execute", "save"],
    key=None,
):
    base_blocks_data, _ = prepare_blocks_export(base_blocks)

    # TODO: Add custom commands, to make it customize to act upon a command bar of tools
    # and commmands and how to render them on the ui
    _from_client = _component_func(
        base_blocks=base_blocks_data,
        editor_schema=editor_schema,
        commands=commands,
        key=key,
        default={"command": "default", "editor_state": {}},
    )

    return build_streamlit_flow_response(_from_client)
