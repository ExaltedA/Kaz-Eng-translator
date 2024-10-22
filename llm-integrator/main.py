# app/main.py
import uvicorn
import logging
from fastapi import FastAPI
from app.api.v1.endpoints.translation import router as translation_router
from app.api.v1.endpoints.health_check import router as healthcheck_router
from app.core.config import settings
from dependencies import get_translator_service  # Import from dependencies

logging.basicConfig(level=settings.logging_level)

app = FastAPI()

# Startup event to load the model
async def startup_event():
    app.state.translator_service = get_translator_service()

# Register the event handlers
app.add_event_handler("startup", startup_event)

# Include the routers
app.include_router(translation_router, prefix="/v1")
app.include_router(healthcheck_router, prefix="/v1")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=settings.api_port)
