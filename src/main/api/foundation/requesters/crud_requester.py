from typing import Optional

import allure
import requests
from requests import Response

from src.main.api.configs.config import Config
from src.main.api.foundation.http_requester import HttpRequester
from src.main.api.models.base_model import BaseModel


class CrudRequester(HttpRequester):
    def post(self, model : Optional[BaseModel]) -> Response:
        body = model.model_dump() if model is not None else ""

        with allure.step(f"POST {Config.fetch("backendUrl")}{self.endpoint.value.url}"):
            allure.attach(str(body), "Request body", allure.attachment_type.JSON)

        response = requests.post(
            url=f"{Config.fetch("backendUrl")}{self.endpoint.value.url}",
            json=body,
            headers=self.headers
        )

        allure.attach(f"{response.text, "Request body", allure.attachment_type.JSON}")

        self.response_spec(response)
        return response

    def delete(self, user_id : int) -> Response:
        response = requests.delete(
            url=f"{Config.fetch("backendUrl")}{self.endpoint.value.url}{user_id}",
            headers=self.headers
        )
        self.response_spec(response)
        return response
