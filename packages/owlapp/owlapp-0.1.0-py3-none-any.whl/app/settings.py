import os
import secrets
from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings, extra="ignore"):
    """Application settings.
    Only uppercase variables can be configured on the .env file
    """

    model_config = SettingsConfigDict(
        env_file=os.environ.get("OWL_ENV_FILE", ".env"),
        env_file_encoding="utf-8",
    )

    google_discovery_url: str = (
        "https://accounts.google.com/.well-known/openid-configuration"
    )

    # todo: pagination
    # Until we start supporting pagination, we limit the number of
    # records per SELECT query result for performance reasons.
    result_set_hard_limit: int = 1_000

    SECRET_KEY: str = Field(
        description="The secret key for Flask sessions and JWT",
        default=secrets.token_urlsafe(32),
    )
    FLASK_DEBUG: Optional[bool] = Field(
        description="Whether Flask is in debug mode", default=False
    )

    # Google login
    GOOGLE_CLIENT_ID: str = Field(description="The Google client ID", default=None)
    GOOGLE_CLIENT_SECRET: str = Field(
        description="The Google client secret", default=None
    )
    GOOGLE_OAUTH_ENABLED: bool = Field(
        description="Is Google Login enabled.", default=False
    )

    # Database
    SQLALCHEMY_DATABASE_URI: Optional[str] = Field(
        description="The URI for the database. Only Postgres and SQLite supported.",
        default="sqlite:///sqlite.db",
    )

    PRODUCTION: Optional[bool] = Field(
        description="Whether the app is in production mode", default=False
    )
    PUBLIC_URL: Optional[str] = Field(
        description="The public URL of the app", default=None
    )

    # Logging
    LOG_STDOUT: Optional[bool] = Field(
        description="Whether to log to stdout", default=False
    )
    LOG_FORMAT: Optional[str] = Field(
        description="The format of the logs",
        default="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    LOG_LEVEL: Optional[str] = Field(
        description="The level of the logs", default="INFO"
    )

    STORAGE_BASE_PATH: str = Field(
        description="Base path to store files", default="storage"
    )


settings = Settings()
