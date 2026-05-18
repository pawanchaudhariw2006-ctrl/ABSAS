import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Uses the environment variable if present, otherwise defaults to the docker 'db' service
# Adjust 'root' and 'password' if you specified different values in your docker-compose.yml
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "mysql+pymysql://root:password@db:3306/absas_db"
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True  # Automatically checks and recovers broken connections
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency to inject DB sessions into API endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()