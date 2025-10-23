from fastapi import FastAPI, Cookie
from typing import Annotated

app = FastAPI()

@app.get("/items/")
async def read_items(q: Annotated[str | None, Cookie()] = None):
    return {"q": q}