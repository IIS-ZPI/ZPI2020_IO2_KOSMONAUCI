import json

from nbp import get_table
from jsonschema import validate


def _load_json_schema(path):
    with open(path) as schema_file:
        return json.loads(schema_file.read())


def test():
    schema = _load_json_schema("support/schemas/get_table.json")

test()
print("OK!")
