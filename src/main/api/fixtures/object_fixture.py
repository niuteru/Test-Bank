import logging
from typing import List, Any, Generator

import pytest

from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.create_user_response import CreateUserResponse


@pytest.fixture
def created_obj() -> Generator[list[Any], Any, None]:
    objects: List[Any] = []
    yield objects
    clean_users(objects)

def clean_users(objects: List[Any]) -> None:
    api_manager = ApiManager(objects)
    for user in objects:
        if isinstance(user, CreateUserResponse):
            api_manager.admin_steps.delete_user(user.id)
        else:
            logging.warning(f"Unexpected type {type(user)}")
