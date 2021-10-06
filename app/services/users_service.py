from app.models.users_repository import (
    find_user_by_id,
    insert_user
)

def hello_user() -> str:
    return "hello, user!!!"

def get_user_by_id(id: str):
    result = find_user_by_id(id)
    print(result)
    return result

def create_user():
    dummy_user = {
        "email": "test@test.com",
        "nickname": "tester",
        "password": "test pass word",
        "name": "tester A",
        "phone": "01022223333"
    }
    return insert_user(dummy_user)
