"""Pydantic Schemas for Request/Response validation"""

from pydantic import BaseModel, Field
from typing import Optional


class OrderBase(BaseModel):
    """Base Order schema"""

    name: str = Field(..., min_length=1, max_length=255, description="Order name")
    quantity: int = Field(default=1, ge=1, description="Order quantity")
    description: Optional[str] = Field(None, description="Order description")


class OrderCreate(OrderBase):
    """Schema for creating an order"""

    pass


class OrderUpdate(BaseModel):
    """Schema for updating an order"""

    name: Optional[str] = Field(None, min_length=1, max_length=255)
    quantity: Optional[int] = Field(None, ge=1)
    description: Optional[str] = None


class OrderResponse(OrderBase):
    """Schema for order response"""

    id: int

    model_config = {"from_attributes": True}
