ABSAS - Aspect Based Sentiment Analysis System
An end-to-end system designed to identify specific aspects in text (e.g., "food", "service") and classify the sentiment associated with each one. This project utilizes a containerized microservices architecture for scalability and ease of deployment.

Features:
1. FastAPI Backend: High-performance Python API for sentiment processing.
2. MySQL Database: Persistent storage for analysis results and metadata.
3. Dockerized Architecture: Simplified environment setup using docker-compose.
4. ML Integration: Dual-model approach for Aspect Extraction and Sentiment Analysis.
5. Swagger UI: Auto-generated interactive API documentation at /docs.

Flowchart

## System Architecture Flowchart (Backend)

```text
[ Incoming HTTP Request ] ──► Body: { "text": "..." } | Header: Bearer <JWT>
                  │
                  ▼
┌──────────────────────────────────────────────────┐
│ 1. SECURITY MODULE (app/api/endpoints/auth.py)   │
├──────────────────────────────────────────────────┤
│ • Uses PyJWT & Passlib (Bcrypt) libraries        │
│ • Validates cryptographic JWT signature          │
└─────────────────┬────────────────────────────────┘
                  │
                  ▼
┌──────────────────────────────────────────────────┐
│ 2. INGESTION ROUTER (app/api/endpoints/predict.py)
├──────────────────────────────────────────────────┤
│ • FastAPI POST `/api/` Endpoint                  │
│ • Packages request payload for the ML pipeline   │
└─────────────────┬────────────────────────────────┘
                  │
                  ▼
┌──────────────────────────────────────────────────┐
│ 3. CORE NLP ENGINE (app/ml_model.py)             │
├──────────────────────────────────────────────────┤
│ Splits text array concurrently into 2 tracks:    │
│                                                  │
│ ├── Track A: spaCy (Grammar Baseline Engine)     │
│ │                                                │
│ └── Track B: BERT (Deep Learning Transformer)    │ 
└─────────────────┬────────────────────────────────┘
                  │
                  ▼
┌──────────────────────────────────────────────────┐
│ 4. SQLALCHEMY ORM (app/db/models.py & session.py)|
├──────────────────────────────────────────────────┤
│ • SQLAlchemy Database Engine instantiation       │
│ • Binds the ML extraction data row directly with │
│   the verified structural owner column: `user_id`│   
└─────────────────┬────────────────────────────────┘
                  │ 
                  ▼
┌──────────────────────────────────────────────────┐
│ 5. DATABASE CONTAINER (absas-db-1 MySQL Engine)  │
├──────────────────────────────────────────────────┤
│ • Schema Enforcement (One-to-Many Relationship)  │
│ • Permanently saves transaction history row      │
│ • Verifies user index match via Foreign Key (FK) │
└─────────────────┬────────────────────────────────┘
                  │
                  ▼
┌──────────────────────────────────────────────────┐
│ 6. RESPONSE SERIALIZATION (app/main.py Engine)   │
├──────────────────────────────────────────────────┤
│ • Packages data values using `AnalysisOutSchema` │
│ • Filters out hidden database identity strings   │
└─────────────────┬────────────────────────────────┘
                  │
                  ▼
       [ HTTP 200 Success JSON Response ] ──► Sent to UI to build frontend charts