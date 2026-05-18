ABSAS - Aspect Based Sentiment Analysis System
An end-to-end system designed to identify specific aspects in text (e.g., "food", "service") and classify the sentiment associated with each one. This project utilizes a containerized microservices architecture for scalability and ease of deployment.

Features:
1. FastAPI Backend: High-performance Python API for sentiment processing.
2. MySQL Database: Persistent storage for analysis results and metadata.
3. Dockerized Architecture: Simplified environment setup using docker-compose.
4. ML Integration: Dual-model approach for Aspect Extraction and Sentiment Analysis.
5. Swagger UI: Auto-generated interactive API documentation at /docs.

Flowchart

## System Architecture Flowchart

```text
[ User / Frontend ]
        │
        ├── 1. Request: Send Text for Analysis 
        │      (e.g., "The camera is great but the battery life is poor.")
        ▼
┌────────────────────────────────────────────────────────┐
│               FastAPI Backend (App)                    │
│                                                        │
│  ┌─────────────────────────┐                           │
│  │  POST /api/predict     │ ◄─── Requires Auth Token   │
│  └───────────┬─────────────┘                           │
└──────────────┼─────────────────────────────────────────┘
               │
               ▼
┌────────────────────────────────────────────────────────┐
│            Machine Learning Model Router               │
│                                                        │
│       Splits text into Aspects and Sentiments          │
│       using your 2 selected models:                    │
│                                                        │
│       ├── Model 1 (Baseline: spaCy / Rule-based)       │
│       └── Model 2 (Advanced: BERT / Transformer)       │
└──────────────┬─────────────────────────────────────────┘
               │
               ├── 2. Extracts Results:
               │      - Aspect 1: "camera"   -> Positive
               │      - Aspect 2: "battery"  -> Negative
               ▼
┌────────────────────────────────────────────────────────┐
│               Database Layer (MySQL)                   │
│                                                        │
│  ┌─────────────────────────┐                           │
│  │  Analysis Results Table │ ─── Logs analysis history │
│  └─────────────────────────┘     tied to the User ID   │
└──────────────┬─────────────────────────────────────────┘
               │
               ├── 3. Returns Success Response Body
               ▼
[ User / Frontend UI ] ─── Displays Aspect-level breakdown charts
