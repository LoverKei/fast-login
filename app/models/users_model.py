from pydantic import BaseModel
from bson import ObjectId

class User(BaseModel):
    _id: ObjectId
    email: str
    nickname: str
    password: str
    name: str
    phone: str
