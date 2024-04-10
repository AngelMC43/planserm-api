from sqlalchemy import Column, String, Integer

from database import Base

# Aqui estoy creando una nueva tabla. El nombre de este será 'user'
# seguido del nombre de las columnas y en parentesis sus opciones


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), index=True, unique=True)
    password = Column(String(30), index=True, unique=True)
