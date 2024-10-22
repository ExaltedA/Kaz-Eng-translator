# app/dependencies.py
from fastapi import Request
from app.services.translator import TranslatorService
from app.core.config import settings

# Function that initializes the TranslatorService
def get_translator_service() -> TranslatorService:
    model_name = settings.model_name  # Retrieve model name from config
    translator_service = TranslatorService(model_name=model_name)
    return translator_service

# Inject the loaded translator service into the route
def translator_service_dependency(request: Request) -> TranslatorService:
    return request.app.state.translator_service