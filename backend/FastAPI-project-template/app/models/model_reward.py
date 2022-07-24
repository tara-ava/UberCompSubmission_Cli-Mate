from sqlalchemy import Column, Integer, String, Boolean, DateTime

from app.models.model_base import BareBaseModel


class Reward(BareBaseModel):    
    points = Column(Integer)
    active = Column(String(5))
    partner = Column(Integer)
    since = Column(DateTime)
    desc = Column(String(120))

