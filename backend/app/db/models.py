from .session import Base
from sqlalchemy import Column, Integer, String, Float

class Analysis(Base):
    __tablename__ = "absa_results"

    id = Column(Integer, primary_key=True, index=True)
    review_text = Column(String(500))
    aspect = Column(String(100))    # e.g., "Price"
    sentiment = Column(String(50))  # e.g., "Positive"
    confidence = Column(Float)      # Model accuracy score