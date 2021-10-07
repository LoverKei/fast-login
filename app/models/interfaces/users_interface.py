from typing import Optional
from pydantic import BaseModel
from bson import ObjectId

from app.models.py_objectid import PyObjectId

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