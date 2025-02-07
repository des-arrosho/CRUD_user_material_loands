from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey
from config.db import Base
import enum

class StatusLoands(str, enum.Enum):
    Assent = "Assent"
    Idle = "Idle"
    Defeanted = "Defeanted"
    

class Loands(Base):
    __tablename__="tbb_loands"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey("tbb_users.id"))
    id_material = Column(Integer, ForeignKey("tbb_material.id"))
    fecha_prestamo = Column(DateTime)
    fecha_devolucion = Column(DateTime, nullable=True)
    loand_status = Column(Enum(StatusLoands))
    registrationDate = Column(DateTime)
    updateDate = Column(DateTime)