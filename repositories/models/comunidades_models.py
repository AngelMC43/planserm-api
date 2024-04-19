from sqlalchemy import Column, String, Integer, ARRAY

from database import Base


class Clients(Base):
    __tablename__ = 'Comunidades'

    id = Column(Integer, primary_key=True, index=True)
    comunidad = Column(String(30), unique=True)
    presidente = Column(String(30))
    direccion = Column(String(70))
    municipio = Column(String(30))
    servicios = Column(ARRAY(String()))
    telefono_contacto = Column(Integer)
    domicilio_presidente = Column(String(20))


class Users(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), index=True, )
    password = Column(String(20), index=True)
