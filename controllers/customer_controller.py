
from fastapi import Depends
from sqlalchemy.orm import Session
import repositories.user_repository as user_repository
from database import localSession


# Ubicación donde se monta las solicitudes HTTP
# maneja parametro de entrada y validaciones


# montar funcion fuera

def get_db():
    db = localSession()
    try:
        yield db
    finally:
        db.close()


def get_customers(db: Session = Depends(get_db)):
    return user_repository.get_customers(db=db)
