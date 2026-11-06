from typing import Annotated

from src.main.api.generators.creation_rule import CreationRule
from src.main.api.models.base_model import BaseModel


class CreditRepayRequest(BaseModel):
    creditId: Annotated[int, CreationRule(regex=r"^[1-9]{4}")]
    accountId: Annotated[int, CreationRule(regex=r"^[1-9]{4}")]
    amount: Annotated[float, CreationRule(regex=r"^5000")]