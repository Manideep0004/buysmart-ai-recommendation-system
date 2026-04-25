from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class Rating(BaseModel):
    user_id: str
    score: float = Field(..., ge=1.0, le=5.0)    # 1-5 stars
    comment: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)


# --- Request Schemas ---

class ProductCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=200)
    description: Optional[str] = None
    price: float = Field(..., ge=0)
    category: str
    images: List[str] = []                        # List of image URLs
    stock: int = Field(default=0, ge=0)

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Wireless Headphones",
                "description": "High quality over-ear headphones",
                "price": 49.99,
                "category": "Electronics",
                "images": ["https://example.com/img1.jpg"],
                "stock": 100,
            }
        }
    }


class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=200)
    description: Optional[str] = None
    price: Optional[float] = Field(None, ge=0)
    category: Optional[str] = None
    images: Optional[List[str]] = None
    stock: Optional[int] = Field(None, ge=0)


# --- Response Schemas ---

class ProductOut(BaseModel):
    id: str
    name: str
    description: Optional[str]
    price: float
    category: str
    images: List[str]
    stock: int
    avg_rating: float = 0.0
    rating_count: int = 0
    created_at: datetime

    model_config = {"from_attributes": True}
