from sqlalchemy.orm import Session
from repositories.models.comunidades_models import Customer


# Aqui van todas las queries a db


def get_customers(db: Session):
    return db.query(Customer).all()
