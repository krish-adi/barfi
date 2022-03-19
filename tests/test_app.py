import sys
sys.path.append('../')
from matplotlib import pyplot as plt
from barfi import st_barfi, barfi_schemas
import streamlit as st
from test_blocks import base_blocks

barfi_schema_name = st.selectbox(
    'Select a saved schema to load:', barfi_schemas())

compute_engine = st.checkbox('Activate barfi compute engine', value=False)

barfi_result = st_barfi(base_blocks=base_blocks, compute_engine=compute_engine, 
load_schema=barfi_schema_name)

if barfi_result:
    st.write(barfi_result)
