# milestone: base configuration management for all services

import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_NAME: str = "multi-agent-research-system"
    ENV: str = os.getenv("ENV", "dev")

    POSTGRES_URL: str = os.getenv("POSTGRES_URL", "sqlite:///./events.db")
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379")


settings = Settings()