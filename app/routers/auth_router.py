from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.models.interfaces.auth_interface import (
    token_response,
    verify_token_request,
    verify_token_response
)

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

@router.post("/signin", response_model = token_response)
def signin_user(user: user_signin_model):
    access_token = authService.authenticate_user(user)

    return { "access_token": access_token, "token_type": "bearer" }

@router.post("/signup", response_model = user_response_model)
def signup_user(user: user_create_model):
    authService.verify_signup_code(user)
    user.password = authService.get_password_hash(user.password)
    return userService.create_user(user)

@router.post("/verify", response_model=verify_token_response)
def create_veirfy_code(verify_input: verify_token_request):
    token = authService.request_verify_code(verify_input)
    return { "verify_token": token }
