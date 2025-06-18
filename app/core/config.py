from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()
class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    SMTP_USER: str
    SMTP_PASSWORD: str
    SMTP_HOST: str
    SMTP_PORT: int
    DEBUG_EMAIL: bool = False  

    class Config:
        env_file = ".env"

settings = Settings()#Instantiates the config object
