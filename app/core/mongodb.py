from pymongo import MongoClient
from app.core.config import (
    MONGODB_NAME,
    MONGODB_URL
)
client = MongoClient(MONGODB_URL)
db = client[MONGODB_NAME]

def init_index():
    db.users.create_index([('email', -1)], name='_email_', unique=True)
    db.users.create_index([('phone', -1)], name='_phone_', unique=True)

def get_db():  
    return db

init_index()