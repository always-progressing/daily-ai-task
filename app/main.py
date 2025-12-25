from fastapi import FastAPI
from app.api.health import router as health_router

app = FastAPI(title="AI Daily Tasks")

#app.include_router(health_router, prefix="/health", tags=["Health"]) 
app.include_router(health_router)
