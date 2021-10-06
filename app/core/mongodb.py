from pymongo import MongoClient
from app.core.config import (
    MONGODB_NAME,
    MONGODB_URL
)
client = MongoClient(MONGODB_URL)
db = client[MONGODB_NAME]

def get_db():  
    return db
