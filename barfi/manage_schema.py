import os
import pickle
from typing import Dict

editor_preset = {
    "nodes": [
        {
            "type": "Feed",
            "id": "node_16421654445600",
            "name": "Feed-1",
            "options": [],
            "state": {},
            "interfaces": [["Output 1", {"id": "ni_16421654445601", "value": None}]],
            "position": {"x": 53.10270771798835, "y": 103.53598351788409},
            "width": 200,
            "twoColumn": False,
            "customClasses": "",
        },
        {
            "type": "Feed",
            "id": "node_16421655709876",
            "name": "Feed-2",
            "options": [],
            "state": {},
            "interfaces": [["Output 1", {"id": "ni_16421655709877", "value": None}]],
            "position": {"x": -110.96319142010879, "y": 354.1711813273622},
            "width": 200,
            "twoColumn": False,
            "customClasses": "",
        },
        {
            "type": "Splitter",
            "id": "node_16421655753058",
            "name": "Splitter-1",
            "options": [],
            "state": {},
            "interfaces": [
                ["Input 1", {"id": "ni_16421655753069", "value": None}],
                ["Output 1", {"id": "ni_164216557530610", "value": None}],
                ["Output 2", {"id": "ni_164216557530611", "value": None}],
            ],
            "position": {"x": 160.08999419005372, "y": 242.060177855096},
            "width": 200,
            "twoColumn": False,
            "customClasses": "",
        },
        {
            "type": "Mixer",
            "id": "node_164216557860312",
            "name": "Mixer-1",
            "options": [],
            "state": {},
            "interfaces": [
                ["Input 1", {"id": "ni_164216557860313", "value": None}],
                ["Input 2", {"id": "ni_164216557860314", "value": None}],
                ["Output 1", {"id": "ni_164216557860315", "value": None}],
            ],
            "position": {"x": 428.30492654775384, "y": 112.91965486805523},
            "width": 200,
            "twoColumn": False,
            "customClasses": "",
        },
        {
            "type": "Result",
            "id": "node_164216558728816",
            "name": "Result-1",
            "options": [],
            "state": {},
            "interfaces": [["Input 1", {"id": "ni_164216558728817", "value": None}]],
            "position": {"x": 426.88579992152256, "y": 335.7225351863563},
            "width": 200,
            "twoColumn": False,
            "customClasses": "",
        },
    ],
    "connections": [
        {
            "id": "164216559410520",
            "from": "ni_16421654445601",
            "to": "ni_164216557860313",
        },
        {
            "id": "164216559592723",
            "from": "ni_164216557530610",
            "to": "ni_164216557860314",
        },
        {
            "id": "164216559830026",
            "from": "ni_164216557530611",
            "to": "ni_164216558728817",
        },
        {
            "id": "164216560187829",
            "from": "ni_16421655709877",
            "to": "ni_16421655753069",
        },
    ],
    "panning": {"x": 163.41400013998373, "y": 110.67177791961308},
    "scaling": 0.7761150375278565,
}
editor_preset_with_loop = {
    "nodes": [
        {
            "type": "Feed",
            "id": "node_16421654445600",
            "name": "Feed",
            "options": [],
            "state": {},
            "interfaces": [["Output 1", {"id": "ni_16421654445601", "value": None}]],
            "position": {"x": 53.10270771798835, "y": 103.53598351788409},
            "width": 200,
            "twoColumn": False,
            "customClasses": "",
        },
        {
            "type": "Feed",
            "id": "node_16421655709876",
            "name": "Feed",
            "options": [],
            "state": {},
            "interfaces": [["Output 1", {"id": "ni_16421655709877", "value": None}]],
            "position": {"x": -395.9608670807274, "y": 296.0466553702624},
            "width": 200,
            "twoColumn": False,
            "customClasses": "",
        },
        {
            "type": "Splitter",
            "id": "node_16421655753058",
            "name": "Splitter",
            "options": [],
            "state": {},
            "interfaces": [
                ["Input 1", {"id": "ni_16421655753069", "value": None}],
                ["Output 1", {"id": "ni_164216557530610", "value": None}],
                ["Output 2", {"id": "ni_164216557530611", "value": None}],
            ],
            "position": {"x": 160.08999419005372, "y": 242.060177855096},
            "width": 200,
            "twoColumn": False,
            "customClasses": "",
        },
        {
            "type": "Mixer",
            "id": "node_164216557860312",
            "name": "Mixer",
            "options": [],
            "state": {},
            "interfaces": [
                ["Input 1", {"id": "ni_164216557860313", "value": None}],
                ["Input 2", {"id": "ni_164216557860314", "value": None}],
                ["Output 1", {"id": "ni_164216557860315", "value": None}],
            ],
            "position": {"x": 428.30492654775384, "y": 112.91965486805523},
            "width": 200,
            "twoColumn": False,
            "customClasses": "",
        },
        {
            "type": "Result",
            "id": "node_164216558728816",
            "name": "Result",
            "options": [],
            "state": {},
            "interfaces": [["Input 1", {"id": "ni_164216558728817", "value": None}]],
            "position": {"x": 698.7229579146288, "y": 245.71451925962754},
            "width": 200,
            "twoColumn": False,
            "customClasses": "",
        },
        {
            "type": "Mixer",
            "id": "node_164233731511530",
            "name": "Mixer",
            "options": [],
            "state": {},
            "interfaces": [
                ["Input 1", {"id": "ni_164233731511631", "value": None}],
                ["Input 2", {"id": "ni_164233731511632", "value": None}],
                ["Output 1", {"id": "ni_164233731511633", "value": None}],
            ],
            "position": {"x": -112.723576361132, "y": 375.92941903750454},
            "width": 200,
            "twoColumn": False,
            "customClasses": "",
        },
        {
            "type": "Splitter",
            "id": "node_164233736008643",
            "name": "Splitter",
            "options": [],
            "state": {},
            "interfaces": [
                ["Input 1", {"id": "ni_164233736008644", "value": None}],
                ["Output 1", {"id": "ni_164233736008645", "value": None}],
                ["Output 2", {"id": "ni_164233736008646", "value": None}],
            ],
            "position": {"x": 421.64706550252777, "y": 310.3049542472305},
            "width": 200,
            "twoColumn": False,
            "customClasses": "",
        },
    ],
    "connections": [
        {
            "id": "164216559410520",
            "from": "ni_16421654445601",
            "to": "ni_164216557860313",
        },
        {
            "id": "164216559592723",
            "from": "ni_164216557530610",
            "to": "ni_164216557860314",
        },
        {
            "id": "164233732351836",
            "from": "ni_164233731511633",
            "to": "ni_16421655753069",
        },
        {
            "id": "164233734787542",
            "from": "ni_16421655709877",
            "to": "ni_164233731511631",
        },
        {
            "id": "164233736975950",
            "from": "ni_164216557530611",
            "to": "ni_164233736008644",
        },
        {
            "id": "164233738304254",
            "from": "ni_164233736008645",
            "to": "ni_164216558728817",
        },
        {
            "id": "164233739219957",
            "from": "ni_164233736008646",
            "to": "ni_164233731511632",
        },
    ],
    "panning": {"x": 462.8955070935626, "y": 373.0757152670363},
    "scaling": 0.4821928840637319,
}


