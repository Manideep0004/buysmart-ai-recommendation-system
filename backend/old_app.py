import os
import pickle
import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

BASE_DIR = os.path.dirname(__file__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# load files
model = pickle.load(
    open(os.path.join(BASE_DIR, "model.pkl"), "rb")
)

meta_df = pickle.load(
    open(os.path.join(BASE_DIR, "meta.pkl"), "rb")
)

product_map = pickle.load(
    open(os.path.join(BASE_DIR, "product_map.pkl"), "rb")
)

matrix = pickle.load(
    open(os.path.join(BASE_DIR, "matrix.pkl"), "rb")
)


def recommend(product_index, n=5):
    distances, indices = model.kneighbors(
        matrix.T[product_index],
        n_neighbors=n + 1
    )

    recs = indices.flatten()[1:]
    ids = [product_map[i] for i in recs]

    return meta_df[
        meta_df["product_id"].isin(ids)
    ][["product_id", "title", "image"]].to_dict(
        orient="records"
    )


@app.get("/")
def home():
    return {"message": "BuySmart API running"}


@app.get("/recommend/{product_index}")
def get_rec(product_index: int):
    return recommend(product_index)


@app.get("/recommend_by_id/{pid}")
def recommend_by_id(pid: str):

    index = None
    for i, v in product_map.items():
        if v == pid:
            index = i
            break

    if index is None:
        return []

    distances, indices = model.kneighbors(
        matrix.T[index],
        n_neighbors=6
    )

    recs = indices.flatten()[1:]

    ids = [product_map[i] for i in recs]

    return meta_df[
        meta_df["product_id"].isin(ids)
    ][["product_id", "title", "image"]].to_dict(
        orient="records"
    )


@app.get("/search/{query}")
def search(query: str):

    results = meta_df[
        meta_df["title"].str.contains(
            query,
            case=False,
            na=False
        )
    ].head(5)

    return results[
        ["product_id", "title", "image"]
    ].to_dict(orient="records")