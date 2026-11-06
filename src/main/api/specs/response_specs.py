from http import HTTPStatus
from requests import Response

class ResponseSpecs:

    @staticmethod
    def request_OK():
        def confirm(response : Response):
            assert response.status_code == HTTPStatus.OK, response.text

        return confirm

    @staticmethod
    def request_created():
        def confirm(response: Response):
            assert response.status_code == HTTPStatus.CREATED, response.text

        return confirm

    @staticmethod
    def request_bad():
        def confirm(response: Response):
            assert response.status_code in [HTTPStatus.BAD_REQUEST,
                                            HTTPStatus.NOT_FOUND,
                                            HTTPStatus.UNPROCESSABLE_ENTITY,
                                            HTTPStatus.FORBIDDEN], response.text

        return confirm

