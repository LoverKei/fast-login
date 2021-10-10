from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.models.interfaces.users_interface import (
    user_create_model,
    user_response_model,
    user_signin_model
)
from app.services.auth_service import AuthService
from app.services.users_service import UserService

router = APIRouter()
authService = AuthService()
userService = UserService()

class token_response(BaseModel):
    access_token: str
    token_type: str

@router.post("/signin", response_model = token_response)
def signin_user(user: user_signin_model):
    access_token = authService.authenticate_user(user)

    return { "access_token": access_token, "token_type": "bearer" }

@router.post("/signup", response_model = user_response_model)
def signup_user(user: user_create_model):
    user.password = authService.get_password_hash(user.password)
    return userService.create_user(user)
