from pydantic import BaseModel
from typing import Optional, List


# TO support creation and update APIs
class CreateAndUpdateCar(BaseModel):
    carid: int
    buying: str
    maint: str
    doors: str
    persons: str
    lug_boot: str
    safety: str
    decision: str


# TO support list and get APIs
class Car(CreateAndUpdateCar):
    id: int

    class Config:
        orm_mode = True


# To support list cars API
class PaginatedCarInfo(BaseModel):
    limit: int
    offset: int
    data: List[Car]