import pytest

from src.main.api.models.login_user_request import LoginUserRequest

@pytest.fixture
def login_admin_request() -> LoginUserRequest:
    return LoginUserRequest(username="admin",password="123456")