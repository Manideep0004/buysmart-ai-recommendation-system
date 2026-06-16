import os
import pickle
from typing import List, Dict
from datetime import datetime
from database.collections import get_interactions_collection

# BASE_DIR points to the project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

class RecommendationService:
    def __init__(self):
        # Load the pre-computed KNN model and metadata
        # In a real production app, you might move this to a vector DB later
        self.model = pickle.load(open(os.path.join(BASE_DIR, "model.pkl"), "rb"))
        self.meta_df = pickle.load(open(os.path.join(BASE_DIR, "meta.pkl"), "rb"))
        self.product_map = pickle.load(open(os.path.join(BASE_DIR, "product_map.pkl"), "rb"))
        self.matrix = pickle.load(open(os.path.join(BASE_DIR, "matrix.pkl"), "rb"),)

    async def record_interaction(self, user_id: str, product_id: str, type: str):
        """Save a user interaction to the database."""
        interaction = {
            "user_id": user_id,
            "product_id": product_id,
            "type": type,
            "created_at": datetime.utcnow()
        }
        await get_interactions_collection().insert_one(interaction)

    def get_similar_products(self, pid: str, n: int = 5) -> List[Dict]:
        """Find products similar to a specific product ID using KNN."""
        index = next((i for i, v in self.product_map.items() if v == pid), None)
        if index is None:
            return []
        
        distances, indices = self.model.kneighbors(
            self.matrix.T[index],
            n_neighbors=n + 1
        )
        
        # indices[0][0] is the product itself, so we skip it
        recs = indices.flatten()[1:]
        ids = [self.product_map[i] for i in recs]
        
        return self.meta_df[self.meta_df["product_id"].isin(ids)][["product_id", "title", "image"]].to_dict(orient="records")

    async def get_personalized_recommendations(self, user_id: str, n: int = 10) -> List[Dict]:
        """
        Generate recommendations based on the user's recent history.
        Logic: Get last 3 viewed products and find similar items for each.
        """
        # Get last 3 interactions
        cursor = get_interactions_collection().find(
            {"user_id": user_id, "type": "view"}
        ).sort("created_at", -1).limit(3)
        
        recent_history = await cursor.to_list(length=3)
        
        if not recent_history:
            # Fallback to general recommendations (first 10 items for now)
            # In production, you'd use 'Trending' products here
            return self.meta_df.head(n)[["product_id", "title", "image"]].to_dict(orient="records")

        all_recs = []
        seen_ids = {h["product_id"] for h in recent_history}
        
        for item in recent_history:
            similars = self.get_similar_products(item["product_id"], n=5)
            for s in similars:
                if s["product_id"] not in seen_ids:
                    all_recs.append(s)
                    seen_ids.add(s["product_id"])
        
        return all_recs[:n]

    def search_products(self, query: str, limit: int = 5):
        """Search products by title (from static metadata for now)."""
        results = self.meta_df[self.meta_df["title"].str.contains(query, case=False, na=False)].head(limit)
        return results[["product_id", "title", "image"]].to_dict(orient="records")

# Singleton instance
rec_service = RecommendationService()
