from unittest.mock import MagicMock, patch

from app.services.users_service import UserService

userService = UserService()

correct_id = "615ea10e353e1774f9025d7e"
user = {
        "id": correct_id,
        "email": "tester@test.com",
        "name": "test user",
        "nickname": "tester",
        "phone": "01122223333",
        "password": "test password"
}

@patch("app.models.users_repository.UserRepository.find_user_by_id", MagicMock(return_value=None))
def test_get_user_with_404_error():
    try:
        user = userService.get_user_by_id("615ea10e353e1774f9025d7F")
        if user:
            assert False
    except Exception:
        assert True

@patch("app.models.users_repository.UserRepository.find_user_by_id", MagicMock(return_value=user))
def test_get_user_with_200_success():
    try:
        user = userService.get_user_by_id(correct_id)
        assert user["id"] == correct_id
    except Exception:
        assert False
