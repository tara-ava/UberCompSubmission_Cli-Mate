import jwt

from typing import Optional
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from fastapi_sqlalchemy import db
from pydantic import ValidationError
from starlette import status

from app.models.model_user_hh import UserHh
from app.core.config import settings
from app.core.security import verify_password, get_password_hash
from app.schemas.sche_token import TokenPayload
from app.schemas.sche_user_hh import UserHhCreateRequest, UserHhUpdateRequest 



class UserHhService(object):
    __instance = None

    reusable_oauth2 = HTTPBearer(
        scheme_name='Authorization'
    )

    @staticmethod
    def create_user(data: UserHhCreateRequest):
        new_user = UserHh(
            name=data.name,
            email=data.email,
            dob=data.dob,
            address=data.address,
            mobile=data.mobile,
            points=data.points,
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def update(user: UserHh, data: UserHhUpdateRequest):
        print(f'data: {data.__dict__}')
        user.name = user.name if data.name is None else data.name
        user.email = user.email if data.email is None else data.email
        user.dob = user.dob if data.dob is None else data.dob
        user.address = user.address if data.address is None else data.address
        user.mobile = user.mobile if data.mobile is None else data.mobile
        user.points = user.points if data.points is None else data.points
        db.session.commit()
        return user
