import sys
sys.path.append('../')
from matplotlib import pyplot as plt
from barfi import st_barfi, barfi_schemas
import streamlit as st
from test_blocks import base_blocks, base_blocks_category



barfi_schema_name = st.selectbox(
    'Select a saved schema to load:', barfi_schemas())

compute_engine = st.checkbox('Activate barfi compute engine', value=False)

barfi_result = st_barfi(base_blocks=base_blocks_category, compute_engine=compute_engine, load_schema=barfi_schema_name)

if barfi_result:
    st.write(barfi_result)
    st.write(barfi_result['Feed-1']['block'].get_interface('Output 1'))
    st.write(barfi_result['Feed-2']['block'].get_interface('Output 1'))
    st.write(barfi_result['Splitter-1']['block'].get_interface('Input 1'))
    st.write(barfi_result['Splitter-1']['block'].get_interface('Output 1'))
    st.write(barfi_result['Splitter-1']['block'].get_interface('Output 2'))
    st.write(barfi_result['Mixer-1']['block'].get_interface('Input 1'))
    st.write(barfi_result['Mixer-1']['block'].get_interface('Input 2'))
    st.write(barfi_result['Mixer-1']['block'].get_interface('Output 1'))
    st.write(barfi_result['Result-1']['block'].get_interface('Input 1'))

    st.write(barfi_result['Feed-1']['block'].get_state('info'))
    st.write(barfi_result['Feed-2']['block'].get_state('info'))
    st.write(barfi_result['Splitter-1']['block'].get_state('info'))
    st.write(barfi_result['Mixer-1']['block'].get_state('info'))
    st.write(barfi_result['Result-1']['block'].get_state('info'))