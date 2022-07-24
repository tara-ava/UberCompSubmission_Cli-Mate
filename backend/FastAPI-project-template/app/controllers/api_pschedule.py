import logging
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from fastapi_sqlalchemy import db

from app.helpers.exception_handler import CustomException
from app.helpers.login_manager import login_required, PermissionRequired
from app.helpers.paging import Page, PaginationParams, paginate
from app.schemas.sche_base import DataResponse
from app.schemas.sche_pschedule import PScheduleItemResponse, PScheduleCreateRequest, PScheduleUpdateRequest
from app.services.srv_pschedule import PScheduleService
from app.models.model_pschedule import PSchedule

logger = logging.getLogger()
router = APIRouter()


#@router.get("", dependencies=[Depends(login_required)], response_model=Page[PScheduleItemResponse])
@router.get("", dependencies=[], response_model=Page[PScheduleItemResponse])
def get(params: PaginationParams = Depends()) -> Any:
    """
    API Get list of Pickup Schedule
    """
    try:
        _query = db.session.query(PSchedule)
        ps = paginate(model=PSchedule, query=_query, params=params)
        return ps
    except Exception as e:
        return HTTPException(status_code=400, detail=logger.error(e))


@router.post("", dependencies=[Depends(PermissionRequired('administrators'))], response_model=DataResponse[PScheduleItemResponse])
def create(ps_data: PScheduleCreateRequest) -> Any:
    """
    API Create Pickup Schedule 
    """
    try:
        test1 = db.session.query(PSchedule).filter(PSchedule.date == ps_data.date).first()
        if test1:
            exist_ps = db.session.query(PSchedule).filter(PSchedule.area == ps_data.area).first()
            if exit_ps:
                raise Exception('Schedule already exists')
        new_ps = PScheduleService().create_ps(ps_data)
        return DataResponse().success_response(data=new_ps)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))


@router.get("/{ps_id}", dependencies=[Depends(login_required)], response_model=DataResponse[PScheduleItemResponse])
def detail(ps_id: int) -> Any:
    """
    API get Pickup Schedule
    """
    try:
        exist_ps = db.session.query(PSchedule).get(ps_id)
        if exist_ps is None:
            raise Exception('No schedule found')
        return DataResponse().success_response(data=exist_ps)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))


