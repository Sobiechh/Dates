import os
from pathlib import Path

from dotenv import load_dotenv


dotenv_path = Path(os.path.dirname(os.path.abspath(__file__)), ".env")
if dotenv_path.exists():
    load_dotenv(dotenv_path=dotenv_path)


class AppConfig:
    DATABASE_URL: str = os.environ.get("DATABASE_URL")


settings = AppConfig()
