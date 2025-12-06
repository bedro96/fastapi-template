"""Main FastAPI Application"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.config import settings
from app.database import init_db
from app.routes import orders, web


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan context manager"""
    # Startup
    init_db()
    yield
    # Shutdown (if needed)


# Create FastAPI app
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="FastAPI Template with Azure PostgreSQL support",
    lifespan=lifespan,
)

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Include routers
app.include_router(orders.router)
app.include_router(web.router)


@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "version": settings.APP_VERSION}
