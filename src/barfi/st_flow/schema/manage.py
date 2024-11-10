import pickle
from typing import Dict


def load_schemas():
    try:
        with open("schemas.barfi", "rb") as handle_read:
            schemas = pickle.load(handle_read)
    except FileNotFoundError:
        schemas = {}

    schema_names = list(schemas.keys())
    return {"schema_names": schema_names, "schemas": schemas}


def save_schema(schema_name: str, schema_data: Dict):
    try:
        with open("schemas.barfi", "rb") as handle_read:
            schemas = pickle.load(handle_read)
    except FileNotFoundError:
        schemas = {}

    with open("schemas.barfi", "wb") as handle_write:
        schemas[schema_name] = schema_data
        pickle.dump(schemas, handle_write, protocol=pickle.HIGHEST_PROTOCOL)


def load_schema_name(schema_name: str) -> Dict:
    schemas_barfi = load_schemas()
    if schema_name in schemas_barfi["schema_names"]:
        schema = schemas_barfi["schemas"][schema_name]
        return schema
    else:
        raise ValueError(f"Schema :{schema_name}: not found in the saved schemas")


def delete_schema(schema_name: str):
    try:
        with open("schemas.barfi", "rb") as handle_read:
            schemas = pickle.load(handle_read)
    except FileNotFoundError:
        schemas = {}

    if schema_name in schemas:
        del schemas[schema_name]
    else:
        raise ValueError(f"Schema :{schema_name}: not found in the saved schemas")

    with open("schemas.barfi", "wb") as handle_write:
        pickle.dump(schemas, handle_write, protocol=pickle.HIGHEST_PROTOCOL)


def barfi_schemas():
    schemas_in_db = load_schemas()
    schema_names_in_db = schemas_in_db["schema_names"]

    return schema_names_in_db
