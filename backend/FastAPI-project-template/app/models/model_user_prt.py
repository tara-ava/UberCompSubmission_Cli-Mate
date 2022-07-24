from sqlalchemy import Column, String, Integer, Boolean, DateTime

from app.models.model_base import BareBaseModel


class UserPrt(BareBaseModel):    
    company = Column(String(60))
    email = Column(String(60), unique=True)
    address = Column(String(100))
    phone = Column(String(20))
    mobile = Column(String(20))
    tax_num = Column(String(20))
    bank_acc = Column(String(20))
    ptype = Column(String(5))
