from sqlalchemy import Column, Integer, String, Boolean, DateTime

from app.models.model_base import BareBaseModel


class Waste(BareBaseModel):    
    wtype = Column(String(20))
    weight = Column(Integer)
    date = Column(DateTime)
    available = Column(String(5))
    user = Column(Integer)
    buyer = Column(Integer)

