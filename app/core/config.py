from typing import Optional

from dotenv import load_dotenv
from pydantic import BaseSettings, EmailStr

load_dotenv()


class Settings(BaseSettings):
    app_title: str
    description: str
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    secret: str
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    class Config:
        env_file = '.env'


settings = Settings()
