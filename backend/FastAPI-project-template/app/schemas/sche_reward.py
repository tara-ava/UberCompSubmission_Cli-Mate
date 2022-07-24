from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class RewardBase(BaseModel):
    points: int
    active : str
    partner : int
    since: datetime
    desc: str

    class Config:
        orm_mode = True


class RewardItemResponse(RewardBase):
    id: int
    points: int
    active : str
    partner : int
    since: datetime
    desc: str


class RewardCreateRequest(RewardBase):
    points: int
    active : str
    partner : int
    since: datetime
    desc: str


class RewardUpdateRequest(RewardBase):
    points: Optional[int]
    active : Optional[str]
    partner : Optional[int]
    since: Optional[datetime]
    desc: Optional[str]
