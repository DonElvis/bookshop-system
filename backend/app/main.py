from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.database import Base, engine
from app.routes.health import router as health_router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.API_TITLE,
    version=settings.API_VERSION,
    description="Modern, scalable snack shop management system",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health_router, prefix=settings.API_PREFIX)


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "Welcome to Snack Shop System API",
        "version": settings.API_VERSION,
        "docs": "/docs",
    }
