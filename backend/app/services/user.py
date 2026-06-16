import os
import sys
from datetime import datetime
from ..auth.utils import get_hashed_password

# Allow importing the top-level database/ package from inside backend/app/services/
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from database.collections import get_users_collection

class UserService:
    @staticmethod
    async def create_user(user_data):
        user_doc = {
            "email": user_data.email,
            "password": get_hashed_password(user_data.password),
            "role": "user",
            "avatar": None,
            "created_at": datetime.utcnow(),
        }
        result = await get_users_collection().insert_one(user_doc)
        user_doc["id"] = str(result.inserted_id)
        return user_doc

    @staticmethod
    async def get_user_by_email(email: str):
        user = await get_users_collection().find_one({"email": email})
        if user:
            user["id"] = str(user["_id"])
        return user
