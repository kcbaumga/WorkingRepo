from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Enum
from .Database import Base
import enum


class CarInfo(Base):
    __tablename__ = "car"

    id = Column(Integer, primary_key=True, index=True)
    carid=Column(Integer)
    buying = Column(String)
    maint = Column(String)
    doors = Column(String)
    persons = Column(String)
    lug_boot = Column(String)
    safety = Column(String)
    decision = Column(String)