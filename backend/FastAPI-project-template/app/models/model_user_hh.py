from sqlalchemy import Column, String, Integer, Boolean, DateTime

from app.models.model_base import BareBaseModel


class UserHh(BareBaseModel):    
    name = Column(String(60))
    email = Column(String(60), unique=True)
    dob = Column(DateTime)
    address = Column(String(100))
    mobile = Column(String(20))
    points = Column(Integer)
