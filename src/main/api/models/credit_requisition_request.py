from typing import Annotated

from src.main.api.generators.creation_rule import CreationRule
from src.main.api.models.base_model import BaseModel


class CreditRequisitionRequest(BaseModel):
    accountId: Annotated[int, CreationRule(regex=r"^1")]
    amount: Annotated[int, CreationRule(regex=r"^5000")]
    termMonths: Annotated[int, CreationRule(regex=r"^12")]