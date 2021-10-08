import traceback
from fastapi import FastAPI

from app.core.config import API_PREFIX
from app.routers.api import router as api
from app.core.mongodb import MongoDB
from app.core.redis import Redis

app = FastAPI()

app.include_router(api, prefix=API_PREFIX)

def init_service():
    # MongoDB
    try:
        db = MongoDB()
        db.get_client()
        print("MongoDB init success.")
    except Exception:
        traceback.print_exc()
        print("MongoDB init failed. ", type(Exception), Exception)

    # Redis
    try:
        redis = Redis()
        redis.get_client()
        print("Redis init success.")
    except Exception:
        traceback.print_exc()
        print("Redis init failed. ")


@app.get("/")
def read_root():
    return { "msg": "hello, world!!!" }

init_service()
