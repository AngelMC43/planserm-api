from sqlalchemy.orm import Session
from repositories.models.user_models import User
from repositories.schemas import UserData
# Aqui van todas las queries a db, en este caso "user", para otra tabla otro archivo


def get_users(db: Session):
    return db.query(User).all()


def get_user_by_id(db: Session, id: int):
    return db.query(User).filter(User.id == id).first()


def get_user_by_name(db: Session, name: str):
    return db.query(User).filter(User.name == name).first()


def create_user(db: Session, user: UserData):
    fake_password = user.password + '#fake'
    new_user = User(name=user.name, password=fake_password)
    db.add(new_user)
    db.commit()
    db.flush(new_user)
    return new_user
