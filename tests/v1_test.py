from barfi import st_flow
import streamlit as st
from test_blocks import base_blocks_category

barfi_result = st_flow(
    base_blocks=base_blocks_category["process"],
    load_schema="schema-basic",
)
st.write(barfi_result)
