import pytest

from src.main.api.constans.role import Roles

@pytest.mark.api
class TestLoginUser:
    def test_login_admin(self, api_manager, login_admin_request):
        response = api_manager.admin_steps.login_user(login_admin_request)

        assert response.user.username == login_admin_request.username
        assert response.user.role == Roles.ADMIN

    def test_login_user(self, api_manager, login_user_request):
        response = api_manager.admin_steps.login_user(login_user_request)

        assert response.user.username == login_user_request.username
        assert response.user.role == Roles.USER
