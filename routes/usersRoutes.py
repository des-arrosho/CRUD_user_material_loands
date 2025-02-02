from fastapi import APIRouter,HTTPException, Depends
from sqlalchemy.orm import Session
import crud.users
import config.db
import schemas.users
import models.user

from typing import List

user = APIRouter()

models.user.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@user.get("/user/", response_model=List[schemas.users.user], tags=["Users"])
async def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_users = crud.users.get_users(db = db, skip = skip, limit=limit)
    return db_users

@user.post("/user/{id}", response_model=schemas.users.user, tags=["Usuarios"])
async def read_user(id: int, db: Session = Depends(get_db)):
    db_user= crud.users.get_user(db=db,id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@user.post("/user/", response_model=schemas.users.user, tags=["Users"])
async def create_user(user: schemas.users.userCreate):
    db_user = models.user.User(
        name = user.name,
        lastname = user.lastName,
        typeUser = user.typeUser,
        userName = user.userName,
        email = user.email,
        
    )
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.users.create_user(db=config.db, user=user)
