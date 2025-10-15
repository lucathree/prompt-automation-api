import enum
import os

from typing import Self
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppEnv(enum.StrEnum):
    LOCAL = enum.auto()
    DEV = enum.auto()
    PRD = enum.auto()

    @classmethod
    def current(cls) -> Self:
        env = os.getenv("APP_ENV")
        if env is None or env not in cls._value2member_map_:
            raise ValueError("APP_ENV environment variable is not set or invalid")
        return cls(env)


class Settings(BaseSettings):
    db_user: str
    db_password: str
    db_name: str
    db_url: str
    db_host: str = "localhost"
    db_port: int = 5432

    django_secret_key: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


settings = Settings()
