from enum import StrEnum


class TransactionType(StrEnum):
    DEPOSIT = "deposit"
    TRANSFER = "transfer"
    CREDIT_ISSUANCE = "credit_issuance"
    CREDIT_REPAYMENT = "credit_repayment"