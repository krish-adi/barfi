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