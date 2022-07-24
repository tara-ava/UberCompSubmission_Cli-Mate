from sqlalchemy import Column, Integer, String, Boolean, DateTime

from app.models.model_base import BareBaseModel


class Redeem(BareBaseModel):    
    user = Column(Integer)
    reward = Column(Integer)
    used = Column(String(5))
    expiry = Column(DateTime)

