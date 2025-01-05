# 01: These would be the basic imports to get started
import streamlit as st
from barfi.flow import Block, SchemaManager, ComputeEngine, st_flow


# 02: The first block you'll create is one where you can set the number
number_block = Block(name="Number")
number_block.add_output(name="Output 1")
number_block.add_option(
    name="display-option", type="display", value="This is a Block with Number option."
)
number_block.add_option(name="number-block-option", type="number")


def number_block_func(self):
    number_value = self.get_option(name="number-block-option")
    self.set_interface(name="Output 1", value=option_value)


number_block.add_compute(number_block_func)

# 03: The second block will be one that just prints the number
result_block = Block(name="Result")
result_block.add_input(name="Input 1")
result_block.add_option(
    name="display-option", type="display", value="This is a Result Block."
)


def result_block_func(self):
    number_value = self.get_interface(name="Input 1")
    print(number_value)


result_block.add_compute(result_block_func)

# ... existing code as above ...

# 04: The st_flow takes in the base blocks and returns the schema
barfi_result = st_flow(base_blocks=[number_block, result_block])

# 05: You can view the schema here
st.write(barfi_result)

# ... existing code as above ...

# 06: Initialize your compute engine with the base_blocks and execute the schema.
compute_engine = ComputeEngine([number_block, result_block])

# 07: Reference to the flow_schema from the barfi_result
flow_schema = barfi_result.editor_schema
compute_engine.execute(flow_schema)
