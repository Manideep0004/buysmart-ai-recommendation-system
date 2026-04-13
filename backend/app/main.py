from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes.auth import auth_router
from .routes.products import router as product_router

app = FastAPI(title="BuySmart AI Production API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(product_router, prefix="/products", tags=["products"])

@app.get("/")
def home():
    return {"message": "BuySmart AI Production API is running"}
