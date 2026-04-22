import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from pydantic_settings import BaseSettings

class DBSettings(BaseSettings):
    db_url: str
    model_config = {"env_file": "../../.env", "extra": "ignore"}

settings = DBSettings()
os.makedirs("data", exist_ok=True)

engine = create_engine(settings.db_url, pool_pre_ping=True, echo=False)
SessionLocal = sessionmaker(bind=engine)
Base = DeclarativeBase()