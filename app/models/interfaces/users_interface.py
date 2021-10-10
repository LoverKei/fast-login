from typing import Optional
from pydantic import BaseModel

class user_create_model(BaseModel):
    email: str
    nickname: str
    password: str
    name: str
    phone: str

class user_response_model(BaseModel):
    id: str
    email: str
    nickname: str
    name: str
    phone: str

class user_signin_model(BaseModel):
    id: str
    password: str
