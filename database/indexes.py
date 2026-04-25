"""
DB Index Setup Script
=====================
Run this ONCE after connecting to MongoDB to create all necessary indexes.

Usage:
    python -m database.indexes

Why indexes matter:
  - `email` on users → fast login lookups, enforces uniqueness
  - `user_id` on orders/wishlist/cart → fast per-user queries
  - `category` on products → fast filtered browsing
  - `name` text index on products → enables $text search queries
"""
import asyncio
from .connection import connect_db, get_db


async def create_indexes():
    await connect_db()
    db = get_db()

    # Users: unique email
    await db["users"].create_index("email", unique=True)
    print("✅ users.email — unique index")

    # Products: category filter + full-text search on name
    await db["products"].create_index("category")
    await db["products"].create_index([("name", "text"), ("description", "text")])
    print("✅ products.category — index")
    print("✅ products.name + description — text index")

    # Orders: fast per-user lookup, sorted by date
    await db["orders"].create_index([("user_id", 1), ("created_at", -1)])
    print("✅ orders.user_id + created_at — compound index")

    # Wishlist: one document per user
    await db["wishlist"].create_index("user_id", unique=True)
    print("✅ wishlist.user_id — unique index")

    # Cart: one document per user
    await db["cart"].create_index("user_id", unique=True)
    print("✅ cart.user_id — unique index")

    print("\n🎉 All indexes created successfully.")


if __name__ == "__main__":
    asyncio.run(create_indexes())
