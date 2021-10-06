from fastapi import FastAPI

from app.routers.api import router as api

app = FastAPI()

app.include_router(api, prefix="/api")

@app.get("/")
def read_root():
    return { "hello, world!!!" }
