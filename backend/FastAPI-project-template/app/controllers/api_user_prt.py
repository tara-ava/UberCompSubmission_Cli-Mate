import logging
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from fastapi_sqlalchemy import db

from app.helpers.exception_handler import CustomException
from app.helpers.login_manager import login_required, PermissionRequired
from app.helpers.paging import Page, PaginationParams, paginate
from app.schemas.sche_base import DataResponse
from app.schemas.sche_user import UserItemResponse, UserCreateRequest, UserUpdateMeRequest, UserUpdateRequest
from app.schemas.sche_user_prt import UserPrtItemResponse, UserPrtCreateRequest, UserPrtUpdateRequest
from app.services.srv_user_prt import UserPrtService
from app.models.model_user import User
from app.models.model_user_prt import UserPrt

logger = logging.getLogger()
router = APIRouter()


#@router.get("", dependencies=[Depends(login_required)], response_model=Page[UserPrtItemResponse])
@router.get("", dependencies=[], response_model=Page[UserPrtItemResponse])
def get(params: PaginationParams = Depends()) -> Any:
    """
    API Get list User Partner RC/RW
    """
    try:
        _query = db.session.query(UserPrt)
        userprt = paginate(model=UserPrt, query=_query, params=params)
        return userprt
    except Exception as e:
        return HTTPException(status_code=400, detail=logger.error(e))


@router.post("", dependencies=[Depends(PermissionRequired('administrators'))], response_model=DataResponse[UserPrtItemResponse])
def create(user_data: UserPrtCreateRequest) -> Any:
    """
    API Create Partner User
    """
    try:
        exist_user = db.session.query(UserPrt).filter(UserPrt.email == user_data.email).first()
        if exist_user:
            raise Exception('Email already exists')
        new_user = UserPrtService().create_user(user_data)
        return DataResponse().success_response(data=new_user)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))


#@router.get("/{user_id}", dependencies=[Depends(login_required)], response_model=DataResponse[UserPrtItemResponse])
@router.get("/{user_id}", dependencies=[], response_model=DataResponse[UserPrtItemResponse])
def detail(user_id: int) -> Any:
    """
    API get Detail User
    """
    try:
        exist_user = db.session.query(UserPrt).get(user_id)
        if exist_user is None:
            raise Exception('User already exists')
        return DataResponse().success_response(data=exist_user)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))


@router.put("/{user_id}", dependencies=[Depends(PermissionRequired('administrators'))],
            response_model=DataResponse[UserPrtItemResponse])
def update(user_id: int, user_data: UserPrtUpdateRequest) -> Any:
    """
    API update User
    """
    try:
        exist_user = db.session.query(UserPrt).get(user_id)
        if exist_user is None:
            raise Exception('User already exists')
        updated_user = UserPrtService().update(user=exist_user, data=user_data)
        return DataResponse().success_response(data=updated_user)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))
