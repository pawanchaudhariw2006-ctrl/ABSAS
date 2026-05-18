from pydantic import BaseModel, EmailStr
from typing import Optional

# --- User Schemas ---
class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True


# --- Analysis Schemas ---
class AnalysisRequest(BaseModel):
    text: str

class AnalysisResponse(BaseModel):
    id: int
    text: str
    aspect: Optional[str] = None
    sentiment: Optional[str] = None
    confidence: Optional[float] = None
    user_id: int

    class Config:
        from_attributes = True