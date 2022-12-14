from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Enum
from Database import Base
import enum


class CarInfo(Base):
    __tablename__ = "cardecision"

    id = Column(Integer, primary_key=True, index=True)
    buying = Column(String)
    maint = Column(String)
    doors = Column(String)
    persons = Column(String)
    lug_boot = Column(String)
    carsafety = Column(String)
    decision = Column(String)
    carid=Column(Integer)