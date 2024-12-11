import streamlit as st
from barfi import st_flow
from barfi.config import SCHEMA_VERSION
from barfi.st_flow.schema.manage import SchemaManager
from barfi.st_flow.flow.types import FlowSchema, FlowViewport
from assets import base_blocks_category


base_blocks = base_blocks_category

schema_manager = SchemaManager()
st.write(schema_manager.schema_names)
# load_schema_name = st.selectbox("Schema name", [None] + schema_manager.schema_names)
load_schema_name = None

if load_schema_name is not None:
    load_schema = schema_manager.load_schema(load_schema_name)
else:
    load_schema = FlowSchema(
        version=SCHEMA_VERSION,
        nodes=[],
        connections=[],
        viewport=FlowViewport(x=0, y=0, zoom=1),
    )

barfi_result = st_flow(
    base_blocks=base_blocks,
    editor_schema=load_schema,
)

st.write([(n.name, n.options) for n in barfi_result.editor_schema.nodes])

# schema_manager.save_schema(schema_name, barfi_result.editor_schema)
