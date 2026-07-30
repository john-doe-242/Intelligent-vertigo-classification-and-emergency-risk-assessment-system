from fastapi import APIRouter
from app.schemas.patient import PatientAssessment

router = APIRouter()


@router.post("/assessment")
async def patient_assessment(data: PatientAssessment):

    return {
        "status": "success",
        "message": "Patient assessment received successfully.",
        "patient": data
    }