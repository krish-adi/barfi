import pickle 

data = {'schema-2': {'data' : 'some random dict'}}
schema_name = list(data.keys())[0]
schema_data = data[schema_name]

try:
    with open('try.barfi', 'rb') as handle_read:
        schemas = pickle.load(handle_read)
except FileNotFoundError:
    schemas = {}

print(schemas)

with open('try.barfi', 'wb') as handle_write:
    schemas[schema_name] = schema_data
    pickle.dump(schemas, handle_write, protocol=pickle.HIGHEST_PROTOCOL)

with open('try.barfi', 'rb') as handle_read:
    schemas = pickle.load(handle_read)
    print(schemas)


# st.write('### DAG Graph of the computational block-link')
# fig, ax = plt.subplots(figsize=(12, 6))
# nx.draw(_ce._graph, with_labels=True, node_color='lightblue',
#         node_size=500, labels=_ce._map_block_id_name)
# st.pyplot(fig)

# st.write(_compu_order)

# st.write(_ce._active_blocks)
# st.write(_ce._map_block_id_name)
# st.write(_ce._map_interface_id_block_id)
# st.write(_ce._map_interface_id_name)
# st.write(_ce._map_link_interface_id_from_to)
# st.write(_ce._map_link_interface_id_to_from)