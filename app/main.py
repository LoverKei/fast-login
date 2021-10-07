from fastapi import FastAPI

from app.core.config import API_PREFIX
from app.routers.api import router as api

app = FastAPI()

app.include_router(api, prefix=API_PREFIX)

@app.get("/")
def read_root():
    return { "msg": "hello, world!!!" }
