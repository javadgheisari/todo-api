from sqlalchemy.orm.session import Session
from todo.schemas import UserBase
from .models import User


def create_user(db:Session, request: UserBase):
    user = User(
        email = request.email,
        name = request.name
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def retreive_user(id, db:Session):
    return db.query(User).filter(User.id == id).first()