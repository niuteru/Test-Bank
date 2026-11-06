from typing import Annotated

from src.main.api.generators.creation_rule import CreationRule
from src.main.api.models.base_model import BaseModel


class UserDepositRequest(BaseModel):
    accountId: Annotated[int, CreationRule(regex=r"^[1-9]{6}")]
    amount: Annotated[float, CreationRule(regex=r"1000")]