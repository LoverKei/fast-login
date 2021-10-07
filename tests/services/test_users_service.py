from fastapi.testclient import TestClient
from unittest.mock import MagicMock

from app.main import app
from app.models.users_repository import find_user_by_id

client = TestClient(app)

user = {
        "id": "615ea10e353e1774f9025d7e",
        "name": "test user",
        "nickname": "tester",
        "phone": "01122223333"
}

def test_get_user_with_404_error():
    mock = find_user_by_id
    mock.method = MagicMock(return_value=user)
    
    response = client.get("api/users/615ea10e353e1774f9025d7F")
    print(response)
    assert response.status_code == 404

def test_get_user_with_200_success():
    mock = find_user_by_id
    mock.method = MagicMock(return_value=user)
    
    id = "615ea10e353e1774f9025d7e"
    response = client.get("api/users/" + id)
    print(response)
    assert response.status_code == 200
    assert response.json()["id"] == id
