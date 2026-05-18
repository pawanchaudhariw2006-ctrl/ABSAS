from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr

# Import database infrastructure from your db/ folder
from db.session import get_db
from db.models import User  # Ensure your User class in models.py matches this

# Import passlib for secure password hashing
from passlib.context import CryptContext

# Setup password hashing configuration
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter()

# --- Pydantic Schemas for Validation ---
class UserRegisterSchema(BaseModel):
    email: EmailStr
    password: str

class UserResponseSchema(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True


# --- API Endpoints ---

# Change "/register" to "/signup" here:
@router.post("/signup", response_model=UserResponseSchema, status_code=status.HTTP_201_CREATED)
def signup(user_in: UserRegisterSchema, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user_in.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email is already registered."
        )
    
    # 2. Hash the user's password securely
    hashed_pass = pwd_context.hash(user_in.password)
    
    # 3. Instantiate the SQLAlchemy model entry
    new_user = User(
        email=user_in.email,
        hashed_password=hashed_pass  # Matches the column name in your models.py
    )
    
    # 4. Save entry to the database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user


@router.post("/login")
def login(user_in: UserRegisterSchema, db: Session = Depends(get_db)):
    # 1. Fetch user by email
    user = db.query(User).filter(User.email == user_in.email).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid email or password."
        )
    
    # 2. Verify hashed password match
    if not pwd_context.verify(user_in.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid email or password."
        )
    
    return {"message": "Login successful!", "user_id": user.id}