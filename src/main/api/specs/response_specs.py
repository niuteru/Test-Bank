from http import HTTPStatus
from typing import Callable

from requests import Response

class ResponseSpecs:

    @staticmethod
    def request_OK() -> Callable[..., Response | None]:
        def confirm(response : Response) -> Response | None:
            assert response.status_code == HTTPStatus.OK, response.text

        return confirm

    @staticmethod
    def request_created() -> Callable[..., Response | None]:
        def confirm(response: Response) -> Response | None:
            assert response.status_code == HTTPStatus.CREATED, response.text

        return confirm

    @staticmethod
    def request_bad() -> Callable[..., Response | None]:
        def confirm(response: Response) -> Response | None:
            assert response.status_code in [HTTPStatus.BAD_REQUEST,
                                            HTTPStatus.NOT_FOUND,
                                            HTTPStatus.UNPROCESSABLE_ENTITY,
                                            HTTPStatus.FORBIDDEN], response.text

        return confirm

