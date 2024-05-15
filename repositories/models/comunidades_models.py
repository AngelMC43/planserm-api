from sqlalchemy import Column, String, Integer

from database import Base


class Clients(Base):
    __tablename__ = 'Comunidades'

    id = Column(Integer, primary_key=True, index=True)
    comunidad = Column(String(30), unique=True)
    presidente = Column(String(30))
    direccion = Column(String(70))
    municipio = Column(String(30))
    servicios = Column(String(255))
    telefono_contacto = Column(String(10))
    domicilio_presidente = Column(String(20))
