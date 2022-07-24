from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class PBookBase(BaseModel):
    user: int
    pickup : int

    class Config:
        orm_mode = True


class PBookItemResponse(PBookBase):
    id: int
    user: int
    pickup : int



class PBookCreateRequest(PBookBase):
    user: int
    pickup : int



class PBookUpdateRequest(PBookBase):
    user: Optional[int]
    pickup : Optional[int]
