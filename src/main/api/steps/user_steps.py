import allure

from src.main.api.constans.endpoint import Endpoint
from src.main.api.foundation.requesters.crud_requester import CrudRequester
from src.main.api.foundation.requesters.validate_crud_requester import ValidateCrudRequester
from src.main.api.models.base_model import BaseModel
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.login_user_request import LoginUserRequest
from src.main.api.models.user_depost_request import UserDepositRequest
from src.main.api.models.user_transfer_request import UserTransferRequest
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.steps.base_steps import BaseSteps


class UserSteps(BaseSteps):
    @allure.step("Создание счета в банке")
    def create_account(self, create_user_request: CreateUserRequest) -> BaseModel:
        response = ValidateCrudRequester(
            ResponseSpecs.request_created(),
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.USER_CREATE_ACCOUNT
        ).post()
        return response

    @allure.step("Пополнение баланса")
    def deposit(self, login_user_request: LoginUserRequest,
                user_deposit_requests: UserDepositRequest) -> BaseModel:
        response = ValidateCrudRequester(
            ResponseSpecs.request_OK(),
            RequestSpecs.auth_headers(username=login_user_request.username, password=login_user_request.password),
            Endpoint.USER_DEPOSIT
        ).post(user_deposit_requests)
        return response

    @allure.step("Невалидное Пополнение баланса")
    def invalid_deposit(self, login_user_request: LoginUserRequest,
                        user_deposit_requests: UserDepositRequest) -> None:
        CrudRequester(
            ResponseSpecs.request_bad(),
            RequestSpecs.auth_headers(username=login_user_request.username, password=login_user_request.password),
            Endpoint.USER_DEPOSIT
        ).post(user_deposit_requests)

    @allure.step("Перевод денег")
    def transfer(self, login_user_request: LoginUserRequest,
                 user_transfer_request: UserTransferRequest) -> BaseModel:
        response = ValidateCrudRequester(
            ResponseSpecs.request_OK(),
            RequestSpecs.auth_headers(username=login_user_request.username, password=login_user_request.password),
            Endpoint.USER_TRANSFER
        ).post(user_transfer_request)
        return response

    @allure.step("Невалидный Перевод денег")
    def invalid_transfer(self, login_user_request: LoginUserRequest,
                 user_transfer_request: UserTransferRequest) -> None:
        CrudRequester(
            ResponseSpecs.request_bad(),
            RequestSpecs.auth_headers(username=login_user_request.username, password=login_user_request.password),
            Endpoint.USER_TRANSFER
        ).post(user_transfer_request)

