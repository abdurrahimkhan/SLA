from sqlalchemy import Column, Integer, ForeignKey, DateTime, String, func
from sqlalchemy.orm import relationship
from database.database import Base


class UserAuthLog(Base):
    __tablename__ = "user_auth_logs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String)
    name = Column(String)
    login_time = Column(DateTime, default=func.now())
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="auth_logs")
