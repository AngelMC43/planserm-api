from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Conexión a la base de datos a través de create_engine()

URL_CONNECTION = 'mssql+pymssql://sa:talan2022@TAL-9P3V7S3/planserm'

engine = create_engine(URL_CONNECTION)

localSession = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()
