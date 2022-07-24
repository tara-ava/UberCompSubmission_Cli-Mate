import jwt

from typing import Optional
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from fastapi_sqlalchemy import db
from pydantic import ValidationError
from starlette import status

from app.models.model_waste import Waste
from app.core.config import settings
from app.core.security import verify_password, get_password_hash
from app.schemas.sche_token import TokenPayload
from app.schemas.sche_waste import WasteCreateRequest, WasteUpdateRequest 



class WasteService(object):
    __instance = None

    reusable_oauth2 = HTTPBearer(
        scheme_name='Authorization'
    )

    @staticmethod
    def create_waste(data: WasteCreateRequest):
        newaste  = PSchedule(
            wtype=data.wtype,
            weight=data.weight,
            date=data.date,
            available='Y',
            user = data.user,
            buyer = 0,
        )
        db.session.add(newaste)
        db.session.commit()
        return newaste

    @staticmethod
    def update(w: Waste, data: WasteUpdateRequest):
        print(f'data: {data.__dict__}')
        w.wtype = w.wtype if data.wtype is None else data.wtype
        w.weight = w.weight if data.weight is None else data.weight
        w.date = w.date if data.date is None else data.date
        w.available = w.available if data.available is None else data.available
        w.user = w.user if data.user is None else data.user
        w.buyer = w.buyer if data.buyer is None else data.buyer
        db.session.commit()
        return ps
