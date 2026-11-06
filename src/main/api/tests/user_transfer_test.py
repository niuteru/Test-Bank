import pytest
from sqlalchemy.orm import Session

from src.main.api.constans.transaction_type import TransactionType
from src.main.api.db.crud.transaction_crud import TransactionCrud as Transaction
from src.main.api.utils.allure.attachment_helper import AttachmentHelper


@pytest.mark.api
class TestUserTransfer:

    def test_user_transfer_valid(self, api_manager,
                                 login_user_request,
                                 db_session: Session,
                                 user_transfer_request):
        response = api_manager.user_steps.transfer(login_user_request, user_transfer_request)
        transaction_info_from_db = Transaction.get_transaction_by_id(db_session, user_transfer_request.toAccountId)

        assert transaction_info_from_db.transaction_type == TransactionType.TRANSFER, \
            "Тип транзакции не соответствует проведенной операции"
        assert response.fromAccountIdBalance == 0

        AttachmentHelper.attach_orm(
            transaction_info_from_db,
            "Получение транзакции с бд",
            "Транзакция в бд"
        )

    def test_user_transfer_invalid(self, api_manager,
                                   db_session: Session,
                                   login_user_request,
                                   user_transfer_invalid_request):
        api_manager.user_steps.invalid_transfer(login_user_request, user_transfer_invalid_request)
        transaction_info_from_db = Transaction.get_transaction_by_id(db_session,
                                                                     user_transfer_invalid_request.toAccountId)

        assert transaction_info_from_db is None, "Информация о транзакции есть в бд, ошибка"

        AttachmentHelper.attach_orm(
            transaction_info_from_db,
            "Получение транзакции с бд",
            "Транзакция в бд"
        )

