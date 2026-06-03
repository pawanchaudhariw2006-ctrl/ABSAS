from pydantic import BaseModel, EmailStr

# What the API expects when a user signs up
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# What the API returns to the frontend (hiding the password)
class UserResponse(BaseModel):
    id: int
    email: str
    is_active: bool

    class Config:
        from_attributes = True