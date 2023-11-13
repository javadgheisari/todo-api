from typing import Annotated, Union

from fastapi import APIRouter
from pydantic import BaseModel

# from main import app
router = APIRouter(tags=['Item'])

class Image(BaseModel):
    id: int
    name: str | None = None

class Item(BaseModel):
    name: str
    desc: str | None = None
    ids: list = []
    image: Image | None = None


@router.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@router.post("/items/")
async def create_item(item: Item):
    return item