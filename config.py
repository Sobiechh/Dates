import os
from pathlib import Path

from dotenv import load_dotenv

dotenv_path = Path(os.path.dirname(os.path.abspath(__file__)), ".env")
if dotenv_path.exists():
    load_dotenv(dotenv_path=dotenv_path)


class AppConfig:
    POSTGRES_DB: str = os.environ.get("POSTGRES_DB")
    POSTGRES_USER: str = os.environ.get("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.environ.get("POSTGRES_PASSWORD")
    POSTGRES_HOST: str = os.environ.get("POSTGRES_HOST")
    DATABASE_URL: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}"
    SECRET_API_KEY: str = os.environ.get("SECRET_API_KEY")


settings = AppConfig()
