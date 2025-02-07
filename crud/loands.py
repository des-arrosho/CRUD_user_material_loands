from sqlalchemy.orm import Session
from models.loand import Loands
import schemas.loands

def get_loands(db: Session, skip: int = 0, limit: int = None):
    query = db.query(Loands).offset(skip)
    if limit:
        query = query.limit(limit)
    return query.all()

def get_loand(db: Session, id: int):
    return db.query(Loands).filter(Loands.id == id).first()


def create_loand(db: Session, loand_data: schemas.loands.loandsCreate):
        new_loand = Loands(
            id_usuario=loand_data.id_usuario,
            id_material=loand_data.id_material,
            fecha_prestamo=loand_data.fecha_prestamo,
            fecha_devolucion=loand_data.fecha_devolucion,
            loand_status=loand_data.loand_status,
            registrationDate=loand_data.registrationDate,
            updateDate=loand_data.updateDate
        )
        db.add(new_loand)
        db.commit()
        db.refresh(new_loand)
        return new_loand

def update_loand(db: Session, id: int, loand_data: schemas.loands.loandsUpdate):
    db_loan = db.query(Loands).filter(Loands.id == id).first()
    if not db_loan:
        return None

    for key, value in loand_data.dict(exclude_unset=True).items():
        setattr(db_loan, key, value)

    db.commit()
    db.refresh(db_loan)
    return db_loan

def delete_loand(db: Session, id: int):
    db_loan = db.query(Loands).filter(Loands.id == id).first()
    if not db_loan:
        return None

    db.delete(db_loan)
    db.commit()
    return db_loan
