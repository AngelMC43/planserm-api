from fastapi import FastAPI
from typing import Text, Optional
from datetime import datetime
from enum import Enum
from pydantic import BaseModel

app = FastAPI()


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
