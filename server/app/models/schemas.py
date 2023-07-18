from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str


class UserInDB(BaseModel):
    first_name: str
    last_name: str
    email: str
