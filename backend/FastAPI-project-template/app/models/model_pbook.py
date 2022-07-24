from sqlalchemy import Column, Integer, String, Boolean, DateTime

from app.models.model_base import BareBaseModel


class PBook(BareBaseModel):    
    user = Column(Integer)
    pickup = Column(Integer)
