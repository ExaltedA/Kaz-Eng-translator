from fastapi import APIRouter, Depends
from pydantic import BaseModel
from dependencies import translator_service_dependency

router = APIRouter()

class Query(BaseModel):
    text: str

@router.post("/translate/")
def translate(query: Query, translator_service = Depends(translator_service_dependency)):
    translated_text = translator_service.translate(query.text)
    return {"translated_text": translated_text}
