import logging
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from fastapi_sqlalchemy import db

from app.helpers.exception_handler import CustomException
from app.helpers.login_manager import login_required, PermissionRequired
from app.helpers.paging import Page, PaginationParams, paginate
from app.schemas.sche_base import DataResponse
from app.schemas.sche_redeem import RedeemItemResponse, RedeemCreateRequest, RedeemUpdateRequest
from app.services.srv_redeem import RedeemService
from app.models.model_redeem import Redeem

logger = logging.getLogger()
router = APIRouter()


#@router.get("", dependencies=[Depends(login_required)], response_model=Page[RedeemItemResponse])
@router.get("", dependencies=[], response_model=Page[RedeemItemResponse])
def get(params: PaginationParams = Depends()) -> Any:
    """
    API Get list of Redeem Records
    """
    try:
        _query = db.session.query(Redeem)
        rd = paginate(model=Redeem, query=_query, params=params)
        return rd
    except Exception as e:
        return HTTPException(status_code=400, detail=logger.error(e))


#@router.post("", dependencies=[Depends(PermissionRequired('administrators'))], response_model=DataResponse[RedeemItemResponse])
@router.post("", dependencies=[], response_model=DataResponse[RedeemItemResponse])
def create(rd_data: RedeemCreateRequest) -> Any:
    """
    API Create Redeem Record
    """
    try:
        new_rd = RedeemService().create_redeem(rd_data)
        return DataResponse().success_response(data=new_rd)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))


#@router.get("/{rd_id}", dependencies=[Depends(login_required)], response_model=DataResponse[RedeemItemResponse])
@router.get("/{rd_id}", dependencies=[], response_model=DataResponse[RedeemItemResponse])
def detail(rd_id: int) -> Any:
    """
    API get Redeem Record
    """
    try:
        exist_rd = db.session.query(Redeem).get(rd_id)
        if exist_rd is None:
            raise Exception('No redeem found')
        return DataResponse().success_response(data=exist_rd)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))


