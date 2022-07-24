from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr

from app.helpers.enums import UserRole


class UserPrtBase(BaseModel):
    company: str
    email: EmailStr
    address: str
    phone: str
    mobile: str
    tax_num: str
    bank_acc: str
    ptype: str

    class Config:
        orm_mode = True


class UserPrtItemResponse(UserPrtBase):
    id: int
    company: str
    email: EmailStr
    address: str
    phone: str
    mobile: str
    tax_num: str
    bank_acc: str
    ptype: str

class UserPrtCreateRequest(UserPrtBase):
    company: str
    email: EmailStr
    address: str
    phone: str
    mobile: str
    tax_num: str
    bank_acc: str
    ptype: str

class UserPrtUpdateRequest(BaseModel):
    company: Optional[str]
    email: Optional[EmailStr]
    address: Optional[str]
    phone: Optional[str]
    mobile: Optional[str]
    tax_num: Optional[str]
    bank_acc: Optional[str]
    ptype: Optional[str]
