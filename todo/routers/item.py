from typing import Annotated, Union

from fastapi import APIRouter
from todo.schemas import Item

router = APIRouter(tags=['Item'])

@router.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@router.post("/items/")
async def create_item(item: Item):
    return item