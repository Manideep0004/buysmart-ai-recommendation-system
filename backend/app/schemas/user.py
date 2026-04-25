from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from enum import Enum
from datetime import datetime


class UserRole(str, Enum):
    user = "user"
    admin = "admin"


# --- Request Schemas ---

class UserSignup(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=64)

    model_config = {"json_schema_extra": {"example": {"email": "user@example.com", "password": "secret123"}}}


class UserLogin(BaseModel):
    email: EmailStr
    password: str

    model_config = {"json_schema_extra": {"example": {"email": "user@example.com", "password": "secret123"}}}


class UserUpdate(BaseModel):
    avatar: Optional[str] = None  # URL to profile image
    role: Optional[UserRole] = None  # Admin only


# --- Response Schemas ---

class UserOut(BaseModel):
    id: str
    email: EmailStr
    role: UserRole
    avatar: Optional[str] = None
    created_at: datetime

    model_config = {"from_attributes": True}


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class TokenPayload(BaseModel):
    sub: str          # User ID
    exp: Optional[int] = None
