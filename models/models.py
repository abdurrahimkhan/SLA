import json
from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, func
from sqlalchemy.orm import relationship
from database.database import Base


class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, autoincrement=True)
    Email = Column(String, unique=True)
    Name = Column(String)
    Parent_User = Column(String)
    Password = Column(String)
    Office_Phone = Column(String)
    Mobile = Column(String)
    Platform = Column(String)
    Active = Column(Boolean, default=True)
    Role = Column(String, default="user")
    createdAt = Column(DateTime, default=func.now())
    updatedAt = Column(DateTime, default=func.now(), onupdate=func.now())
    deletedAt = Column(DateTime)
    permissions_id = Column(Integer, ForeignKey('Permissions.id'))

    def to_json(self):
        user_dict = {
            "id": self.id,
            "Email": self.Email,
            "Name": self.Name,
            "Parent_User": self.Parent_User,
            "Password": self.Password,
            "Office_Phone": self.Office_Phone,
            "Mobile": self.Mobile,
            "Platform": self.Platform,
            "Active": self.Active,
            "Role": self.Role,
            "createdAt": self.createdAt.isoformat() if isinstance(self.createdAt, datetime) else None,
            "updatedAt": self.updatedAt.isoformat() if isinstance(self.updatedAt, datetime) else None,
            "deletedAt": self.deletedAt.isoformat() if isinstance(self.deletedAt, datetime) else None,
            "permissions_id": self.permissions_id
        }
        return json.dumps(user_dict)
    # permission = relationship("Permissions", back_populates="users")
    # auth_logs = relationship("UserAuthLog", back_populates="user")


# from pprint import pprint
# (Pdb) pprint(vars(users[0]))
class Permission(Base):
    __tablename__ = "Permissions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    domains = Column(String, default="")
    region = Column(String, default="")
    type = Column(String, default="Contractor Region User")
    createdAt = Column(DateTime, default=func.now())
    updatedAt = Column(DateTime, default=func.now(), onupdate=func.now())

    # users = relationship("User", back_populates="permission")


class UserAuthLog(Base):
    __tablename__ = "UserAuthLogs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String)
    name = Column(String)
    login_time = Column(DateTime, default=func.now())
    user_id = Column(Integer, ForeignKey('User.id'))

    # user = relationship("User", back_populates="auth_logs")


permission = relationship("Permissions", back_populates="users")
auth_logs = relationship("UserAuthLog", back_populates="user")
users = relationship("User", back_populates="permission")
user = relationship("User", back_populates="auth_logs")
