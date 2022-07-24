import logging
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from fastapi_sqlalchemy import db

from app.helpers.exception_handler import CustomException
from app.helpers.login_manager import login_required, PermissionRequired
from app.helpers.paging import Page, PaginationParams, paginate
from app.schemas.sche_base import DataResponse
from app.schemas.sche_user import UserItemResponse, UserCreateRequest, UserUpdateMeRequest, UserUpdateRequest
from app.schemas.sche_user_hh import UserHhItemResponse, UserHhCreateRequest, UserHhUpdateRequest
from app.services.srv_user_hh import UserHhService
from app.models.model_user import User
from app.models.model_user_hh import UserHh

logger = logging.getLogger()
router = APIRouter()


#@router.get("", dependencies=[Depends(login_required)], response_model=Page[UserHhItemResponse])
@router.get("", dependencies=[], response_model=Page[UserHhItemResponse])
def get(params: PaginationParams = Depends()) -> Any:
    """
    API Get list Household Users
    """
    try:
        _query = db.session.query(UserHh)
        userhh = paginate(model=UserHh, query=_query, params=params)
        return userhh
    except Exception as e:
        return HTTPException(status_code=400, detail=logger.error(e))


@router.post("", dependencies=[Depends(PermissionRequired('administrators'))], response_model=DataResponse[UserHhItemResponse])
def create(user_data: UserHhCreateRequest) -> Any:
    """
    API Create Household User
    """
    try:
        exist_user = db.session.query(UserHh).filter(UserHh.email == user_data.email).first()
        if exist_user:
            raise Exception('Email already exists')
        new_user = UserHhService().create_user(user_data)
        return DataResponse().success_response(data=new_user)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))


#@router.get("/{user_id}", dependencies=[Depends(login_required)], response_model=DataResponse[UserHhItemResponse])
@router.get("/{user_id}", dependencies=[], response_model=DataResponse[UserHhItemResponse])
def detail(user_id: int) -> Any:
    """
    API get Detail Household User
    """
    try:
        exist_user = db.session.query(UserHh).get(user_id)
        if exist_user is None:
            raise Exception('User already exists')
        return DataResponse().success_response(data=exist_user)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))


@router.put("/{user_id}", dependencies=[Depends(PermissionRequired('administrators'))],
            response_model=DataResponse[UserHhItemResponse])
def update(user_id: int, user_data: UserHhUpdateRequest) -> Any:
    """
    API update Household User
    """
    try:
        exist_user = db.session.query(UserHh).get(user_id)
        if exist_user is None:
            raise Exception('User already exists')
        updated_user = UserHhService().update(user=exist_user, data=user_data)
        return DataResponse().success_response(data=updated_user)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))
