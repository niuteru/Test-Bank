from sqlalchemy import Column, Integer, ForeignKey, Double, String, DateTime

from src.main.api.db.base import Base


class Transaction(Base):
    __tablename__ = 'transaction'
    id = Column(Integer, primary_key=True)
    to_account_id = Column(Integer, ForeignKey('account.id'))
    from_account_id = Column(Integer, ForeignKey('account.id'))
    credit_id = Column(Integer, ForeignKey('credit.id'))
    amount = Column(Double, default=0)
    transaction_type = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)

    def __repr__(self) -> str:
        return (f"Transaction(account_id={str(self.to_account_id)},"
                f"from_account_id={self.from_account_id},"
                f"amount={self.amount},"
                f"transaction_type={self.transaction_type},"
                f"created_at={self.created_at})")