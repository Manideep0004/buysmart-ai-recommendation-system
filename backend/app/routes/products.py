from fastapi import APIRouter, Depends, status
from typing import Optional
from ..services.recommendation import rec_service
from ..auth.utils import get_current_user

router = APIRouter()

@router.get("/recommend/{product_index}")
def get_rec(product_index: int):
    """Index-based recommendations."""
    return rec_service.get_similar_products(str(product_index)) # Note: adjusted to use string ID internally

@router.get("/by-id/{pid}")
async def recommend_by_id(pid: str, current_user: Optional[dict] = Depends(get_current_user)):
    """Find products similar to a specific product ID."""
    # If user is logged in, record this as a 'view' interaction
    if current_user:
        await rec_service.record_interaction(current_user["id"], pid, "view")
    
    return rec_service.get_similar_products(pid)

@router.get("/personalized")
async def get_personalized(current_user: dict = Depends(get_current_user)):
    """Get recommendations based on the logged-in user's recent history."""
    return await rec_service.get_personalized_recommendations(current_user["id"])

@router.post("/interact/{pid}", status_code=status.HTTP_204_NO_CONTENT)
async def interact(pid: str, type: str = "view", current_user: dict = Depends(get_current_user)):
    """Manually record a user interaction (view, click, etc.)."""
    await rec_service.record_interaction(current_user["id"], pid, type)

@router.get("/{product_index}")
def get_rec_by_index(product_index: int):
    """Index-based recommendations."""
    return rec_service.get_similar_products(str(product_index)) # Note: adjusted to use string ID internally

@router.get("/search/popular")
def popular():
    """Return popular products."""
    return rec_service.get_popular_products()

@router.get("/search/{query}")
def search(query: str):
    """Search for products by title."""
    return rec_service.search_products(query)
