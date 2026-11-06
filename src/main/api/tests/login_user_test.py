import pytest
from sqlalchemy.orm import Session

from main.api.classes.api_manager import ApiManager
from main.api.models.login_user_request import LoginUserRequest
from src.main.api.db.crud.user_crud import UserCrudDb as User
from src.main.api.constans.role import Roles

@pytest.mark.api
class TestLoginUser:
    def test_login_admin(self, api_manager: ApiManager,db_session: Session, login_admin_request: LoginUserRequest):
        response = api_manager.admin_steps.login_user(login_admin_request)
        user_from_db = User.get_user_by_username(db_session, login_admin_request.username)

        assert user_from_db is not None, "Пользователя нет в бд"
        assert user_from_db.username == login_admin_request.username, "Имя в бд не совпадает с именем в запросе"
        assert response.user.username == login_admin_request.username, "Имя в ответе не совпадает с именем в запросе"
        assert response.user.role == Roles.ADMIN, "Роль админа не соответствует переданной роли"

    def test_login_user(self, api_manager: ApiManager,db_session: Session, login_user_request: LoginUserRequest):
        response = api_manager.admin_steps.login_user(login_user_request)
        user_from_db = User.get_user_by_username(db_session, login_user_request.username)

        assert user_from_db is not None, "Пользователя нет в бд"
        assert user_from_db.username == login_user_request.username, "Имя в бд не совпадает с именем в запросе"
        assert response.user.username == login_user_request.username, "Имя в ответе не совпадает с именем в запросе"
        assert response.user.role == Roles.USER, "Роль пользователя не соответствует переданной роли"
