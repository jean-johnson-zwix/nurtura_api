from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "nurtura"
    database_user_name: str
    database_password: str
    database_host: str
    database_port: int
    database_name: str
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()

DATABASE_URL = f"postgresql://{settings.database_user_name}:{settings.database_password}@{settings.database_host}:{settings.database_port}/{settings.database_name}"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind = engine)
Base = declarative_base()
