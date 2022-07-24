from fastapi import APIRouter

from app.controllers import api_user, api_login, api_register, api_user_hh, api_user_prt, api_pschedule, api_waste, api_reward, api_redeem, api_pbook

router = APIRouter()

router.include_router(api_login.router, tags=["login"], prefix="/login")

router.include_router(api_register.router, tags=["register"], prefix="/register")

router.include_router(api_user.router, tags=["user"], prefix="/users")

router.include_router(api_user_hh.router, tags=["user_hh"], prefix="/users_hh")

router.include_router(api_user_prt.router, tags=["user_prt"], prefix="/users_prt")

router.include_router(api_pschedule.router, tags=["pschedule"], prefix="/pschedule")

router.include_router(api_waste.router, tags=["waste"], prefix="/waste")

router.include_router(api_reward.router, tags=["reward"], prefix="/reward")

router.include_router(api_redeem.router, tags=["redeem"], prefix="/redeem")

router.include_router(api_pbook.router, tags=["pbook"], prefix="/pbook")
