import requests

from src.main.api.models.login_user_request import LoginUserRequest
from src.main.api.models.login_user_response import LoginUserResponse


class RequestSpecs:
    @staticmethod
    def base_headers():
        return {
            "Content-Type": "application/json",
            "accept": "application/json"
        }

    @staticmethod
    def auth_headers(username: str, password: str):
        request = LoginUserRequest(username=username, password=password)
        headers = RequestSpecs.base_headers()
        response = requests.post(
            url="http://localhost:4111/api/auth/token/login",
            json=request.model_dump(),
            headers=headers
        )

        if response.status_code == 200:
            login_response = LoginUserResponse(**response.json())
            token = login_response.token
            headers["Authorization"] = f"Bearer {token}"
            return headers

        raise Exception("Failed to Login")

