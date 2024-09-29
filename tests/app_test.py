from barfi import st_barfi, barfi_schemas, load_schema_name
import streamlit as st
from test_blocks import base_blocks_category

test_case_list = ["load-legacy__schema-basic", "load__math"]
test_case = test_case_list[1]

if test_case == "load-legacy__schema-basic":
    st.write(barfi_schemas())
    schema = load_schema_name("schema-basic")
    st.write(schema)

    compute_engine = st.checkbox("Activate barfi compute engine", value=True)

    barfi_result = st_barfi(
        base_blocks=base_blocks_category["process"],
        compute_engine=compute_engine,
        load_schema="schema-basic",
    )

    if barfi_result:
        st.write(barfi_result)
        st.write(barfi_result["Result-1"]["block"].get_interface("Input 1"))
elif test_case == "load__math":
    compute_engine = st.checkbox("Activate barfi compute engine", value=True)

    barfi_result = st_barfi(
        base_blocks=base_blocks_category["math"], compute_engine=compute_engine
    )

    if barfi_result:
        st.write(barfi_result)
        st.write(barfi_result["Result-1"]["block"].get_interface("Input 1"))
