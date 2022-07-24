from sqlalchemy import Column, Integer, String, Boolean, DateTime

from app.models.model_base import BareBaseModel


class PSchedule(BareBaseModel):    
    date = Column(DateTime)
    area = Column(String(50))
    capacity = Column(Integer)
