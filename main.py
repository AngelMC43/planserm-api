from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from typing import Text, Optional
from datetime import datetime
from enum import Enum

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
    return user_repository.get_users(db=db)


# aqui llamo al controller(realmente llamaria a la ruta route) para hacer flujo

@app.get('/api/clients', response_model=list[CustomId])
def get_customers(db: Session = Depends(get_db)):
    return customer_services.get_all_customers(db)


class Libro(BaseModel):
    titulo: str
    autor: str
    paginas: int
    editorial: Optional[str]


class Movies (BaseModel):
    id: int
    title: str
    author: str
    year: int
    content: Text
    created: datetime = datetime.now()
    published: bool = False


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


muestras = []


@app.get('/')
def root():
    return {'message': 'Conectado'}


@app.get('/libros/{id}')
def show_book(id: int):
    return {'data': id}


@app.post('/libros')
def insert_book(book: Libro):
    return {'message': f'El libro {book.titulo} se ha insertado'}


@app.get('/pelicula')
def show_movie():
    listado = list(map(lambda movie: movie["id"], muestras))

    return listado


@app.post('/pelicula')
def add_movie(movie: Movies):
    muestras.append(movie.dict())

    return {'messsage': f'Se ha insertado la peli {movie.title}'}


@app.get('/models/{models_name}')
def get_model(models_name: ModelName, needy: str):
    if models_name is ModelName.alexnet:
        return {
            "model_name": "model_name",
            "message": "Deep Learning FTW!",
            "needy": {needy}
        }

    if models_name == "lenet":
        return {"model_name": "model_name", "message": "LeCNN all the images"}

    return {"model_name": "model_name", "message": "Have some residuals"}
