from pydantic_settings import BaseSettings

# Configuration class for application settings, using Pydantic's BaseSettings to load environment variables.
class Settings(BaseSettings):
    """
    Application configuration settings loaded from environment variables.
    """
    DATABASE_URL: str
    
    SECRET_KEY: str

    ALGORITHM: str

    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"

settings = Settings()