import pytest

from src.main.api.fixtures.api_fixture import api_manager
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.login_user_request import LoginUserRequest
from src.main.api.models.user_depost_request import UserDepositRequest
from src.main.api.models.user_transfer_request import UserTransferRequest


@pytest.fixture
def login_user_request(api_manager) -> LoginUserRequest:
    create_user_request = RandomModelGenerator.generate(CreateUserRequest)
    api_manager.admin_steps.create_user(create_user_request)
    return LoginUserRequest(username=create_user_request.username, password=create_user_request.password)

@pytest.fixture
def user_deposit_request(api_manager, login_user_request) -> UserDepositRequest:
    create_account_response = api_manager.user_steps.create_account(login_user_request)
    return RandomModelGenerator.generate(UserDepositRequest, accountId=create_account_response.id)


@pytest.fixture
def user_deposit_invalid_request() -> UserDepositRequest:
    return RandomModelGenerator.generate(UserDepositRequest)


@pytest.fixture
def user_transfer_request(api_manager, login_user_request) -> UserTransferRequest:
    first_account_response = api_manager.user_steps.create_account(login_user_request)
    second_account_response = api_manager.user_steps.create_account(login_user_request)
    deposit_request = RandomModelGenerator.generate(UserDepositRequest, accountId=first_account_response.id)
    api_manager.user_steps.deposit(login_user_request, deposit_request)

    return RandomModelGenerator.generate(UserTransferRequest,
                                         fromAccountId=first_account_response.id,
                                         toAccountId=second_account_response.id)



@pytest.fixture
def user_transfer_invalid_request(api_manager, login_user_request) -> UserTransferRequest:
    first_account_response = api_manager.user_steps.create_account(login_user_request)
    deposit_request = RandomModelGenerator.generate(UserDepositRequest,
                                                           accountId=first_account_response.id)
    api_manager.user_steps.deposit(login_user_request, deposit_request)

    return RandomModelGenerator.generate(UserTransferRequest)


