from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

import crud.material
import config.db
import schemas.materials
import models.material

models.material.Base.metadata.create_all(bind=config.db.engine)

material_router = APIRouter()

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@material_router.get("/materials/", response_model=List[schemas.materials.material], tags=["Materials"])
async def read_materials(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.material.get_materials(db=db, skip=skip, limit=limit)


@material_router.get("/materials/{id}", response_model=schemas.materials.material, tags=["Materials"])
async def read_material(id: int, db: Session = Depends(get_db)):
    db_material = crud.material.get_material(db=db, id=id)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return db_material

@material_router.post("/materials/", response_model=schemas.materials.material, tags=["Materials"])
async def create_material(material: schemas.materials.materialCreate, db: Session = Depends(get_db)):
    return crud.material.create_material(db, material)

@material_router.put("/materials/{id}", response_model=schemas.materials.material, tags=["Materials"])
async def update_material(id: int, material_update: schemas.materials.materialUpdate, db: Session = Depends(get_db)):
    db_material = crud.material.update_material(db, id, material_update)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return db_material

@material_router.delete("/materials/{id}", response_model=schemas.materials.material, tags=["Materials"])
async def delete_material(id: int, db: Session = Depends(get_db)):
    db_material = crud.material.delete_material(db, id)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return db_material
