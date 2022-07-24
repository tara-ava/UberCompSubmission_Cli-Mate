import jwt

from typing import Optional
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from fastapi_sqlalchemy import db
from pydantic import ValidationError
from starlette import status

from app.models.model_redeem import Redeem
from app.core.config import settings
from app.core.security import verify_password, get_password_hash
from app.schemas.sche_token import TokenPayload
from app.schemas.sche_redeem import RedeemCreateRequest, RedeemUpdateRequest 



class RedeemService(object):
    __instance = None

    reusable_oauth2 = HTTPBearer(
        scheme_name='Authorization'
    )

    @staticmethod
    def create_redeem(data: RedeemCreateRequest):
        new_r  = Redeem(
            user=data.user,
            reward=data.reward,
            used='N',
            expiry=data.expiry,
        )
        db.session.add(new_r)
        db.session.commit()
        return new_r

    @staticmethod
    def update(red: Redeem, data: RedeemUpdateRequest):
        print(f'data: {data.__dict__}')
        red.user = red.user if data.user is None else data.user
        red.reward = red.reward if data.reward is None else data.reward
        red.used = red.used if data.used is None else data.used
        red.expiry = red.expiry if data.expiry is None else data.expiry
        db.session.commit()
        return rew
