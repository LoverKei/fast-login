from fastapi.testclient import TestClient
from unittest.mock import MagicMock, patch

from app.main import app

client = TestClient(app)

correct_id = "615ea10e353e1774f9025d7e"
user = {
        "id": correct_id,
        "email": "tester@test.com",
        "name": "test user",
        "nickname": "tester",
        "phone": "01122223333",
        "password": "test password"
}

@patch("app.services.users_service.find_user_by_id", MagicMock(return_value=None))
def test_get_user_with_404_error():
    response = client.get("api/users/615ea10e353e1774f9025d7F")
    print(response)
    assert response.status_code == 404

@patch("app.services.users_service.find_user_by_id", MagicMock(return_value=user))
def test_get_user_with_200_success():
    response = client.get("api/users/" + correct_id)
    assert response.status_code == 200
    assert response.json()["id"] == correct_id
