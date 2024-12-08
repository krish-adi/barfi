from barfi import st_flow
from barfi.st_flow.schema.manage import SchemaManager
import streamlit as st
from assets import base_blocks_category
import json

# from barfi.st_flow.block.prepare import prepare_blocks_export
from barfi.st_flow.flow.types import build_streamlit_flow_response

schema_manager = SchemaManager()

base_blocks = base_blocks_category["math"]
# load_schema = "schema-basic"
# base_blocks_data, base_blocks_list = prepare_blocks_export(base_blocks)
# editor_schema = prepare_editor_schema(load_schema, base_blocks_data)
with open("v1_app_result.json", "r") as f:
    barfi_result = build_streamlit_flow_response(json.load(f))

st.write(barfi_result)
st.write(barfi_result.editor_schema)

schema_manager.save_schema("test_schema_math", barfi_result.editor_schema)
st.write(schema_manager.schema_names)

load_schema = schema_manager.load_schema("test_schema_math")
st.write(load_schema)

# barfi_result = st_flow(
#     base_blocks=base_blocks,
#     # editor_schema=editor_schema,
# )
# st.write(barfi_result)
# with st.form("save_barfi_result"):
#     st.write("Save Barfi Result")
#     # Every form must have a submit button.
#     submitted = st.form_submit_button("Submit")
#     if submitted:
#         with open("v1_app_result.json", "w") as f:
#             json.dump(barfi_result, f)
#         st.write("Barfi result saved!")


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
