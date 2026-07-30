from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

DATABASE_URL = (
    "postgresql+psycopg://postgres:password@localhost:5432/vertigo_ai"
)

engine = create_engine(
    DATABASE_URL,
    echo=False,
    future=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()