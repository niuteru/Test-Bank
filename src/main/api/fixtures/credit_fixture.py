import pytest

from src.main.api.constans.role import Roles
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.create_account_response import CreateAccountResponse
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.credit_repay_request import CreditRepayRequest
from src.main.api.models.credit_requisition_request import CreditRequisitionRequest
from src.main.api.models.login_user_request import LoginUserRequest


@pytest.fixture
def login_credit_user_request(api_manager) -> LoginUserRequest:
    create_user_request = RandomModelGenerator.generate(CreateUserRequest, role=Roles.CREDIT_SECRET)
    api_manager.admin_steps.create_user(create_user_request)
    return LoginUserRequest(username=create_user_request.username, password=create_user_request.password)

@pytest.fixture
def credit_requisition(api_manager,
                       login_credit_user_request,
                       create_credit_account) -> CreditRequisitionRequest:
    return RandomModelGenerator.generate(CreditRequisitionRequest,accountId=create_credit_account.id)

@pytest.fixture
def create_credit_account(api_manager, login_credit_user_request) -> CreateAccountResponse:
    return api_manager.user_steps.create_account(login_credit_user_request)


@pytest.fixture
def credit_repay_request(api_manager,
                         login_credit_user_request,
                         credit_requisition) -> CreditRepayRequest:
    credit_requisition_response = api_manager.credit_steps.credit_request(login_credit_user_request,
                                                                          credit_requisition)
    return RandomModelGenerator.generate(CreditRepayRequest,
                                            creditId=credit_requisition_response.creditId,
                                            accountId=credit_requisition_response.accountId)

@pytest.fixture
def credit_repay_invalid_request(api_manager,
                        login_credit_user_request,
                        credit_requisition) -> CreditRepayRequest:
    credit_requisition_response = api_manager.credit_steps.credit_request(login_credit_user_request,
                                                                          credit_requisition)
    return RandomModelGenerator.generate(CreditRepayRequest,
                                            accountId=credit_requisition_response.accountId)