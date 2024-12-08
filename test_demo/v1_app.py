import streamlit as st
from barfi import st_flow
from barfi.st_flow.schema.manage import SchemaManager
from assets import base_blocks_category
from dataclasses import asdict

# from barfi.st_flow.block.prepare import prepare_blocks_export

schema_manager = SchemaManager()
st.write(schema_manager.schema_names)

# load_schema = "schema-basic"
# base_blocks_data, base_blocks_list = prepare_blocks_export(base_blocks)
# editor_schema = prepare_editor_schema(load_schema, base_blocks_data)

base_blocks = base_blocks_category["math"]
load_schema = schema_manager.load_schema("test_schema_math")

barfi_result = st_flow(
    base_blocks=base_blocks,
    editor_schema=asdict(load_schema),
)

st.write(barfi_result.editor_schema)

# schema_manager.save_schema("test_schema_math", barfi_result.editor_schema)

# load_schema = schema_manager.load_schema("test_schema_math")
# st.write(load_schema)

# with open("v1_app_result.json", "r") as f:
#     barfi_result = build_streamlit_flow_response(json.load(f))
