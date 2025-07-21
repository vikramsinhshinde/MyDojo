from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str
    ENVIRONMENT: str
    DEBUG: bool

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    DATABASE_URL: str

    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_BUCKET_NAME: str
    AWS_REGION: str

    class Config:
        env_file = ".env"

settings = Settings()

