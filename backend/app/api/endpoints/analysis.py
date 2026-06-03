from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.analysis import AnalysisRequest, AnalysisResponse # <-- Importing the schema

router = APIRouter()

@router.post("/predict", response_model=AnalysisResponse)
def predict_sentiment(payload: AnalysisRequest):
    # This is a temporary placeholder before linking your ML model
    mock_sentiment = "Positive" 
    
    return {
        "id": 1,
        "text_input": payload.text_input,
        "aspect": payload.aspect,
        "sentiment": mock_sentiment
    }