from pydantic import BaseModel
from datetime import datetime



class PermissionBase(BaseModel):
    name: str
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
