import logging
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from fastapi_sqlalchemy import db

from app.helpers.exception_handler import CustomException
from app.helpers.login_manager import login_required, PermissionRequired
from app.helpers.paging import Page, PaginationParams, paginate
from app.schemas.sche_base import DataResponse
from app.schemas.sche_waste import WasteItemResponse, WasteCreateRequest, WasteUpdateRequest
from app.services.srv_waste import WasteService
from app.models.model_waste import Waste

logger = logging.getLogger()
router = APIRouter()


#@router.get("", dependencies=[Depends(login_required)], response_model=Page[WasteItemResponse])
@router.get("", dependencies=[], response_model=Page[WasteItemResponse])
def get(params: PaginationParams = Depends()) -> Any:
    """
    API Get list of Waste Records
    """
    try:
        _query = db.session.query(Waste)
        w = paginate(model=Waste, query=_query, params=params)
        return w
    except Exception as e:
        return HTTPException(status_code=400, detail=logger.error(e))


@router.post("", dependencies=[Depends(PermissionRequired('administrators'))], response_model=DataResponse[WasteItemResponse])
def create(w_data: WasteCreateRequest) -> Any:
    """
    API Create Waste Record
    """
    try:
        newaste = WasteService().create_waste(w_data)
        return DataResponse().success_response(data=newaste)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))


@router.get("/{w_id}", dependencies=[Depends(login_required)], response_model=DataResponse[WasteItemResponse])
def detail(w_id: int) -> Any:
    """
    API get Waste Record
    """
    try:
        exist_w = db.session.query(Waste).get(w_id)
        if exist_w is None:
            raise Exception('No waste found')
        return DataResponse().success_response(data=exist_w)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))


