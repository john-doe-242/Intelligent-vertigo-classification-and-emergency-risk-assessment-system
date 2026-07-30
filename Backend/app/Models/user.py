from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime
)

from sqlalchemy.sql import func
from app.database.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String(120), nullable=False)

    email = Column(
        String(255),
        unique=True,
        nullable=False,
        index=True
    )

    username = Column(
        String(100),
        unique=True,
        nullable=False,
        index=True
    )

    hashed_password = Column(
        String(255),
        nullable=False
    )

    role = Column(
        String(30),
        default="doctor",
        nullable=False
    )

    department = Column(
        String(100),
        nullable=True
    )

    phone_number = Column(
        String(20),
        nullable=True
    )

    is_active = Column(
        Boolean,
        default=True
    )

    is_verified = Column(
        Boolean,
        default=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        onupdate=func.now()
    )