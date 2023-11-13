from fastapi import APIRouter, Depends

from config.schemas import UserBase
from todo import controllers
from config.database import get_db

router = APIRouter(prefix='/user', tags=['user'])

# create user
@router.post('/')
async def create_user(user:UserBase, db=Depends(get_db)):
    return controllers.create_user(db, user)