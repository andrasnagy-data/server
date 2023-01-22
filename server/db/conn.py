"""
Database connection setup.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_CONN_STRING: str = "sqlite+pysqlite:///demo.db"

engine = create_engine(DATABASE_CONN_STRING, echo=True, future=True)
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
