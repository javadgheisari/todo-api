from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from typing import List

from todo.models import User
from todo.schemas import UserBase, UserDisplay
from todo import controllers
from config.database import get_db

router = APIRouter(prefix='/user', tags=['user'])

# create user
@router.post('/', response_model=UserDisplay)
async def create_user(user:UserBase, db=Depends(get_db)):
    return controllers.create_user(db, user)

# # retreive user
# @router.get('/{id}', response_model=UserBase)
# async def retreive_user(id:int, db=Depends(get_db)):
#     user = controllers.retreive_user(id, db)
#     return user

# retreive user
@router.get('/{id}', response_model=UserBase)
async def retreive_user(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    return user

# all users
@router.get('/users/', response_model=List[UserDisplay])
async def get_all_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

# update user
@router.put('/{id}')
def update_user(id: int, user: UserBase, db=Depends(get_db)):
    return controllers.update_user(id, db, user)
 
# delete user
@router.delete('/{id}')
def delete_user(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    db.delete(user)
    db.commit()
    return 'deleted'
    