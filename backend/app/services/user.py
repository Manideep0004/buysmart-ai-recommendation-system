from uuid import uuid4
from ..auth.utils import get_hashed_password

# In-memory user store for Step 1 (will be replaced by DB in Step 2)
users_db = []

class UserService:
    @staticmethod
    async def create_user(user_data):
        user = {
            "id": str(uuid4()),
            "email": user_data.email,
            "password": get_hashed_password(user_data.password)
        }
        users_db.append(user)
        return user

    @staticmethod
    async def get_user_by_email(email: str):
        return next((u for u in users_db if u["email"] == email), None)
