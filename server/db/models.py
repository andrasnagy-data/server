"""
Data base tables.
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.schema import Table
from sqlalchemy_utils.types import EmailType

from server.db.conn import Base


class User(Base):
    """
    Users table.
    """

    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(EmailType, nullable=False)
    version = Column(Integer, nullable=False)


# association table
relationships = Table(
    "relationships",
    Base.metadata,
    Column("follower", Integer, ForeignKey("user.id")),
    Column("followee", Integer, ForeignKey("user.id")),
)
