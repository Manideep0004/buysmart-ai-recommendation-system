from datetime import datetime
from typing import List, Optional
from enum import Enum
from bson import ObjectId
from pydantic import BaseModel, Field
from .base import PyObjectId


class OrderStatus(str, Enum):
    pending = "pending"
    processing = "processing"
    shipped = "shipped"
    delivered = "delivered"
    cancelled = "cancelled"


class OrderItemDocument(BaseModel):
    """
    Embedded snapshot of a product at order time.

    Why snapshot and not a reference?
      Product prices and names can change after purchase. Storing a
      snapshot preserves the exact state the user agreed to pay for.
    """
    product_id: str                      # Reference kept for lookup
    name: str                            # Snapshot
    price: float                         # Snapshot (price at time of purchase)
    quantity: int = Field(..., ge=1)
    image: Optional[str] = None          # Snapshot


class OrderModel(BaseModel):
    """MongoDB document model for an Order."""
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    user_id: str                         # Reference to User._id
    items: List[OrderItemDocument]
    total: float                         # Pre-computed: sum(price * qty)
    status: OrderStatus = OrderStatus.pending
    payment_intent_id: Optional[str] = None   # Stripe payment intent (Step 8)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "populate_by_name": True,
        "arbitrary_types_allowed": True,
        "json_encoders": {ObjectId: str},
    }
