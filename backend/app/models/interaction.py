from datetime import datetime
from enum import Enum
from bson import ObjectId
from pydantic import BaseModel, Field
from .base import PyObjectId

class InteractionType(str, Enum):
    view = "view"
    click = "click"
    purchase = "purchase"
    wishlist = "wishlist"

class InteractionModel(BaseModel):
    """
    Stores a single user interaction with a product.
    Used to build the user's interest profile for dynamic recommendations.
    """
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    user_id: str
    product_id: str
    type: InteractionType
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "populate_by_name": True,
        "arbitrary_types_allowed": True,
        "json_encoders": {ObjectId: str},
    }
