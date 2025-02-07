from typing import List, Union, Optional
from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class loandsBase(BaseModel):
    id_usuario: int
    id_material: int
    fecha_prestamo: datetime
    fecha_devolucion: Optional[datetime] = None
    loand_status: str
    registrationDate: datetime
    updateDate: datetime

class loandsCreate(loandsBase):
    pass
class loandsUpdate(loandsBase):
    pass
class loands(loandsBase):
    id: int
    class config:
        orm_mode = True