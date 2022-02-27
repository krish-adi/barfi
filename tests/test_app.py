import sys
sys.path.append('../')
from matplotlib import pyplot as plt
from barfi import st_barfi, barfi_schemas
import streamlit as st
from test_blocks import feed, result, mixer, splitter

base_blocks = [feed, result, mixer, splitter]

barfi_schema_name = st.selectbox(
    'Select a saved schema to load:', barfi_schemas())

compute_engine = st.checkbox('Activate barfi compute engine', value=False)

schema_execution_result = st_barfi(
    base_blocks=base_blocks, compute_engine=compute_engine, load_schema=barfi_schema_name)

if schema_execution_result:
    st.write(schema_execution_result)
