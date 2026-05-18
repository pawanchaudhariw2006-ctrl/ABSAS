from fastapi import APIRouter

# This creates the router instance for your machine learning predictions
router = APIRouter()

@router.post("/")
def make_prediction():
    return {"message": "ML Model prediction endpoint"}