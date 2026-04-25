from bson import ObjectId
from pydantic import BaseModel, Field
from typing import List
from .base import PyObjectId


class WishlistModel(BaseModel):
    """
    MongoDB document model for a User's Wishlist.

    Design choice — store product_ids as plain strings (references):
      Unlike orders, we always want the LATEST product data (current
      price, availability), so we reference by ID instead of embedding.
      One wishlist per user (1-to-1 relationship).
    """
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    user_id: str                          # Reference to User._id (unique index in DB)
    product_ids: List[str] = []           # References to Product._id

    model_config = {
        "populate_by_name": True,
        "arbitrary_types_allowed": True,
        "json_encoders": {ObjectId: str},
    }
