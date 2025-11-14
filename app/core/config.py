from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    @property
    def DATABASE_URL(self):
        return f"sqlite+aiosqlite:///././db.sqlite3"


settings = Settings()
