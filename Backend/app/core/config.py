from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    PROJECT_NAME: str = (
        "Intelligent Vertigo Classification and Emergency Risk Assessment System"
    )

    API_VERSION: str = "v1"

    SECRET_KEY: str = "CHANGE_THIS_TO_A_RANDOM_SECRET"

    ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    DATABASE_URL: str = (
        "postgresql+psycopg://postgres:password@localhost:5432/vertigo_ai"
    )


settings = Settings()