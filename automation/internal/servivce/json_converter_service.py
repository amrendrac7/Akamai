import time
import json

from fastapi.responses import StreamingResponse
import pandas as pd

from automation.internal.utils import data_converter


def convert_to_csv(data, sep: str):
    t0 = time.perf_counter()
    # json_data = json.loads(data)
    json_data = data
    # df = pd.DataFrame(
    #     [data_converter.flatten_json(input_, sep) for input_ in json_data]
    # )
    df = pd.DataFrame(data)

    return StreamingResponse(
        iter([df.to_csv(index=False)]),
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment;filename=data.csv"}
    )