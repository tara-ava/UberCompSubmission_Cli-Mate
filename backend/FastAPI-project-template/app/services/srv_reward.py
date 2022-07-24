import jwt

from typing import Optional
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from fastapi_sqlalchemy import db
from pydantic import ValidationError
from starlette import status

from app.models.model_reward import Reward
from app.core.config import settings
from app.core.security import verify_password, get_password_hash
from app.schemas.sche_token import TokenPayload
from app.schemas.sche_reward import RewardCreateRequest, RewardUpdateRequest 



class RewardService(object):
    __instance = None

    reusable_oauth2 = HTTPBearer(
        scheme_name='Authorization'
    )

    @staticmethod
    def create_reward(data: RewardCreateRequest):
        new_r  = Reward(
            points=data.points,
            active='Y',
            partner=data.partner,
            since=data.since,
            desc = data.desc,
        )
        db.session.add(new_r)
        db.session.commit()
        return new_r

    @staticmethod
    def update(rew: Reward, data: RewardUpdateRequest):
        print(f'data: {data.__dict__}')
        rew.points = rew.points if data.points is None else data.points
        rew.active = rew.active if data.active is None else data.active
        rew.partner = rew.partner if data.partner is None else data.partner
        rew.since = rew.since if data.since is None else data.since
        rew.desc = rew.desc if data.desc is None else data.desc
        db.session.commit()
        return rew
