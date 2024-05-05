import pdb

from passlib.context import CryptContext
from datetime import datetime, timedelta
from fastapi import HTTPException
import jwt
from sqlalchemy.orm import Session
from models.models import User
from sqlalchemy import select

# from .database import get_db

ACCESS_TOKEN_EXPIRES_MINUTES = 60

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def get_hashed_password(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    print("success ")
    print(plain_password)
    print(hashed_password)
    return pwd_context.verify(plain_password, hashed_password)


def authenticate_user(email: str, password: str, db: Session):
    print("hit here")
    # pdb.set_trace()
    # user = db.query(User).filter(User.Email == email).first()
    user = select(User).where(User.Email==email)
    result = db.execute(user)
    for user_obj in result.scalars():
        print(user_obj)

    if not user or not verify_password(get_hashed_password(password), user.Password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, "HUAWEISTC", algorithm="HS256")
    return encoded_jwt


def login(email: str, password: str, db: Session):
    # pdb.set_trace()
    user = authenticate_user(email, password, db)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRES_MINUTES)
    access_token = create_access_token(
        data={"sub": user.Email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
