from barfi import st_flow
import streamlit as st
from assets import base_blocks_category
import json
# from barfi.st_flow.block.prepare import prepare_blocks_export


base_blocks = base_blocks_category["math"]
# load_schema = "schema-basic"
# base_blocks_data, base_blocks_list = prepare_blocks_export(base_blocks)
# editor_schema = prepare_editor_schema(load_schema, base_blocks_data)

barfi_result = st_flow(
    base_blocks=base_blocks,
    # editor_schema=editor_schema,
)
st.write(barfi_result)
with st.form("save_barfi_result"):
    st.write("Save Barfi Result")
    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        with open("v1_app_result.json", "w") as f:
            json.dump(barfi_result, f)
        st.write("Barfi result saved!")


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
