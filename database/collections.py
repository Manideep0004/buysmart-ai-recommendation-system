from motor.motor_asyncio import AsyncIOMotorCollection
from .connection import get_db


def get_users_collection() -> AsyncIOMotorCollection:
    """Return the 'users' collection."""
    return get_db()["users"]


def get_products_collection() -> AsyncIOMotorCollection:
    """Return the 'products' collection."""
    return get_db()["products"]


def get_orders_collection() -> AsyncIOMotorCollection:
    """Return the 'orders' collection."""
    return get_db()["orders"]


def get_wishlist_collection() -> AsyncIOMotorCollection:
    """Return the 'wishlist' collection."""
    return get_db()["wishlist"]


def get_cart_collection() -> AsyncIOMotorCollection:
    """Return the 'cart' collection."""
    return get_db()["cart"]
