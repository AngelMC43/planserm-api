from sqlalchemy.orm import Session

from models import Clients
from squema import ClientsData, UserData


def get_user_by_id(db: Session, id: int):
    return db.query(UserData).filter(UserData.id == id).first()


def get_user_by_name(db: Session, name: str):
    return db.query(Clients).filter(Clients.name == name).first()


def get_clients(db: Session):
    return db.query(Clients).all()


def get_client_id(db: Session, id: int):
    return db.query(Clients).filter(Clients.id == id).first()


def get_client_by_name(db: Session, name: str):
    return db.query(Clients).filter(Clients.name == name).first()


# def create_user(db: Session, client: ClientsData):
#     new_user = Clients(
#         name=name
#     )
#     db.add(new_user)
#     db.flush(new_user)
#     return new_user


def create_client(db: Session, client: ClientsData):
    new_client = Clients(
        comunidad=client.comunidad,
        presidente=client.presidente,
        direccion=client.direccion,
        municipio=client.municipio,
        servicios=client.servicios,
        telefono_contacto=client.telefono_contacto,
        domicilio_presidente=client.domicilio_presidente
    )
    db.add(new_client)
    db.flush(new_client)
    return new_client
