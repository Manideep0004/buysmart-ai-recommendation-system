from datetime import datetime
from typing import Optional
from enum import Enum
from bson import ObjectId
from pydantic import BaseModel, EmailStr, Field
from .base import PyObjectId


class UserRole(str, Enum):
    user = "user"
    admin = "admin"


class UserModel(BaseModel):
    """
    MongoDB document model for a User.
    The `id` field maps to MongoDB's `_id` (ObjectId).
    """
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    email: EmailStr
    hashed_password: str
    role: UserRole = UserRole.user
    avatar: Optional[str] = None         # URL to profile picture
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "populate_by_name": True,        # Allow using 'id' instead of '_id'
        "arbitrary_types_allowed": True,
        "json_encoders": {ObjectId: str},
    }
