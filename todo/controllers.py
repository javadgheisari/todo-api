from sqlalchemy.orm.session import Session
from config.schemas import UserBase
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