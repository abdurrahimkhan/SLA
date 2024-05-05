from pydantic import BaseModel
from datetime import datetime


class UserAuthLogBase(BaseModel):
    id: int
    email: str
    name: str
    login_time: datetime


class UserAuthLogCreate(UserAuthLogBase):
    pass


class UserAuthLog(UserAuthLogBase):
    id: int

    class Config:
        orm_mode = True
