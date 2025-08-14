from __future__ import annotations

from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    app_name: str = "stock-picker"
    env: str = "development"  # development | staging | production
    debug: bool = True
    api_v1_prefix: str = "/api/v1"

    # CORS
    backend_cors_origins: list[str] = ["*"]

    # Security
    secret_key: str = "change-me"

    # Database
    database_url: str = "sqlite:///./data/app.db"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()  # type: ignore[call-arg]
