########################################################################################################################
# IMPORTS

import json

import typer
from typing_extensions import Annotated

########################################################################################################################
# TYPES

class Dict:
    def __init__(self, value: str):
        self.value = json.loads(value)

    def __str__(self):
        return str(self.value)


def parse_json_dict(value: str) -> Dict:
    try:
        return Dict(value)
    except json.JSONDecodeError as err:
        raise ValueError(f"Invalid JSON string: {value}") from err
    

DictArg = Annotated[Dict, typer.Argument(parser=parse_json_dict)]
DictOpt = Annotated[Dict, typer.Option(parser=parse_json_dict)]