import allure

from src.main.api.constans.endpoint import Endpoint
from src.main.api.foundation.requesters.crud_requester import CrudRequester
from src.main.api.foundation.requesters.validate_crud_requester import ValidateCrudRequester
from src.main.api.models.base_model import BaseModel
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.login_user_request import LoginUserRequest
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.steps.base_steps import BaseSteps


class AdminSteps(BaseSteps):

    @allure.step("Создание пользователя")
    def create_user(self,create_user_request : CreateUserRequest ) -> BaseModel:
        response = ValidateCrudRequester(
            ResponseSpecs.request_OK(),
            RequestSpecs.auth_headers(username="admin", password="123456"),
            Endpoint.ADMIN_CREATE_USER
        ).post(create_user_request)

        self.created_obj.append(response)
        return response

    @allure.step("Создание невалидного пользователя")
    def create_invalid_user(self, create_user_request : CreateUserRequest) -> None:
        CrudRequester(
            ResponseSpecs.request_bad(),
            RequestSpecs.auth_headers(username="admin", password="123456"),
            Endpoint.ADMIN_CREATE_USER
        ).post(create_user_request)

    @allure.step("Удаление пользователя")
    def delete_user(self, user_id: int) -> None:
        CrudRequester(
            ResponseSpecs.request_OK(),
            RequestSpecs.auth_headers(username="admin", password="123456"),
            Endpoint.ADMIN_DELETE_USER
        ).delete(user_id)

    @allure.step("Вход пользователя")
    def login_user(self, login_user_request: LoginUserRequest) -> BaseModel:
        response = ValidateCrudRequester(
            ResponseSpecs.request_OK(),
            RequestSpecs.base_headers(),
            Endpoint.LOGIN_USER
        ).post(login_user_request)
        return response