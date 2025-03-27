from pydantic_settings import BaseSettings
from pydantic import BaseModel
from dotenv import load_dotenv
import os


load_dotenv()

PORT: int = os.environ.get("PORT")
HOST: str = os.environ.get("HOST")
DB_URL: str = os.environ.get("DB_URL")
JWT_SECRET: str = os.environ.get("JWT_SECRET")
CACHE_PORT: int = os.environ.get("REDIS_PORT")
CACHE_HOST: str = os.environ.get("REDIS_HOST")
KAFKA_SERVER: str = os.environ.get("KAFKA_SERVER")

class RunSettings(BaseModel):
    port: int = PORT
    host: str = HOST

class DatabaseSettings(BaseModel):
    db_url: str = DB_URL

class JWTSettings(BaseModel):
    access_token_expired_minutes: int = 60 # 1 hour
    refresh_token_expired_minutes: int = 60 * 60 * 24 # 1 day
    secret: str = JWT_SECRET
    algorithm: str = "HS256"


class CacheSettings(BaseModel):
    host: str = CACHE_HOST
    port: int = CACHE_PORT
    ttl: int = 30 # 30 seconds
    url: str = f"redis://{CACHE_HOST}:{CACHE_PORT}"


class KafkaSettings(BaseModel):
    server: str = KAFKA_SERVER
    mail_topic: str = "mails"
    

MODELS: list = [
    "app.models"
]


class Settings(BaseSettings):
    run: RunSettings = RunSettings()
    db: DatabaseSettings = DatabaseSettings()
    models: list = MODELS
    jwt: JWTSettings = JWTSettings()
    cache: CacheSettings = CacheSettings()
    kafka: KafkaSettings = KafkaSettings()


def get_settings() -> Settings:
    return Settings()