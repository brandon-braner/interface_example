# fastapi router

from fastapi import APIRouter
from fastapi import Depends
from app.modules.user.service.user_interface import UserInterface
from app.modules.user.service.tqa_user_service import TQAUserService
from app.modules.user.service.hat_trick_user_service import HatTrickUserService
router = APIRouter()


def get_user_service() -> UserInterface:
    # return HatTrickUserService()
    return TQAUserService()

@router.get("/")
def user(user_service: UserInterface = Depends(get_user_service)):
    return user_service.get_users()

@router.get("/{user_id}")
def user(user_id: int, user_service: UserInterface = Depends(get_user_service)):
    return user_service.get_user(user_id)