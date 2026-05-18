import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import time
from fastapi import FastAPI
from api.endpoints import auth, predict
from db import models
from db.session import engine
from sqlalchemy.exc import OperationalError


app = FastAPI(title="ABSAS Backend API")

# Gracefully wait for MySQL container to fully initialize
print("Connecting to MySQL database...")
for i in range(10):  # Try 10 times
    try:
        models.Base.metadata.create_all(bind=engine)
        print("Database tables created/synchronized successfully!")
        break
    except OperationalError as e:
        print(f"Database not ready yet (attempt {i+1}/10). Error: {e}")
        print("Retrying in 3 seconds...")
        time.sleep(3)
else:
    print("Could not connect to the database. Exiting application.")
    raise SystemExit(1)

# Include your endpoint routers matching your folder setup
app.include_router(auth.router, prefix="/api", tags=["Authentication"])
app.include_router(predict.router, prefix="/api", tags=["Analysis"])

@app.get("/")
def home():
    return {"message": "Welcome to the Aspect-Based Sentiment Analysis System API"}