import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("MONGO_DB_NAME", "buysmart")


class Database:
    client: AsyncIOMotorClient = None
    db = None


db_instance = Database()


async def connect_db():
    """Connect to MongoDB Atlas on application startup."""
    db_instance.client = AsyncIOMotorClient(MONGO_URI)
    db_instance.db = db_instance.client[DB_NAME]
    # Verify connection by pinging the server
    await db_instance.client.admin.command("ping")
    print(f"✅ Connected to MongoDB Atlas — database: '{DB_NAME}'")


async def disconnect_db():
    """Close MongoDB connection on application shutdown."""
    if db_instance.client:
        db_instance.client.close()
        print("🔌 Disconnected from MongoDB Atlas")


def get_db():
    """Return the active database instance."""
    return db_instance.db
