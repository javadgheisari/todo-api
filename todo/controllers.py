from sqlalchemy.orm.session import Session
from todo.schemas import UserBase
from .models import User
from config.hash import Hash


def create_user(db:Session, request: UserBase):
    user = User(
        email = request.email,
        name = request.name,
        password = Hash.bcrypt(request.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def retreive_user(id, db:Session):
    return db.query(User).filter(User.id == id).first()

def retreive_user(id, db:Session):
    return db.query(User).filter(User.id == id).first()


def update_user(id, db:Session, request: UserBase):
    user = db.query(User).filter(User.id == id)
    user.update({
        User.email : request.email,
        User.name : request.name,
        User.password : Hash.bcrypt(request.password)
    })
    db.commit()
    return 'updated'