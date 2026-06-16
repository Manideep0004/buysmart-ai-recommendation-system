from typing import Optional
from motor.motor_asyncio import AsyncIOMotorCollection, AsyncIOMotorDatabase
from .connection import get_db


def get_users_collection() -> AsyncIOMotorCollection:
    """Return the 'users' collection."""
    db: Optional[AsyncIOMotorDatabase] = get_db()
    assert db is not None, "Database not connected"
    return db["users"]


def get_products_collection() -> AsyncIOMotorCollection:
    """Return the 'products' collection."""
    db: Optional[AsyncIOMotorDatabase] = get_db()
    assert db is not None, "Database not connected"
    return db["products"]


def get_orders_collection() -> AsyncIOMotorCollection:
    """Return the 'orders' collection."""
    db: Optional[AsyncIOMotorDatabase] = get_db()
    assert db is not None, "Database not connected"
    return db["orders"]


def get_wishlist_collection() -> AsyncIOMotorCollection:
    """Return the 'wishlist' collection."""
    db: Optional[AsyncIOMotorDatabase] = get_db()
    assert db is not None, "Database not connected"
    return db["wishlist"]


def get_cart_collection() -> AsyncIOMotorCollection:
    """Return the 'cart' collection."""
    db: Optional[AsyncIOMotorDatabase] = get_db()
    assert db is not None, "Database not connected"
    return db["cart"]


def get_interactions_collection() -> AsyncIOMotorCollection:
    """Return the 'interactions' collection."""
    db: Optional[AsyncIOMotorDatabase] = get_db()
    assert db is not None, "Database not connected"
    return db["interactions"]
