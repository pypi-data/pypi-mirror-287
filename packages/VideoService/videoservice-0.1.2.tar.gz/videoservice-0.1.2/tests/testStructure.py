from typing import Union, Dict, List
from types import TracebackType

settings = {
    "_filter_by_date": {
        "filter": list[str],
        "active": True | False
    },
    "_filter_by_length": {
        "filter": list[int],
        "active": True | False
    },
    "_filter_by_tags": {
        "filter": list[str],
        "active": True | False
    }}

Expected_type = Dict[str, Dict[str, Union[ Union[ List[str], list[int] ], bool] ] ]

print(isinstance(settings, Expected_type))