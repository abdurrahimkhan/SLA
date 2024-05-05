# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from app.database import SessionLocal
# from app import crud, schemas
#
# router = APIRouter()
#
#
# # Dependency to get the database session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# @router.get("/users/", response_model=list[schemas.User])
# def get_all_users(db: Session = Depends(get_db)):
#     users = crud.get_all_users(db)
#     return users
