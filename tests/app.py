from dataclasses import asdict
import streamlit as st
from barfi import st_flow
from barfi.config import SCHEMA_VERSION
from barfi.st_flow.schema.manage import SchemaManager
from barfi.st_flow.flow.types import FlowSchema, FlowViewport
from assets.blocks import base_blocks


schema_manager = SchemaManager(filepath="./assets/")
# st.write(schema_manager.schema_names)
load_schema_name = st.selectbox("Schema name", [None] + schema_manager.schema_names)


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


tab1, tab2, tab3 = st.tabs(["View Schema", "Save Schema", "Update Schema"])

with tab1:
    st.write(asdict(barfi_result))
    # st.write(barfi_result)
    # st.write(
    #     [(n.name, n.options, n.inputs, n.outputs) for n in barfi_result.editor_schema.nodes]
    # )
with tab2:
    with st.form("save_schema"):
        schema_name = st.text_input("Schema name")
        if st.form_submit_button("Save schema"):
            schema_manager.save_schema(schema_name, barfi_result.editor_schema)
with tab3:
    with st.form("update_schema"):
        if st.form_submit_button("Update schema"):
            schema_manager.update_schema(load_schema_name, barfi_result.editor_schema)
