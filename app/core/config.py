from dotenv import find_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
import os


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=find_dotenv(),
    )

    @property
    def DATABASE_URL(self):
        return f"sqlite+aiosqlite:///././task_scheduler.db"


settings = Settings()
