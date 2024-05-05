from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from database.database import Base


class Permission(Base):
    __tablename__ = "permissions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    domains = Column(String, default="")
    region = Column(String, default="")
    type = Column(String, default="Contractor Region User")
    createdAt = Column(DateTime, default=func.now())
    updatedAt = Column(DateTime, default=func.now(), onupdate=func.now())

    users = relationship("User", back_populates="permission")
