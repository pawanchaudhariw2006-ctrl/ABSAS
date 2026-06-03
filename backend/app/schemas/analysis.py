from pydantic import BaseModel

# What the frontend sends for sentiment analysis
class AnalysisRequest(BaseModel):
    text_input: str
    aspect: str

# What the backend returns after prediction
class AnalysisResponse(BaseModel):
    id: int
    text_input: str
    aspect: str
    sentiment: str

    class Config:
        from_attributes = True