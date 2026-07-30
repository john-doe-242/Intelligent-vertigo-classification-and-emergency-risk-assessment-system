from pydantic import BaseModel, Field


class PatientAssessment(BaseModel):
    patient_name: str = Field(..., min_length=2)
    age: int = Field(..., ge=1, le=120)
    gender: str

    dizziness_duration: str
    nausea: bool
    vomiting: bool
    hearing_loss: bool
    tinnitus: bool
    headache: bool
    blurred_vision: bool
    imbalance: bool

    blood_pressure: str
    heart_rate: int