from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    id: int
    email: str
    Name: str
    Parent_User: str
    Password: str
    Office_Phone: str
    Mobile: str
    Platform: str
    Active: str
    Role: str
    createdAt: datetime
    updatedAt: datetime
    deletedAt: datetime
    permissions_id: int


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    permission_id: int

    class Config:
        orm_mode = True


class PermissionBase(BaseModel):
    id: int
    domains: str
    region: str
    type: str
    createdAt: datetime
    updatedAt: datetime


class PermissionCreate(PermissionBase):
    pass


class Permission(PermissionBase):
    id: int

    class Config:
        orm_mode = True


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
