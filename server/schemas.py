"""
Data schemas.
"""
from pydantic import BaseModel


class User(BaseModel):
    """
    User representation in app.
    """

    name: str
    email: str

    class Config:
        orm_mode = True


class UserInDB(BaseModel):
    """
    User representation in data base.
    """

    first_name: str
    last_name: str
    email: str

    class Config:
        orm_mode = True
