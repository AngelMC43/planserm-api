from sqlalchemy.orm import Session

from repositories.models.comunidades_models import Clients
from repositories.models.user_models import User
from repositories.models.labors_models import Labors

from repositories.schemas import ClientsData, UserData, LaborsData


def get_users(db: Session):
    return db.query(User).all()


def get_user_by_id(db: Session, id: int):
    return db.query(User).filter(User.id == id).first()


def get_user_by_name(db: Session, name: str):
    return db.query(User).filter(User.name == name).first()


def create_user(db: Session, user: UserData):
    new_user = User(name=user.name, password=user.password)
    db.add(new_user)
    db.commit()
    db.flush(new_user)
    return new_user


# CLIENTS


def get_clients(db: Session):
    return db.query(Clients).all()


def get_client_id(db: Session, id: int):
    return db.query(Clients).filter(Clients.id == id).first()


def get_client_by_name(db: Session, comunidad: str):
    return db.query(Clients).filter(Clients.comunidad == comunidad).first()


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
    db.commit()
    db.flush(new_client)
    return new_client


# LABORS


def get_labors(db: Session):
    return db.query().all(Labors)


def create_labor(db: Session, labor: LaborsData):
    new_labor = Labors(
        tipo=labor.tipo,
    )
    db.add(new_labor)
    db.commit()
    db.flush(new_labor)
    return new_labor
