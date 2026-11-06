import allure

from src.main.api.constans.endpoint import Endpoint
from src.main.api.foundation.requesters.crud_requester import CrudRequester
from src.main.api.foundation.requesters.validate_crud_requester import ValidateCrudRequester
from src.main.api.models.base_model import BaseModel
from src.main.api.models.credit_repay_request import CreditRepayRequest
from src.main.api.models.credit_requisition_request import CreditRequisitionRequest
from src.main.api.models.login_user_request import LoginUserRequest
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.steps.base_steps import BaseSteps


class CreditSteps(BaseSteps):
    @allure.step("Запрос кредита")
    def credit_request(self, login_user_request: LoginUserRequest,
                       credit_requisition: CreditRequisitionRequest) -> BaseModel:
        response = ValidateCrudRequester(
            ResponseSpecs.request_created(),
            RequestSpecs.auth_headers(username=login_user_request.username, password=login_user_request.password),
            Endpoint.USER_CREDIT_REQUISITION
        ).post(credit_requisition)
        return response

    @allure.step("Невалидный запрос кредита")
    def credit_invalid_request(self, login_user_request: LoginUserRequest,
                       credit_requisition: CreditRequisitionRequest) -> None:
        CrudRequester(
            ResponseSpecs.request_bad(),
            RequestSpecs.auth_headers(username=login_user_request.username, password=login_user_request.password),
            Endpoint.USER_CREDIT_REQUISITION
        ).post(credit_requisition)

    @allure.step("Погашение кредита")
    def credit_repay(self, login_user_request: LoginUserRequest,
                       credit_repay_request: CreditRepayRequest) -> BaseModel:
        response = ValidateCrudRequester(
            ResponseSpecs.request_OK(),
            RequestSpecs.auth_headers(username=login_user_request.username, password=login_user_request.password),
            Endpoint.USER_CREDIT_REPAY
        ).post(credit_repay_request)
        return response

    @allure.step("Невалидное погашение кредита")
    def credit_invalid_repay(self, login_user_request: LoginUserRequest,
                       credit_repay_request: CreditRepayRequest) -> None:
        CrudRequester(
            ResponseSpecs.request_bad(),
            RequestSpecs.auth_headers(username=login_user_request.username, password=login_user_request.password),
            Endpoint.USER_CREDIT_REPAY
        ).post(credit_repay_request)


