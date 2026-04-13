from fastapi import APIRouter
from ..services.recommendation import rec_service

router = APIRouter()

@router.get("/{product_index}")
def get_rec(product_index: int):
    return rec_service.get_recommendations(product_index)

@router.get("/by-id/{pid}")
def recommend_by_id(pid: str):
    return rec_service.get_recommendations_by_id(pid)

@router.get("/search/{query}")
def search(query: str):
    return rec_service.search_products(query)
