"""
This module contains the database configuration for the api
"""

import os
from typing import Annotated

from dotenv import load_dotenv
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.orm import Session

load_dotenv()

sqlite_url = os.getenv("DATABASE_URL")

engine = create_engine(sqlite_url, pool_pre_ping=True, pool_recycle=3600)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def create_tables():
    """
    Function that creates the tables in the database.
    """
    Base.metadata.create_all(engine)


def get_db():
    """
    Función que se encarga de obtener una conexión a la base de datos.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


SessionDep = Annotated[Session, Depends(get_db)]
