from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.user import User
from app.schemas.auth import UserRegister
from app.schemas.auth import UserLogin

from app.repositories.user_repository import UserRepository

from app.core.security import (
    hash_password,
    verify_password
)

from app.core.jwt_handler import (
    create_access_token,
    create_refresh_token
)


class AuthService:

    @staticmethod
    def register(
        db: Session,
        request: UserRegister
    ):

        if UserRepository.get_by_email(db, request.email):

            raise HTTPException(
                status_code=400,
                detail="Email already registered."
            )

        if UserRepository.get_by_username(db, request.username):

            raise HTTPException(
                status_code=400,
                detail="Username already exists."
            )

        user = User(

            full_name=request.full_name,

            username=request.username,

            email=request.email,

            hashed_password=hash_password(
                request.password
            ),

            role=request.role,

            department=request.department,

            phone_number=request.phone_number
        )

        return UserRepository.create_user(
            db,
            user
        )

    @staticmethod
    def login(
        db: Session,
        request: UserLogin
    ):

        user = UserRepository.get_by_email(
            db,
            request.email
        )

        if not user:

            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials."
            )

        if not verify_password(
            request.password,
            user.hashed_password
        ):

            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials."
            )

        access_token = create_access_token(

            {
                "sub": user.email,
                "role": user.role
            }

        )

        refresh_token = create_refresh_token(

            {
                "sub": user.email,
                "role": user.role
            }

        )

        return {

            "access_token": access_token,

            "refresh_token": refresh_token,

            "token_type": "bearer",

            "user": user

        }