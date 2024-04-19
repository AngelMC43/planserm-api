from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
from database import engine, localSession
from schemas import ClientsData, UserData
from comunidades_models import Clients

from pydantic import BaseModel
import uvicorn


from repositories import user_repository
from database import engine, localSession
from repositories.schemas import UserId, CustomId
from repositories.models.user_models import Base
from services import customer_services

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = localSession()
    try:
        yield db
    finally:
        db.close()


@app.get('/api/users', response_model=list[UserId])
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db=db)


@app.get('/api/users/{id:int}')
def get_user(id, db: Session = Depends(get_db)):
    user_by_id = crud.get_user_by_id(db=db, id=id)
    if user_by_id:
        return user_by_id
    raise HTTPException(status_code=400, detail='error, no hay na')


@app.post('api/users/{id:int}', reponse_model=[UserId])
def create_user(user: UserId, db: Session = Depends(get_db)):
    check_name = crud.get_user_by_id(db=db, id=user.id)
    if check_name:
        raise HTTPException(status_code=404, detail='Ya existe')
    return crud.get_user_by_id(db=db, id=id)

    # aqui llamo al controller(realmente llamaria a la ruta route) para hacer flujo


@ app.get('/api/clients', response_model=list[CustomId])
def get_clients(db: Session = Depends(get_db)):
    client = crud.get_all_customers(db)
    return client


@ app.get('/api/clients/{id}', response_model=list[CustomId])
def get_client_id(db: Session = Depends(get_db)):
    client = customer_services.get_all_customers(db)
    return client


class Client(BaseModel):
    comunidad: str
    presidente: str
    direccion: str
    municipio: str
    servicios: str
    telefono_contacto: int
    domicilio_presidente: str


@ app.post('/api/clients')
def create_client(client: Client, db: Session = Depends(get_db)):
    client.append(client)
    return {'successful deleted'}


@ app.get('/')
def root():
    return {'message': 'Conectado'}


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
