from pydantic import BaseModel


class UserData(BaseModel):
    id: int
    name: str
    password: str


class ClientsData(BaseModel):
    id: int
    comunidad: str
    presidente: str
    direccion: str
    municipio: str
    servicios: str
    telefono_contacto: int
    domicilio_presidente: str
