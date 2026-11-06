import pytest

from sqlalchemy.orm import Session

from main.api.classes.api_manager import ApiManager
from main.api.models.credit_requisition_request import CreditRequisitionRequest
from main.api.models.login_user_request import LoginUserRequest
from src.main.api.db.crud.credit_crud import CreditCrud as Credit
from src.main.api.utils.allure.attachment_helper import AttachmentHelper


@pytest.mark.api
class TestUserCreditRequests:

    def test_user_credit_request_valid(self, api_manager: ApiManager,
                                       db_session: Session,
                                       credit_requisition: CreditRequisitionRequest,
                                       login_credit_user_request: LoginUserRequest):
        response = api_manager.credit_steps.credit_request(login_credit_user_request, credit_requisition)
        credit_from_db = Credit.get_credit_by_id(db_session, response.accountId)

        assert credit_from_db is not None, "Кредит не был одобрен"
        assert response.balance == credit_requisition.amount, "Ошибка в сумме получения кредита"

        AttachmentHelper.attach_orm(
            credit_from_db,
            "Получение кредита с бд",
            "Кредит в бд"
        )

    def test_user_credit_request_invalid(self, api_manager: ApiManager,
                                         db_session: Session,
                                         credit_requisition: CreditRequisitionRequest,
                                         login_user_request: LoginUserRequest):
        api_manager.credit_steps.credit_invalid_request(login_user_request, credit_requisition)
        credit_from_db = Credit.get_credit_by_id(db_session, credit_requisition.accountId)

        assert credit_from_db is None, "Кредит был одобрен с невалидными данными"

        AttachmentHelper.attach_orm(
            credit_from_db,
            "Получение кредита с бд",
            "Кредит в бд"
        )
