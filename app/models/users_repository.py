from bson.objectid import ObjectId

from app.core.mongodb import get_db
from app.models.interfaces.users_interface import user_create_model
from app.models.py_objectid import convert_id

users = get_db()["users"]

def find_user_by_id(id: str):
    result = users.find_one({ "_id": ObjectId(id) })

    return convert_id(result)

def add_user(user: user_create_model):
    result = users.insert_one(user.dict())
    new_user = find_user_by_id(result.inserted_id)

    return new_user
