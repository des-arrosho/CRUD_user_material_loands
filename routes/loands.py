from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.loands
import config.db
import schemas.loands
import models.loand

from typing import List

loands_router = APIRouter()

models.loand.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        print("Conectando a la base de datos...")
        yield db
    finally:
        db.close()
        print("Conexión cerrada.")


@loands_router.get("/loands/", response_model=List[schemas.loands.loands], tags=["Loands"])
async def read_loands(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_loands = crud.loands.get_loands(db=db, skip=skip, limit=limit)
    return db_loands

@loands_router.get("/loands/{id}", response_model=schemas.loands.loands, tags=["Loands"])
async def read_loands(id: int, db: Session = Depends(get_db)):
    db_loand = crud.loands.get_loands(db=db, id=id)
    if db_loand is None:
        raise HTTPException(status_code=404, detail="Loand not found")
    return db_loand

@loands_router.post("/loands/", response_model=schemas.loands.loands, tags=["Loands"])
async def create_loand(loand: schemas.loands.loandsCreate, db: Session = Depends(get_db)):
    new_loand = crud.loands.create_loand(db, loand)
    return new_loand

@loands_router.put("/loands/{id}", response_model=schemas.loands.loands, tags=["Loands"])
async def update_loand(id: int, loand_update: schemas.loands.loandsUpdate, db: Session = Depends(get_db)):
    db_loand = crud.loands.update_loand(db, id, loand_update)
    if db_loand is None:
        raise HTTPException(status_code=404, detail="Loand not found")
    return db_loand

@loands_router.delete("/loands/{id}", response_model=schemas.loands.loands, tags=["Loands"])
async def delete_loand(id: int, db: Session = Depends(get_db)):
    db_loand = crud.loands.delete_loand(db, id)
    if db_loand is None:
        raise HTTPException(status_code=404, detail="Loand not found")
    return db_loand
