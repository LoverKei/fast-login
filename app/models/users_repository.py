from bson.objectid import ObjectId
from app.core.mongodb import get_db

users = get_db()["users"]

def find_user_by_id(id: str):
    return users.find_one({ "_id": ObjectId(id) }, { "_id": 0 })

def find_users():
    return users.find()

def insert_user(user):
    result = users.insert_one(user)
    return { "id": str(result.inserted_id) }
