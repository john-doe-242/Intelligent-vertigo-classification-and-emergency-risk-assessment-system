from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime


class UserRegister(BaseModel):
    full_name: str = Field(..., min_length=3, max_length=120)

    username: str = Field(..., min_length=4, max_length=30)

    email: EmailStr

    password: str = Field(..., min_length=8)

    role: str = "doctor"

    department: Optional[str] = None

    phone_number: Optional[str] = None


class UserLogin(BaseModel):
    email: EmailStr

    password: str


class Token(BaseModel):
    access_token: str

    refresh_token: str

    token_type: str = "bearer"


class TokenPayload(BaseModel):
    sub: str

    role: str

    exp: datetime


class RefreshTokenRequest(BaseModel):
    refresh_token: str


class UserResponse(BaseModel):

    id: int

    full_name: str

    username: str

    email: EmailStr

    role: str

    department: Optional[str]

    phone_number: Optional[str]

    is_active: bool

    is_verified: bool

    created_at: datetime

    class Config:
        from_attributes = True