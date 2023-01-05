from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    Values are set from .env.sample.sample file
    Rename .env.sample.sample.sample to .env.sample.sample in your local before changing the value.
    """
    POSTGRES_PORT: int
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_HOSTNAME: str

    class Config:
        env_file = "./.env"


settings = Settings()
