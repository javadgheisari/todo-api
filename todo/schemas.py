from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    name : str
    password : str

class UserDisplay(BaseModel):
    id: int
    email: str
    name : str

    class config:
        orm_mode = True

class Image(BaseModel):
    id: int
    name: str | None = None

class Item(BaseModel):
    name: str
    desc: str | None = None
    ids: list = []
    image: Image | None = None