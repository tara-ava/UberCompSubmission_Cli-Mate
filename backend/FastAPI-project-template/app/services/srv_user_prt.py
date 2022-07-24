import jwt

from typing import Optional
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from fastapi_sqlalchemy import db
from pydantic import ValidationError
from starlette import status

from app.models.model_user_prt import UserPrt
from app.core.config import settings
from app.core.security import verify_password, get_password_hash
from app.schemas.sche_token import TokenPayload
from app.schemas.sche_user_prt import UserPrtCreateRequest, UserPrtUpdateRequest 



class UserPrtService(object):
    __instance = None

    reusable_oauth2 = HTTPBearer(
        scheme_name='Authorization'
    )

    @staticmethod
    def create_user(data: UserPrtCreateRequest):
        new_user = UserPrt(
            company=data.company,
            email=data.email,
            address=data.address,
            phone=data.phone,
            mobile=data.mobile,
            tax_num=data.tax_num,
            bank_acc=data.bank_acc,
            ptype=data.ptype,
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def update(user: UserPrt, data: UserPrtUpdateRequest):
        print(f'data: {data.__dict__}')
        user.company = user.company if data.company is None else data.company
        user.email = user.email if data.email is None else data.email
        user.address = user.address if data.address is None else data.address
        user.phone = user.phone if data.phone is None else data.phone
        user.mobile = user.mobile if data.mobile is None else data.mobile
        user.tax_num = user.tax_num if data.tax_num is None else data.tax_num
        user.bank_acc = user.bank_acc if data.bank_acc is None else data.bank_acc
        user.ptype = user.ptype if data.ptype is None else data.ptype
        db.session.commit()
        return user
