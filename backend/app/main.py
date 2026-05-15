from fastapi import FastAPI
from app.db.session import engine
from app.db import models

# This command tells MySQL to create the tables if they don't exist
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="ABSA System API")

@app.get("/")
def health_check():
    return {"status": "Online", "database": "Connected"}