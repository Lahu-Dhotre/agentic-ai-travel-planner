from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    app_name: str = "Agentic AI Trip Planner"
    debug: bool = True
    # Add more config variables as needed

    class Config:
        env_file = ".env"

@lru_cache
def get_settings():
    return Settings()
