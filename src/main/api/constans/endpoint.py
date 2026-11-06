from dataclasses import dataclass
from enum import Enum
from typing import Optional, Type

from src.main.api.models.base_model import BaseModel
from src.main.api.models.create_account_response import CreateAccountResponse
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.create_user_response import CreateUserResponse
from src.main.api.models.credit_repay_request import CreditRepayRequest
from src.main.api.models.credit_repay_response import CreditRepayResponse
from src.main.api.models.credit_requisition_request import CreditRequisitionRequest
from src.main.api.models.credit_requisition_response import CreditRequisitionResponse
from src.main.api.models.login_user_request import LoginUserRequest
from src.main.api.models.login_user_response import LoginUserResponse
from src.main.api.models.user_deposit_response import UserDepositResponse
from src.main.api.models.user_depost_request import UserDepositRequest
from src.main.api.models.user_transfer_request import UserTransferRequest
from src.main.api.models.user_transfer_response import UserTransferResponse



@dataclass
class EndpointConfiguration:
    request_model : Optional[Type[BaseModel]]
    url : str
    response_model : Optional[Type[BaseModel]]


class Endpoint(Enum):
    ADMIN_CREATE_USER = EndpointConfiguration(
        request_model=CreateUserRequest,
        url="admin/create",
        response_model=CreateUserResponse
    )

    USER_CREATE_ACCOUNT = EndpointConfiguration(
        request_model=None,
        url="account/create",
        response_model=CreateAccountResponse
    )

    ADMIN_DELETE_USER = EndpointConfiguration(
        request_model=None,
        url="admin/users/",
        response_model=None
    )

    LOGIN_USER = EndpointConfiguration(
        request_model=LoginUserRequest,
        url="auth/token/login",
        response_model=LoginUserResponse
    )

    USER_CREDIT_REPAY = EndpointConfiguration(
        request_model=CreditRepayRequest,
        url="credit/repay",
        response_model=CreditRepayResponse
    )

    USER_CREDIT_REQUISITION = EndpointConfiguration(
        request_model=CreditRequisitionRequest,
        url="credit/request",
        response_model=CreditRequisitionResponse
    )

    USER_DEPOSIT = EndpointConfiguration(
        request_model=UserDepositRequest,
        url="account/deposit",
        response_model=UserDepositResponse
    )

    USER_TRANSFER = EndpointConfiguration(
        request_model=UserTransferRequest,
        url="account/transfer",
        response_model=UserTransferResponse
    )