from fastapi import APIRouter

import pandas as pd

from automation.internal.servivce import json_converter_service


router = APIRouter()

@router.get("/json-to-csv")
def convert_json_to_csv(sep: str = "."):
    data = [
        {"name": "amrendra", "class": 1},
        {"name": "mayuri", "class": 2},
        {"name": "sharme", "class": 1},
    ]
    return json_converter_service.convert_to_csv(data, sep)



@router.get("/csv-separtor")
def get_csv_separator():
    return {"message": "hello"}
