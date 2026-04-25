from pydantic import BaseModel, Field
from typing import List


# --- Wishlist Schemas ---

class WishlistAddItem(BaseModel):
    product_id: str

    model_config = {"json_schema_extra": {"example": {"product_id": "abc123"}}}


class WishlistOut(BaseModel):
    id: str
    user_id: str
    product_ids: List[str]

    model_config = {"from_attributes": True}


# --- Cart Schemas ---

class CartItem(BaseModel):
    product_id: str
    quantity: int = Field(..., ge=1)


class CartUpsertItem(BaseModel):
    """Used to add or update an item in the cart."""
    product_id: str
    quantity: int = Field(..., ge=1)

    model_config = {"json_schema_extra": {"example": {"product_id": "abc123", "quantity": 2}}}


class CartOut(BaseModel):
    id: str
    user_id: str
    items: List[CartItem]

    model_config = {"from_attributes": True}
