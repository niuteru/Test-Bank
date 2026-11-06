from typing import Any

import allure
import sqlalchemy

from src.main.api.db.base import Base


class AttachmentHelper:

    @staticmethod
    def attach_orm(model: Any, step_name: str, attachment_name: str) -> None:
        with allure.step(step_name):
            allure.attach(model.__repr__(), attachment_name, attachment_type=allure.attachment_type.TEXT)