import os
from typing import List, Dict, Union

from barfi.config import RELEASE
from barfi.v0.block_builder import Block
from barfi.v0.compute_engine import ComputeEngine
from barfi.v0.manage_schema import load_schema_name, load_schemas, save_schema

try:
    import streamlit.components.v1 as components
except ImportError:
    raise ImportError(
        "Please install required dependencies using: pip install barfi[v0]"
    )


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
        "st_barfi",
        url="http://localhost:3001",
    )
else:
    st_barfi_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(st_barfi_dir, "static")
    _component_func = components.declare_component("st_barfi", path=build_dir)

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


def st_barfi(
    base_blocks: Union[List[Block], Dict],
    load_schema: str = None,
    compute_engine: bool = True,
    key=None,
):
    if load_schema:
        editor_schema = load_schema_name(load_schema)
    else:
        editor_schema = None

    schemas_in_db = load_schemas()
    schema_names_in_db = schemas_in_db["schema_names"]

    editor_setting = {"compute_engine": compute_engine}

    # base_blocks_data = [block._export() for block in base_blocks]

    if isinstance(base_blocks, List):
        base_blocks_data = [block._export() for block in base_blocks]
        base_blocks_list = base_blocks
    elif isinstance(base_blocks, Dict):
        base_blocks_data = []
        base_blocks_list = []
        for category, block_list in base_blocks.items():
            if isinstance(block_list, List):
                for block in block_list:
                    base_blocks_list.append(block)
                    block_data = block._export()
                    block_data["category"] = category
                    base_blocks_data.append(block_data)
            else:
                raise TypeError(
                    "Invalid type for base_blocks passed to the st_barfi component."
                )
    else:
        raise TypeError(
            "Invalid type for base_blocks passed to the st_barfi component."
        )

    _from_client = _component_func(
        base_blocks=base_blocks_data,
        load_editor_schema=editor_schema,
        load_schema_names=schema_names_in_db,
        load_schema_name=load_schema,
        editor_setting=editor_setting,
        key=key,
        default={"command": "skip", "editor_state": {}},
    )

    if _from_client["command"] == "execute":
        if compute_engine:
            _ce = ComputeEngine(blocks=base_blocks_list)
            _ce.add_editor_state(_from_client["editor_state"])
            _ce._map_block_link()
            _ce._execute_compute()
            return _ce.get_result()
        else:
            _ce = ComputeEngine(blocks=base_blocks_list)
            _ce.add_editor_state(_from_client["editor_state"])
            _ce._map_block_link()
            # return _ce.get_result()
            return _from_client
    if _from_client["command"] == "save":
        save_schema(
            schema_name=_from_client["schema_name"],
            schema_data=_from_client["editor_state"],
        )
    if _from_client["command"] == "load":
        load_schema = _from_client["schema_name"]
        editor_schema = load_schema_name(load_schema)
    else:
        pass

    return {}


def barfi_schemas():
    schemas_in_db = load_schemas()
    schema_names_in_db = schemas_in_db["schema_names"]

    return schema_names_in_db
