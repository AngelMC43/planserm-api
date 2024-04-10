from pydantic import BaseModel


class UserData(BaseModel):
    name: str
    password: str


class UserId(UserData):
    id: int


class CustomData(BaseModel):
    id: int
    comunidad: str
    presidente: str
    direccion: str
    municipio: str
    servicios: str
    telefono_contacto: int
    domicilio_presidente: str


class CustomId(CustomData):
    id: int
