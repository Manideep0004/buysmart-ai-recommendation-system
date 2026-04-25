from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum
from datetime import datetime


class OrderStatus(str, Enum):
    pending = "pending"
    processing = "processing"
    shipped = "shipped"
    delivered = "delivered"
    cancelled = "cancelled"


class OrderItem(BaseModel):
    product_id: str
    name: str          # Snapshot of name at order time (price can change later)
    price: float
    quantity: int = Field(..., ge=1)
    image: Optional[str] = None


# --- Request Schemas ---

class OrderCreate(BaseModel):
    items: List[OrderItem] = Field(..., min_length=1)
    payment_intent_id: Optional[str] = None   # From Stripe (Step 8)

    model_config = {
        "json_schema_extra": {
            "example": {
                "items": [{"product_id": "abc123", "name": "Headphones", "price": 49.99, "quantity": 2}],
                "payment_intent_id": "pi_xxx",
            }
        }
    }


class OrderStatusUpdate(BaseModel):
    status: OrderStatus


# --- Response Schemas ---

class OrderOut(BaseModel):
    id: str
    user_id: str
    items: List[OrderItem]
    total: float
    status: OrderStatus
    payment_intent_id: Optional[str] = None
    created_at: datetime

    model_config = {"from_attributes": True}
