"""Order Model"""

from sqlalchemy import Column, Integer, String, Text
from app.database import Base


class Order(Base):
    """Order table model"""

    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False, index=True)
    quantity = Column(Integer, nullable=False, default=1)
    description = Column(Text, nullable=True)

    def __repr__(self) -> str:
        return f"<Order(id={self.id}, name='{self.name}', quantity={self.quantity})>"
