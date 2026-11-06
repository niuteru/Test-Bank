import pytest
from sqlalchemy.orm import Session

from src.main.api.constans.transaction_type import TransactionType
from src.main.api.db.crud.transaction_crud import TransactionCrud as Transaction
from src.main.api.utils.allure.attachment_helper import AttachmentHelper


@pytest.mark.api
class TestUserDeposit:

    def test_user_deposit_valid(self,api_manager,
                                db_session: Session,
                                login_user_request,
                                user_deposit_request):
        response = api_manager.user_steps.deposit(login_user_request, user_deposit_request)
        transaction_info_from_db = Transaction.get_transaction_by_id(db_session, user_deposit_request.accountId)

        assert transaction_info_from_db.transaction_type == TransactionType.DEPOSIT,\
            "Тип транзакции не соответствует проведенной операции"
        assert response.balance == user_deposit_request.amount, ("Баланс после ответа не соответсвует"
                                                                 " сумме переданной в запрос")

        AttachmentHelper.attach_orm(
            transaction_info_from_db,
            "Получение транзакции с бд",
            "Транзакция в бд"
        )

    def test_user_deposit_invalid(self,api_manager,
                                  db_session: Session,
                                  login_user_request,
                                  user_deposit_invalid_request):
        api_manager.user_steps.invalid_deposit(login_user_request, user_deposit_invalid_request)
        transaction_info_from_db = Transaction.get_transaction_by_id(db_session, user_deposit_invalid_request.accountId)

        assert transaction_info_from_db is None, "Информация о транзакции есть в бд, ошибка"

        AttachmentHelper.attach_orm(
            transaction_info_from_db,
            "Получение транзакции с бд",
            "Транзакция в бд"
        )





