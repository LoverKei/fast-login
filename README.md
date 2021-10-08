# fast-login
login service with fastAPI

python version: 3.9.7

ENV:
    - python 3.7
    - fastapi
    - mongodb
    - redis

PRE-INSTALL:
    - pip install fastapi
    - pip install uvicorn

    - pip install pytest
    - pip install request

    - pip install pymongo
    - pip install redis

RUN: uvicorn app.main:app --reload
