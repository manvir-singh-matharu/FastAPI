from fastapi import FastAPI
import pandas as pd
import json

app = FastAPI()

@app.get("/csv-to-json/")
async def get_csv_as_json():
    df = pd.read_csv("DATAF.csv")
    return json.loads(df.to_json(orient="records"))