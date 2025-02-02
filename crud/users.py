import models.user
import schemas.users
from sqlalchemy.orm import Session

def get_users(db: Session, skip: int = 0, limit: int = 0):
    return db.query(models.user.User).offset(skip).limit(limit).all()

def get_user(db: Session, id: int):
    return db.query(models.user.User).filter(models.user.User.id == id).first()