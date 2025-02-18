from fastapi import FastAPI

from automation.routers import json_converter


app = FastAPI()


app.include_router(json_converter.router)


@app.get("/")
def root():
    return {"message": "Akamai Automation"}
