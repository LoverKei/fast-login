from fastapi import APIRouter

from app.services.users_service import UserService
from app.models.interfaces.users_interface import (
    user_create_model,
    user_response_model
)

router = APIRouter()
userService = UserService()

@router.get("")
def helloUser ():
    return userService.hello_user()

@router.get("/{userId}", response_model = user_response_model)
def getUser(userId: str):
    return userService.get_user_by_id(userId)

@router.post("", response_model = user_response_model)
def getUser(user: user_create_model):
    return userService.create_user(user)
