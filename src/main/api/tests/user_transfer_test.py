import pytest
from sqlalchemy.orm import Session

from main.api.classes.api_manager import ApiManager
from main.api.models.login_user_request import LoginUserRequest
from main.api.models.user_transfer_request import UserTransferRequest
from src.main.api.constans.transaction_type import TransactionType
from src.main.api.db.crud.transaction_crud import TransactionCrud as Transaction
from src.main.api.utils.allure.attachment_helper import AttachmentHelper


@pytest.mark.api
class TestUserTransfer:

    def test_user_transfer_valid(self, api_manager: ApiManager,
                                 login_user_request:LoginUserRequest,
                                 db_session: Session,
                                 user_transfer_request: UserTransferRequest):
        response = api_manager.user_steps.transfer(login_user_request, user_transfer_request)
        transaction_info_from_db = Transaction.get_transaction_by_id(db_session, user_transfer_request.toAccountId)

        assert transaction_info_from_db.transaction_type == TransactionType.TRANSFER, \
            "Тип транзакции не соответствует проведенной операции"
        assert response.fromAccountIdBalance == 0, "Перевод не был осуществлен, баланс не изменился"

        AttachmentHelper.attach_orm(
            transaction_info_from_db,
            "Получение транзакции с бд",
            "Транзакция в бд"
        )

    def test_user_transfer_invalid(self, api_manager: ApiManager,
                                   db_session: Session,
                                   login_user_request: LoginUserRequest,
                                   user_transfer_invalid_request: UserTransferRequest):
        api_manager.user_steps.invalid_transfer(login_user_request, user_transfer_invalid_request)
        transaction_info_from_db = Transaction.get_transaction_by_id(db_session,
                                                                     user_transfer_invalid_request.toAccountId)

        assert transaction_info_from_db is None, "Информация о транзакции есть в бд, ошибка"

        AttachmentHelper.attach_orm(
            transaction_info_from_db,
            "Получение транзакции с бд",
            "Транзакция в бд"
        )

