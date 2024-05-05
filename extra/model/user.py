from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, func
from sqlalchemy.orm import relationship
from database.database import Base


class User(Base):
    __tablename__ = "users"

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
    permission_id = Column(Integer, ForeignKey('permissions.id'))

    permission = relationship("Permissions", back_populates="users")
    auth_logs = relationship("UserAuthLog", back_populates="user")


# from models.permission import Permission  # Moved import here to resolve circular dependency
# from models.user_auth_log import UserAuthLog
