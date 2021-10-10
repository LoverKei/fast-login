from unittest.mock import MagicMock, patch

from app.services.auth_service import AuthService
from app.models.interfaces.users_interface import (
    user_signin_model
)
from app.models.interfaces.auth_interface import (
    token_response,
    verify_token_request,
    verify_token_response
)

authService = AuthService()

correct_id = "615ea10e353e1774f9025d7e"
correct_password = "test password"
hashed_password = authService.get_password_hash("test password")
user = {
        "id": correct_id,
        "email": "tester@test.com",
        "name": "test user",
        "nickname": "tester",
        "phone": "01122223333",
        "password": authService.get_password_hash("test password")
}

signin_user = {
    "id": correct_id,
    "password": correct_password
}

invalid_user = {
    "id": correct_id,
    "password": "wrong password"
}

verify_token_input = {
    "phone": "01122223333"
}

def test_get_signin_type_id():
    id = "615ea10e353e1774f9025d7e"
    type = authService.get_signin_type(id)
    assert type == 'id'

def test_get_signin_type_email():
    id = "tester@email.com"
    type = authService.get_signin_type(id)
    assert type == 'email'

def test_get_signin_type_phone():
    id = "010-1111-2222"
    type = authService.get_signin_type(id)
    assert type == 'phone'

@patch("app.models.users_repository.UserRepository.find_user_by_id", MagicMock(return_value=user))
def test_authenticate_user():
    try:
        authService.authenticate_user(user_signin_model(**signin_user))
        assert True
    except Exception:
        assert False

@patch("app.models.users_repository.UserRepository.find_user_by_id", MagicMock(return_value=user))
def test_wrong_authenticate_user():
    try:
        authService.authenticate_user(user_signin_model(**invalid_user))
        assert False
    except Exception:
        assert True

@patch("app.services.auth_service", "__generate_verify_token", MagicMock(return_value="test_generated_token"))
def test_request_verify_code():
    try:
        token = authService.request_verify_code(verify_token_request(**verify_token_input))
        assert True
    except Exception:
        assert False
