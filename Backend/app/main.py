from fastapi import FastAPI
from app.api.patient import router

app = FastAPI(
    title="Intelligent Vertigo Classification and Emergency Risk Assessment System",
    version="1.0.0"
)

app.include_router(router, prefix="/api")

@app.get("/")
def home():
    return {
        "message": "Backend Running Successfully"
    }