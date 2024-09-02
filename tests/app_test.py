from barfi import st_barfi, barfi_schemas, load_schemas, load_schema_name
import streamlit as st
from test_blocks import base_blocks_category


st.write(barfi_schemas())
# schema = load_schema_name("schema-basic")
# st.write(schema)


compute_engine = st.checkbox("Activate barfi compute engine", value=False)

barfi_result = st_barfi(
    base_blocks=base_blocks_category["process"],
    compute_engine=compute_engine,
    load_schema="schema-basic",
)

if barfi_result:
    st.write(barfi_result)
