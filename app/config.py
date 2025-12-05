"""Application Configuration"""

import os
from typing import Optional
from dotenv import load_dotenv

load_dotenv()


class Settings:
    """Application settings"""

    # Database
    USE_SQLITE: bool = os.getenv("USE_SQLITE", "False").lower() == "true"
    DATABASE_HOST: Optional[str] = os.getenv("DATABASE_HOST", "localhost")
    DATABASE_PORT: Optional[str] = os.getenv("DATABASE_PORT", "5432")
    DATABASE_NAME: Optional[str] = os.getenv("DATABASE_NAME", "fastapi_db")
    DATABASE_USER: Optional[str] = os.getenv("DATABASE_USER", "postgres")
    DATABASE_PASSWORD: Optional[str] = os.getenv("DATABASE_PASSWORD", "postgres")

    @property
    def database_url(self) -> str:
        """Construct database URL"""
        if self.USE_SQLITE:
            return "sqlite:///./orders.db"
        return (
            f"postgresql://{self.DATABASE_USER}:{self.DATABASE_PASSWORD}"
            f"@{self.DATABASE_HOST}:{self.DATABASE_PORT}/{self.DATABASE_NAME}"
        )

    # Application
    APP_NAME: str = "FastAPI Template"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"


settings = Settings()
