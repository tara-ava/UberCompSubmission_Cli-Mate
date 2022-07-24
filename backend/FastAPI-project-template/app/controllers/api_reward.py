import logging
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from fastapi_sqlalchemy import db

from app.helpers.exception_handler import CustomException
from app.helpers.login_manager import login_required, PermissionRequired
from app.helpers.paging import Page, PaginationParams, paginate
from app.schemas.sche_base import DataResponse
from app.schemas.sche_reward import RewardItemResponse, RewardCreateRequest, RewardUpdateRequest
from app.services.srv_reward import RewardService
from app.models.model_reward import Reward

logger = logging.getLogger()
router = APIRouter()


#@router.get("", dependencies=[Depends(login_required)], response_model=Page[RewardItemResponse])
@router.get("", dependencies=[], response_model=Page[RewardItemResponse])
def get(params: PaginationParams = Depends()) -> Any:
    """
    API Get list of Reward Records
    """
    try:
        _query = db.session.query(Reward)
        rw = paginate(model=Reward, query=_query, params=params)
        return rw
    except Exception as e:
        return HTTPException(status_code=400, detail=logger.error(e))


@router.post("", dependencies=[Depends(PermissionRequired('administrators'))], response_model=DataResponse[RewardItemResponse])
def create(rw_data: RewardCreateRequest) -> Any:
    """
    API Create Reward Record
    """
    try:
        new_rw = RewardService().create_reward(rw_data)
        return DataResponse().success_response(data=new_rw)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))


@router.get("/{rw_id}", dependencies=[Depends(login_required)], response_model=DataResponse[RewardItemResponse])
def detail(rw_id: int) -> Any:
    """
    API get Reward Record
    """
    try:
        exist_rw = db.session.query(Reward).get(rw_id)
        if exist_rw is None:
            raise Exception('No reward found')
        return DataResponse().success_response(data=exist_rw)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))


