from typing import List, Union, Optional
from pydantic import BaseModel
from datetime import datetime

class materialBase(BaseModel):
    type_material: str
    brand: str
    model: str
    status: str
    registrationDate: datetime
    updateDate: datetime

class materialCreate(materialBase):
    pass
class materialUpdate(materialBase):
    pass
class material(materialBase):
    id: int
    class config:
        orm_mode = True
