from fastapi import FastAPI
from fastapi.responses import RedirectResponse

import json

app = FastAPI()

@app.get("/{url}")
async def root(url):
    with open("redirects.json") as json_file:
        json_data = json.load(json_file)
        try:
            return RedirectResponse(json_data[url]) 
        except Exception as e:
            return {"message": f"{e}"}