def load_schemas():
    try:
        prefix = os.environ.get("BARFI_BASE_PATH", "")
        schema_file = f"{prefix}/schemas.barfi"

        with open(schema_file, "rb") as handle_read:
            schemas = pickle.load(handle_read)
    except FileNotFoundError:
        schemas = {}

    schema_names = list(schemas.keys())
    return {"schema_names": schema_names, "schemas": schemas}


def save_schema(schema_name: str, schema_data: Dict):
    try:
        prefix = os.environ.get("BARFI_BASE_PATH", "")
        schema_file = f"{prefix}/schemas.barfi"

        with open(schema_file, "rb") as handle_read:
            schemas = pickle.load(handle_read)
    except FileNotFoundError:
        schemas = {}

    with open(schema_file, "wb") as handle_write:
        schemas[schema_name] = schema_data
        pickle.dump(schemas, handle_write, protocol=pickle.HIGHEST_PROTOCOL)


def load_schema_name(schema_name: str) -> Dict:
    prefix = os.environ.get("BARFI_BASE_PATH", "")
    schemas_barfi = load_schemas(prefix=prefix)
    if schema_name in schemas_barfi["schema_names"]:
        schema = schemas_barfi["schemas"][schema_name]
        return schema
    else:
        raise ValueError(f"Schema :{schema_name}: not found in the saved schemas")


def delete_schema(schema_name: str):
    try:
        prefix = os.environ.get("BARFI_BASE_PATH", "")
        schema_file = f"{prefix}/schemas.barfi"

        with open(schema_file, "rb") as handle_read:
            schemas = pickle.load(handle_read)
    except FileNotFoundError:
        schemas = {}

    if schema_name in schemas:
        del schemas[schema_name]
    else:
        raise ValueError(f"Schema :{schema_name}: not found in the saved schemas")

    with open(schema_file, "wb") as handle_write:
        pickle.dump(schemas, handle_write, protocol=pickle.HIGHEST_PROTOCOL)
