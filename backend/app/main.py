from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes.auth import auth_router
from .routes.products import router as product_router

import sys
import os
# Allow importing the top-level database/ package from inside backend/app/
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from database.connection import connect_db, disconnect_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Handle application startup and shutdown events."""
    # --- Startup ---
    await connect_db()
    yield
    # --- Shutdown ---
    await disconnect_db()


app = FastAPI(title="BuySmart AI Production API", lifespan=lifespan)

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
