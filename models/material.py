from sqlalchemy import Column, Integer, String, DateTime, Enum
from config.db import Base
import enum

class Status(str, enum.Enum):
    Available = "Available"
    Borrowed = "Borrowed"
    maitenance = "maitenance"
    

class Material(Base):
    __tablename__="tbb_material"

    id = Column(Integer, primary_key=True, autoincrement=True)
    type_material = Column(String(60))
    brand = Column(String(60))
    model = Column(String(60))
    status = Column(Enum(Status))
    registrationDate = Column(DateTime)
    updateDate = Column(DateTime)
    