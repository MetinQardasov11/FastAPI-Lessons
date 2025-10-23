from fastapi import FastAPI, Response
from pydantic import BaseModel, EmailStr
from typing import Any
from fastapi.responses import JSONResponse, RedirectResponse

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []
    
    
class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None
    
    
class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None
    
    
class UserIn(BaseUser):
    password: str


@app.post("/user/")
async def create_user(user: UserIn) -> UserIn:
    return user


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    return user


@app.post("/items/")
async def create_item(item: Item) -> Item:
    return item


@app.get("/items/")
async def read_items() -> list[Item]:
    return [Item(name="Portal Gun", price=42.0, description="Powerful gun from the matrix"), Item(name="Plumbus", price=32.0)]



@app.get("/portal")
async def get_portal(teleport: bool = False) -> Response:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return JSONResponse(content={"message": "Here's your interdimensional portal."})


@app.get("/teleport")
async def get_teleport() -> RedirectResponse:
    return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")