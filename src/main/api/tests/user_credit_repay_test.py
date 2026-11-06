import allure
import pytest
from sqlalchemy.orm import Session

from src.main.api.db.crud.credit_crud import CreditCrud as Credit
from src.main.api.utils.allure.attachment_helper import AttachmentHelper


@pytest.mark.api
class TestUserCreditRepay:

    def test_user_credit_repay_valid(self, api_manager,
                                     credit_repay_request,
                                     db_session: Session,
                                     login_credit_user_request):
        response = api_manager.credit_steps.credit_repay(login_credit_user_request, credit_repay_request)
        credit_from_db = Credit.get_credit_by_id(db_session, credit_repay_request.accountId)

        assert credit_from_db.amount == response.amountDeposited, "Операция по погашению кредита не прошла, ошибка"
        assert response.amountDeposited == credit_repay_request.amount, "Ошибка в сумме оплаты кредита"

        AttachmentHelper.attach_orm(
            credit_from_db,
            "Получение кредита с бд",
            "Кредит в бд"
        )

    def test_user_credit_repay_invalid(self, api_manager,
                                       db_session: Session,
                                       create_credit_account,
                                       credit_repay_invalid_request,
                                       login_credit_user_request):
        api_manager.credit_steps.credit_invalid_repay(login_credit_user_request, credit_repay_invalid_request)
        credit_from_db = Credit.get_credit_by_id(db_session, credit_repay_invalid_request.accountId)

        assert credit_from_db.balance == -credit_repay_invalid_request.amount,\
            "Кредит погасился при неправильном запросеб ошибка"

        AttachmentHelper.attach_orm(
            credit_from_db,
            "Получение кредита с бд",
            "Кредит в бд"
        )


