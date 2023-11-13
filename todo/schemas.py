from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    name : str

class Image(BaseModel):
    id: int
    name: str | None = None

class Item(BaseModel):
    name: str
    desc: str | None = None
    ids: list = []
    image: Image | None = None