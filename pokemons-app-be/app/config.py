import os
from pydantic import AnyHttpUrl, BaseSettings
from typing import List, Optional, Dict, Any
from pydantic import PostgresDsn, validator
DOTENV = os.path.abspath(os.path.join(os.path.dirname(__file__), ".env"))

class Settings(BaseSettings):
    DATABASE_URL: str
    POSTGRES_HOSTNAME: str
    POSTGRES_PORT: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_HOSTNAME"),
            port=values.get("POSTGRES_PORT"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )
    
    class Config:
        env_file = DOTENV


settings = Settings()
