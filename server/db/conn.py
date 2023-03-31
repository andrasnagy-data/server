"""
Database connection setup.
"""
import os

from dotenv import find_dotenv, load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# I would prefer to use google cloud secret manager to store sensitive info
load_dotenv(find_dotenv())

DB_CONN_STRING: str = os.environ.get("DB_CONN_STRING")

engine = create_engine(DB_CONN_STRING, echo=True, future=True)
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, future=True
)
Base = declarative_base()


def get_db():
    """
    DB dependency.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
