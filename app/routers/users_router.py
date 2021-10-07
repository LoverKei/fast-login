from fastapi import APIRouter

from app.services.users_service import (
    hello_user,
    get_user_by_id,
    create_user
)
from app.models.interfaces.users_interface import (
    user_create_model,
    user_response_model
)

router = APIRouter()

@router.get("")
def helloUser ():
    return hello_user()

@router.get("/{userId}", response_model = user_response_model)
def getUser(userId: str):
    return get_user_by_id(userId)

@router.post("", response_model = user_response_model)
def getUser(user: user_create_model):
    return create_user(user)
