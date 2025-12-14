# backend/main.py
from fastapi import FastAPI
from database import engine, Base
from models.test_item import TestItem

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

@app.get("/health")
def health_check():
    return {"status": "ok"}