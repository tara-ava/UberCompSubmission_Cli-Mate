from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr

from app.helpers.enums import UserRole


class PScheduleBase(BaseModel):
    date: datetime
    area: str
    capacity: int

    class Config:
        orm_mode = True


class PScheduleItemResponse(PScheduleBase):
    id: int
    date: datetime
    area: str
    capacity: int


class PScheduleCreateRequest(PScheduleBase):
    date: datetime
    area: str
    capacity: int


class PScheduleUpdateRequest(PScheduleBase):
    date: Optional[datetime]
    area: Optional[str]
    capacity: Optional[int]
