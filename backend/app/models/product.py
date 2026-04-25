from datetime import datetime
from typing import List, Optional
from bson import ObjectId
from pydantic import BaseModel, Field
from .base import PyObjectId


class RatingDocument(BaseModel):
    """Embedded document — stored inside the Product document itself."""
    user_id: str
    score: float = Field(..., ge=1.0, le=5.0)
    comment: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)


class ProductModel(BaseModel):
    """
    MongoDB document model for a Product.

    Ratings are embedded (not referenced) because:
      - We always load them together with the product.
      - There won't be millions of ratings per product.
      - It avoids an extra DB round-trip.
    """
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    description: Optional[str] = None
    price: float = Field(..., ge=0)
    category: str
    images: List[str] = []              # List of image URLs
    stock: int = Field(default=0, ge=0)
    ratings: List[RatingDocument] = []  # Embedded ratings array
    avg_rating: float = 0.0             # Pre-computed, updated on each new rating
    rating_count: int = 0               # Pre-computed count
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "populate_by_name": True,
        "arbitrary_types_allowed": True,
        "json_encoders": {ObjectId: str},
    }
