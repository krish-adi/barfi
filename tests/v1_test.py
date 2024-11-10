from barfi import st_flow
import streamlit as st
from test_blocks import base_blocks_category
from barfi.st_flow.block.prepare import prepare_blocks_export
from barfi.st_flow.schema import (
    load_schema_name,
    barfi_schemas,
    save_schema,
    prepare_editor_schema,
)

base_blocks = base_blocks_category["process"]
load_schema = "schema-basic"
base_blocks_data, base_blocks_list = prepare_blocks_export(base_blocks)
editor_schema = prepare_editor_schema(load_schema, base_blocks_data)

barfi_result = st_flow(
    base_blocks=base_blocks,
    editor_schema=editor_schema,
)
st.write(barfi_result)

# if _from_client["command"] != "skip":
#     _editor_state_from_client = migrate_state_from_ui(
#         base_blocks_data,
#         _from_client["editor_state"]["nodes"],
#         _from_client["editor_state"]["connections"],
#     )
#     _editor_state_from_client["viewport"] = _from_client["editor_state"]["viewport"]

#     if _from_client["command"] == "execute":
#         if compute_engine:
#             _ce = ComputeEngine(blocks=base_blocks_list)
#             _ce.add_editor_state(_editor_state_from_client)
#             _ce._map_block_link()
#             _ce._execute_compute()
#             return _ce.get_result()
#         else:
#             _ce = ComputeEngine(blocks=base_blocks_list)
#             _ce.add_editor_state(_editor_state_from_client)
#             _ce._map_block_link()
#             # return _ce.get_result()
#             return {"command": "execute", "editor_state": _editor_state_from_client}
#     if _from_client["command"] == "save":
#         save_schema(
#             schema_name=_from_client["schema_name"],
#             schema_data=_editor_state_from_client,
#         )
#     if _from_client["command"] == "load":
#         load_schema = _from_client["schema_name"]
#         editor_schema = load_schema_name(load_schema)
# else:
#     return {}
