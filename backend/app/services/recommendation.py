import os
import pickle
from typing import List

# BASE_DIR points to the backend directory (2 levels up from this file)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

class RecommendationService:
    def __init__(self):
        self.model = pickle.load(open(os.path.join(BASE_DIR, "model.pkl"), "rb"))
        self.meta_df = pickle.load(open(os.path.join(BASE_DIR, "meta.pkl"), "rb"))
        self.product_map = pickle.load(open(os.path.join(BASE_DIR, "product_map.pkl"), "rb"))
        self.matrix = pickle.load(open(os.path.join(BASE_DIR, "matrix.pkl"), "rb"))

    def get_recommendations(self, product_index: int, n: int = 5):
        distances, indices = self.model.kneighbors(
            self.matrix.T[product_index],
            n_neighbors=n + 1
        )
        recs = indices.flatten()[1:]
        ids = [self.product_map[i] for i in recs]
        return self.meta_df[self.meta_df["product_id"].isin(ids)][["product_id", "title", "image"]].to_dict(orient="records")

    def get_recommendations_by_id(self, pid: str, n: int = 5):
        index = next((i for i, v in self.product_map.items() if v == pid), None)
        if index is None: return []
        
        distances, indices = self.model.kneighbors(
            self.matrix.T[index],
            n_neighbors=n + 1
        )
        recs = indices.flatten()[1:]
        ids = [self.product_map[i] for i in recs]
        return self.meta_df[self.meta_df["product_id"].isin(ids)][["product_id", "title", "image"]].to_dict(orient="records")

    def search_products(self, query: str, limit: int = 5):
        results = self.meta_df[self.meta_df["title"].str.contains(query, case=False, na=False)].head(limit)
        return results[["product_id", "title", "image"]].to_dict(orient="records")

# Singleton instance
rec_service = RecommendationService()
