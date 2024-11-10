import streamlit.components.v1 as components
from typing import List, Dict, Union

# import st_flow components
from barfi.st_flow.block import Block
from barfi.st_flow.block.prepare import prepare_blocks_export
from barfi.st_flow.flow.compute import ComputeEngine
from barfi.st_flow.schema import (
    load_schema_name,
    barfi_schemas,
    save_schema,
    prepare_editor_schema,
)
from barfi.utils.migration import migrate_state_from_ui
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
    load_schema: str = None,
    compute_engine: bool = True,
    key=None,
):
    base_blocks_data, base_blocks_list = prepare_blocks_export(base_blocks)
    editor_schema = prepare_editor_schema(load_schema, base_blocks_data)

    schema_names_in_db = barfi_schemas()

    editor_setting = {"compute_engine": compute_engine}

    # TODO: Add custom commands, to make it customize to act upon a command bar of tools
    # and commmands and how to render them on the ui
    _from_client = _component_func(
        base_blocks=base_blocks_data,
        load_editor_schema=editor_schema,
        load_schema_names=schema_names_in_db,
        load_schema_name=load_schema,
        editor_setting=editor_setting,
        key=key,
        default={"command": "skip", "editor_state": {}},
    )

    if _from_client["command"] != "skip":
        _editor_state_from_client = migrate_state_from_ui(
            base_blocks_data,
            _from_client["editor_state"]["nodes"],
            _from_client["editor_state"]["connections"],
        )
        _editor_state_from_client["viewport"] = _from_client["editor_state"]["viewport"]

        # _typed_barfi_response = BarfiResponse(
        #     command=_from_client["command"],
        #     editor_state=FlowEditorState(
        #         nodes=[FlowNode(**node) for node in _editor_state_from_client["nodes"]],
        #         connections=[
        #             FlowConnection(**conn)
        #             for conn in _editor_state_from_client["connections"]
        #         ],
        #         viewport=FlowViewport(**_editor_state_from_client["viewport"]),
        #     ),
        # )

        # print(_typed_barfi_response)

        if _from_client["command"] == "execute":
            if compute_engine:
                _ce = ComputeEngine(blocks=base_blocks_list)
                _ce.add_editor_state(_editor_state_from_client)
                _ce._map_block_link()
                _ce._execute_compute()
                return _ce.get_result()
            else:
                _ce = ComputeEngine(blocks=base_blocks_list)
                _ce.add_editor_state(_editor_state_from_client)
                _ce._map_block_link()
                # return _ce.get_result()
                return {"command": "execute", "editor_state": _editor_state_from_client}
        if _from_client["command"] == "save":
            save_schema(
                schema_name=_from_client["schema_name"],
                schema_data=_editor_state_from_client,
            )
        if _from_client["command"] == "load":
            load_schema = _from_client["schema_name"]
            editor_schema = load_schema_name(load_schema)
    else:
        return {}
