import json
from pprint import pprint
from barfi.st_flow.flow.types import build_flow_schema_from_dict


def load_schema():
    with open("./assets/schema_wall.json", "r") as f:
        schema = json.load(f)

    pprint(build_flow_schema_from_dict(schema.get("editor_schema")))


# load_schema()
