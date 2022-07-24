from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr

from app.helpers.enums import UserRole


class UserHhBase(BaseModel):
    name: str
    email: EmailStr
    dob: datetime
    address: str
    mobile: str
    points: int

    class Config:
        orm_mode = True


class UserHhItemResponse(UserHhBase):
    id: int
    name: str
    email: EmailStr
    dob: datetime
    address: str
    mobile: str
    points: int


class UserHhCreateRequest(UserHhBase):
    name: str
    email: EmailStr
    dob: datetime
    address: str
    mobile: str
    points: int

class UserHhUpdateRequest(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    dob: Optional[datetime]
    address: Optional[str]
    mobile: Optional[str]
    points: Optional[int]
