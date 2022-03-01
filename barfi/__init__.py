import streamlit.components.v1 as components
from typing import List, Dict

# import barfi components
from .block_builder import Block
from .compute_engine import ComputeEngine
from .manage_schema import load_schema_name, load_schemas, save_schema
from .manage_schema import editor_preset

import os

_RELEASE = True

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
    build_dir = os.path.join(parent_dir, "client")
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


def st_barfi(base_blocks: List[Block], load_schema: str = None, compute_engine: bool = True, key=None):
    if load_schema:
        editor_schema = load_schema_name(load_schema)
    else:
        editor_schema = None

    schemas_in_db = load_schemas()
    schema_names_in_db = schemas_in_db['schema_names']

    editor_setting = {'compute_engine': compute_engine} 

    base_blocks_data = [block._export() for block in base_blocks]
    _from_client = _component_func(base_blocks=base_blocks_data, load_editor_schema=editor_schema, 
                load_schema_names=schema_names_in_db, load_schema_name=load_schema, editor_setting = editor_setting,
                key=key, default={'command': 'skip', 'editor_state': {}})

    if _from_client['command'] == 'execute':
        if compute_engine:
            _ce = ComputeEngine(blocks=base_blocks)
            _ce.add_editor_state(_from_client['editor_state'])
            _ce._map_block_link()
            _ce._execute_compute()
            return _ce.get_result()
        else:
            _ce = ComputeEngine(blocks=base_blocks)
            _ce.add_editor_state(_from_client['editor_state'])
            _ce._map_block_link()                      
            return _ce.get_result()
    if _from_client['command'] == 'save':
        save_schema(
            schema_name=_from_client['schema_name'], schema_data=_from_client['editor_state'])
    if _from_client['command'] == 'load':
        load_schema = _from_client['schema_name']
        editor_schema = load_schema_name(load_schema)
    else:
        pass

    return {}

def barfi_schemas():
    schemas_in_db = load_schemas()   
    schema_names_in_db = schemas_in_db['schema_names'] 
    
    return schema_names_in_db
