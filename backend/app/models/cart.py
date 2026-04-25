from bson import ObjectId
from pydantic import BaseModel, Field
from typing import List
from .base import PyObjectId


class CartItemDocument(BaseModel):
    """
    Embedded cart line-item.
    References product by ID — cart always shows live price.
    """
    product_id: str
    quantity: int = Field(..., ge=1)


class CartModel(BaseModel):
    """
    MongoDB document model for a User's Cart.

    Design choice — one cart document per user (upsert pattern):
      Instead of creating a new cart on every session, we upsert a
      single document keyed by user_id. This makes add/remove O(1)
      with a targeted $set / $pull on the items array.
    """
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    user_id: str                            # Unique — one cart per user
    items: List[CartItemDocument] = []

    model_config = {
        "populate_by_name": True,
        "arbitrary_types_allowed": True,
        "json_encoders": {ObjectId: str},
    }
