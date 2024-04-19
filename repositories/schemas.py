from pydantic import BaseModel


class UserData(BaseModel):
    name: str
    password: str
    id: int


class ClientsData(BaseModel):
    id: int
    comunidad: str
    presidente: str
    direccion: str
    municipio: str
    servicios: str
    telefono_contacto: int
    domicilio_presidente: str
