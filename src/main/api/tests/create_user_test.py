import allure
import pytest
from requests import Session

from src.main.api.constans.role import Roles
from src.main.api.db.crud.user_crud import UserCrudDb as User
from src.main.api.fixtures.db_fixture import db_session
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.utils.allure.attachment_helper import AttachmentHelper


@pytest.mark.api
class TestCreateUser:
    @pytest.mark.parametrize(
        "create_user_request",
        [
            RandomModelGenerator.generate(CreateUserRequest)
        ]
    )
    def test_create_user_valid(self, api_manager,db_session: Session, create_user_request):
        response = api_manager.admin_steps.create_user(create_user_request)
        user_from_db = User.get_user_by_username(db_session, create_user_request.username)

        assert create_user_request.username == response.username
        assert create_user_request.role == response.role
        assert create_user_request.username == user_from_db.username, "Пользователь не найден, ошибка"

        AttachmentHelper.attach_orm(
            user_from_db,
            "Получение счета пользователя с бд",
            "Счет пользователя в бд"
        )

    @pytest.mark.parametrize(
        "username, password",
        [
            ("Max1й", "Pas!sw0rd"),
            ("ab", "Pas!sw0rd"),
            ("Max!", "Pas!sw0rd"),
            ("Max1", "Pas!sw0rdу"),
            ("Max1", "pas!sw0"),
            ("Max1", "pas!sw0rd"),
            ("Max1", "PAS!SW0RD"),
            ("Max1", "Passsw0rd"),
            ("Max1", "Pas!sword")
        ]
    )
    def test_create_user_invalid(self, username, password, api_manager, db_session: Session):
        create_user_request = CreateUserRequest(username=username,password=password,role=Roles.USER.value)
        api_manager.admin_steps.create_invalid_user(create_user_request)
        user_from_db = User.get_user_by_username(db_session, create_user_request.username)

        assert user_from_db is None, "Пользователь найден, ошибка"

        AttachmentHelper.attach_orm(
            user_from_db,
            "Получение счета пользователя с бд",
            "Счет пользователя в бд"
        )


