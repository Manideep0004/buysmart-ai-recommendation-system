import pickle
import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# load files
model = pickle.load(open("model.pkl", "rb"))
meta_df = pickle.load(open("meta.pkl", "rb"))
product_map = pickle.load(open("product_map.pkl", "rb"))
matrix = pickle.load(open("matrix.pkl", "rb"))


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