from barfi import st_barfi, barfi_schemas
import streamlit as st
from test_blocks import math_blocks

barfi_schema_name = st.selectbox("Select a saved schema to load:", barfi_schemas())

# st.write(load_schemas())
compute_engine = st.checkbox("Activate barfi compute engine", value=True)

barfi_result = st_barfi(
    base_blocks=math_blocks,
    compute_engine=compute_engine,
    load_schema=barfi_schema_name,
)

if barfi_result:
    st.write(barfi_result["Result 1"]["block"].get_interface(name="Input 1"))
    st.write(barfi_result)
