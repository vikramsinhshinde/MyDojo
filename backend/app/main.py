from fastapi import FastAPI
from app.api.api_v1 import api_router
from app.core.config import settings


# Include API routes
app = FastAPI(title="MyDojo API")

app.include_router(api_router, prefix="/api/v1")
