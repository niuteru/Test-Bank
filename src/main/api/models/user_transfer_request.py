from typing import Annotated

from src.main.api.generators.creation_rule import CreationRule
from src.main.api.models.base_model import BaseModel


class UserTransferRequest(BaseModel):
    fromAccountId: Annotated[int, CreationRule(regex=r"^[1-9]{5}")]
    toAccountId: Annotated[int, CreationRule(regex=r"^[1-9]{5}")]
    amount: Annotated[float, CreationRule(regex=r"^1000")]