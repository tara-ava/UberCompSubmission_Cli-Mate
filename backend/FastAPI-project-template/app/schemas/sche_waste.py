from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr

from app.helpers.enums import WasteType


class WasteBase(BaseModel):
    wtype : str
    weight: int
    date: datetime
    available: str
    user : int
    buyer : int

    class Config:
        orm_mode = True


class WasteItemResponse(WasteBase):
    id: int
    wtype : str
    weight: int
    date: datetime
    available: str
    user : int
    buyer : int


class WasteCreateRequest(WasteBase):
    date: datetime
    area: str
    capacity: int


class WasteUpdateRequest(WasteBase):
    wtype : Optional[str]
    weight: Optional[int]
    date: Optional[datetime]
    available: Optional[str]
    user : Optional[int]
    buyer : Optional[int]
