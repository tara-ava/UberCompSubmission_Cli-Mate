import jwt

from typing import Optional
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from fastapi_sqlalchemy import db
from pydantic import ValidationError
from starlette import status

from app.models.model_pschedule import PSchedule
from app.core.config import settings
from app.core.security import verify_password, get_password_hash
from app.schemas.sche_token import TokenPayload
from app.schemas.sche_pschedule import PScheduleCreateRequest, PScheduleUpdateRequest 



class PScheduleService(object):
    __instance = None

    reusable_oauth2 = HTTPBearer(
        scheme_name='Authorization'
    )

    @staticmethod
    def create_ps(data: PScheduleCreateRequest):
        newps  = PSchedule(
            date=data.date,
            area=data.area,
            capacity=data.capacity,
        )
        db.session.add(newps)
        db.session.commit()
        return newps

    @staticmethod
    def update(ps: PSchedule, data: PScheduleUpdateRequest):
        print(f'data: {data.__dict__}')
        ps.date = ps.date if data.date is None else data.date
        ps.area = ps.area if data.area is None else data.area
        ps.capacity = ps.capacity if data.capacity is None else data.capacity
        db.session.commit()
        return ps
