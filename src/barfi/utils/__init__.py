import gzip
import json


def write_json_as_json_gzip(readfile: str, writefile: str) -> None:
    # write_json_as_json_gzip("./assets/schemas.json", "./assets/schemas.barfi")
    with open(readfile, "r") as rf:
        data = json.load(rf)
    with gzip.open(writefile, "wt", encoding="UTF-8") as wf:
        json.dump(data, wf)
