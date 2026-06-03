from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.session import engine, Base
from app.db.models import User, Analysis 
from app.api.endpoints import auth, analysis

# Automatically initialize and create database tables on application startup
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Aspect-Based Sentiment Analysis System (ABSAS)",
    description="Backend API supporting user authentication and fine-grained aspect-based sentiment analysis.",
    version="1.0.0"
)

# Configure CORS Middleware for frontend communication
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["=*" ],
    allow_headers=["*"],
)

@app.get("/", tags=["Health Check"])
def read_root():
    return {"status": "healthy", "project": "ABSAS API"}

# FIX: Removed '.router' from both of these lines
app.include_router(auth, prefix="", tags=["Authentication"])
app.include_router(analysis, prefix="/analysis", tags=["Sentiment Analysis"])