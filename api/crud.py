import pdb

from sqlalchemy.orm import Session
from models.models import User


def get_all_users(db: Session):
    # pdb.set_trace()
    users = db.query(User).all()
    user_jsons = [user.to_json() for user in users]
    return user_jsons
    # return db.query(User).all()


def get_current_users(email, db: Session):
    # pdb.set_trace()
    user = db.query(User).filter(User.Email == email).first()
    return user
