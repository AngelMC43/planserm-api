from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
from database import engine, localSession
import uvicorn

from repositories.schemas import UserData, ClientsData, UserId
from repositories.models.user_models import Base
from services import customer_services

Base.metadata.create_all(bind=engine)

app = FastAPI()


# CONEXION DBB


def get_db():
    db = localSession()
    try:
        yield db
    finally:
        db.close()


# USERS


@ app.get('/api/users')
def get_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users


@app.get('/api/users/{id:int}')
def get_user(id, db: Session = Depends(get_db)):
    user_by_id = crud.get_user_by_id(db=db, id=id)
    if user_by_id:
        return user_by_id
    raise HTTPException(status_code=400, detail='error, no hay na')


@app.post('/api/users/', response_model=UserId)
def create_user(user: UserData, db: Session = Depends(get_db)):
    check_name = crud.get_user_by_name(db=db, name=user.name)
    if check_name:
        raise HTTPException(status_code=400, detail='User already exists')
    return crud.create_user(db=db, user=user)


# aqui llamo al controller(realmente llamaria a la ruta route) para hacer flujo

# CLIENTS


@ app.get('/api/clients')
def get_clients(db: Session = Depends(get_db)):
    client = crud.get_clients(db)
    print("🚀 ~ client:", client)
    return client


@ app.get('/api/clients/{id}')
def get_client_id(db: Session = Depends(get_db)):
    client = customer_services.get_clients(db)
    return client


@ app.post('/api/clients')
def create_client(client: ClientsData, db: Session = Depends(get_db)):
    check_name = crud.get_client_by_name(db=db, comunidad=client.comunidad)
    if check_name:
        raise HTTPException(status_code=400, detail='User already exists')
    return crud.create_client(db=db, client=client)


# LABORS

@ app.get()
@ app.get('/')
def root():
    return {'message': 'Conectado'}


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
