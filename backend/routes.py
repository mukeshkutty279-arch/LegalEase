from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from ai_core.gemini_generator import generate_document


router = APIRouter()


class DocumentRequest(BaseModel):
    document_type: str
    parties: str
    terms: str
    dates: str


@router.get("/health")
def health_check():
    return {
        "status": "healthy",
        "message": "LegalEase backend is working"
    }


@router.post("/generate")
def generate_legal_document(data: DocumentRequest):

    try:
        document = generate_document(
            document_type=data.document_type,
            parties=data.parties,
            terms=data.terms,
            dates=data.dates
        )

        return {
            "document": document
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"AI service error: {str(error)}"
        )
        