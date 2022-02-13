import sys
sys.path.append('../')
from test_blocks import feed, result, mixer, splitter
import streamlit as st
from barfi import st_barfi, ComputeEngine
from matplotlib import pyplot as plt


blocks = [feed, result, mixer, splitter]
ce = ComputeEngine(blocks=blocks)

result = st_barfi(base_blocks=blocks, compute_engine=ce, load_schema='schema-basic')
st.write(result)

# st.write('### DAG Graph of the computational block-link')
# fig, ax = plt.subplots(figsize=(12, 6))
# nx.draw(self._graph, with_labels=True, node_color='lightblue',
#         node_size=500, labels=self._map_block_id_name)
# st.pyplot(fig)

# st.write(_compu_order)

# st.write(self._active_blocks)
# st.write(self._map_block_id_name)
# st.write(self._map_interface_id_block_id)
# st.write(self._map_interface_id_name)
# st.write(self._map_link_interface_id_from_to)
# st.write(self._map_link_interface_id_to_from)
