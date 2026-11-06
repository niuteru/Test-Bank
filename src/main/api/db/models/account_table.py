from sqlalchemy import Column, Integer, ForeignKey, Float

from src.main.api.db.base import Base


class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    number = Column(Integer, unique=True, nullable=False)
    balance = Column(Float, nullable=False)

    def __repr__(self) -> str:
        return (f"Account(id={self.id},"
                f" user_id={self.user_id},"
                f" number={self.number},"
                f" balance={self.balance})")