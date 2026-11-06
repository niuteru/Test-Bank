from typing import Callable, Dict

from src.main.api.constans.endpoint import Endpoint


class HttpRequester:
    def __init__(self, response_spec: Callable, request_spec: Dict, endpoint : Endpoint):
        self.response_spec = response_spec
        self.headers = request_spec
        self.endpoint = endpoint
