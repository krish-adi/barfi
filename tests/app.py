from dataclasses import asdict
import streamlit as st
from barfi.flow import SchemaManager, ComputeEngine
from barfi.flow.schema.types import FlowSchema, FlowViewport
from barfi.flow.streamlit import st_flow
from barfi.config import SCHEMA_VERSION
from assets.blocks import base_blocks


schema_manager = SchemaManager(filepath="./assets/")
load_schema_name = st.selectbox("Schema name", [None] + schema_manager.schema_names)

compute_engine = ComputeEngine(base_blocks)


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
    blocks=base_blocks,
    editor_schema=load_schema,
)

tab1, tab2, tab3, tab4 = st.tabs(
    ["View Schema", "Save Schema", "Update Schema", "Inspect Execute Result"]
)

with tab1:
    tab1_1, tab1_2, tab1_3 = st.tabs(
        ["View as dict", "View as object", "View Node Info"]
    )
    with tab1_1:
        st.write(asdict(barfi_result))
    with tab1_2:
        st.write(barfi_result)
    with tab1_3:
        st.write(
            [
                (n.name, n.options, n.inputs, n.outputs)
                for n in barfi_result.editor_schema.nodes
            ]
        )
with tab2:
    with st.form("save_schema"):
        schema_name = st.text_input("Schema name")
        if st.form_submit_button("Save schema"):
            schema_manager.save_schema(schema_name, barfi_result.editor_schema)
with tab3:
    with st.form("update_schema"):
        if st.form_submit_button("Update schema"):
            schema_manager.update_schema(load_schema_name, barfi_result.editor_schema)
with tab4:
    if barfi_result.command == "execute":
        flow_schema = barfi_result.editor_schema
        compute_engine.execute(flow_schema)
        result_block = flow_schema.block(node_label="Result-1")
        st.write(result_block)
        st.write(result_block.get_interface("Input 1"))
    else:
        st.write("No execute command was run.")
