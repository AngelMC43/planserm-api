from sqlalchemy import Column, String, Integer

from database import Base


class Labors(Base):
    __tablename__ = 'Labors'

    id = Column(Integer, primary_key=True, index=True)
    tipos: Column(String(255))
