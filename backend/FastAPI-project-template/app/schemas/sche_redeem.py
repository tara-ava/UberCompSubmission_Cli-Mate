from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class RedeemBase(BaseModel):
    user: int
    reward: int
    used : str
    expiry: datetime

    class Config:
        orm_mode = True


class RedeemItemResponse(RedeemBase):
    id: int
    user: int
    reward: int
    used : str
    expiry: datetime


class RedeemCreateRequest(RedeemBase):
    user: int
    reward: int
    used : str
    expiry: datetime


class RedeemUpdateRequest(RedeemBase):
    user: Optional[int]
    reward: Optional[int]
    used : Optional[str]
    expiry: Optional[datetime]
