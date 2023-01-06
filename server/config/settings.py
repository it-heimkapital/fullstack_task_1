from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    Values are set from .env file
    """
    POSTGRES_PORT: int
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_HOSTNAME: str

    class Config:
        env_file = "./.env"


settings = Settings()
