import jwt

from typing import Optional
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from fastapi_sqlalchemy import db
from pydantic import ValidationError
from starlette import status

from app.models.model_pbook import PBook
from app.core.config import settings
from app.core.security import verify_password, get_password_hash
from app.schemas.sche_token import TokenPayload
from app.schemas.sche_pbook import PBookCreateRequest, PBookUpdateRequest 



class PBookService(object):
    __instance = None

    reusable_oauth2 = HTTPBearer(
        scheme_name='Authorization'
    )

    @staticmethod
    def create_pbook(data: PBookCreateRequest):
        new_b  = PBook(
            user=data.user,
            pickup = data.pickup,
        )
        db.session.add(new_b)
        db.session.commit()
        return new_b

    @staticmethod
    def update(book: PBook, data: PBookUpdateRequest):
        print(f'data: {data.__dict__}')
        book.user = book.user if data.user is None else data.user
        book.pickup = book.pickup if data.pickup is None else data.pickup
        db.session.commit()
        return book
