from fastapi import HTTPException
from app.models.users_repository import (
    find_user_by_id,
    add_user
)
from app.models.interfaces.users_interface import user_create_model

def hello_user() -> str:
    return "hello, user!!!"

def get_user_by_id(id: str):
    user = find_user_by_id(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def create_user(user: user_create_model):
    return add_user(user)
