import logging
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from fastapi_sqlalchemy import db

from app.helpers.exception_handler import CustomException
from app.helpers.login_manager import login_required, PermissionRequired
from app.helpers.paging import Page, PaginationParams, paginate
from app.schemas.sche_base import DataResponse
from app.schemas.sche_pbook import PBookItemResponse, PBookCreateRequest, PBookUpdateRequest
from app.services.srv_pbook import PBookService
from app.models.model_pbook import PBook

logger = logging.getLogger()
router = APIRouter()


#@router.get("", dependencies=[Depends(login_required)], response_model=Page[PBookItemResponse])
@router.get("", dependencies=[], response_model=Page[PBookItemResponse])
def get(params: PaginationParams = Depends()) -> Any:
    """
    API Get list of PBook Records
    """
    try:
        _query = db.session.query(PBook)
        book = paginate(model=PBook, query=_query, params=params)
        return book
    except Exception as e:
        return HTTPException(status_code=400, detail=logger.error(e))


#@router.post("", dependencies=[Depends(PermissionRequired('administrators'))], response_model=DataResponse[PBookItemResponse])
@router.post("", dependencies=[], response_model=DataResponse[PBookItemResponse])
def create(b_data: PBookCreateRequest) -> Any:
    """
    API Create PBook Record
    """
    try:
        new_b = PBookService().create_pbook(b_data)
        return DataResponse().success_response(data=new_b)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))


@router.get("/{b_id}", dependencies=[Depends(login_required)], response_model=DataResponse[PBookItemResponse])
def detail(b_id: int) -> Any:
    """
    API get PBook Record
    """
    try:
        exist_b = db.session.query(PBook).get(b_id)
        if exist_b is None:
            raise Exception('No pbook found')
        return DataResponse().success_response(data=exist_b)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))


