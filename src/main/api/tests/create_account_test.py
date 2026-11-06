import pytest

from sqlalchemy.orm import Session
from src.main.api.db.crud.account_crud import AccountCrud as Account
from src.main.api.utils.allure.attachment_helper import AttachmentHelper

@pytest.mark.api
class TestCreateAccount:

    def test_create_account(self, api_manager,db_session: Session, login_user_request):
        response = api_manager.user_steps.create_account(login_user_request)
        account_from_db = Account.get_account_by_id(db_session, response.id)

        assert response.balance == 0, "Счет не создан"
        assert account_from_db is not None, "Счета нет в бд"
        assert account_from_db.id == response.id, "Пользователя с таким id нет"
        assert account_from_db.balance is not None, "Поля баланс для созданного аккаунта отсуствует в бд"

        AttachmentHelper.attach_orm(
            account_from_db,
            "Получение счета пользователя с бд",
            "Счет пользователя в бд"
        )
