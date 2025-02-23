from app.core.settings import get_settings


settings = get_settings()


DB_CONFIG = {
    "connections": {"default": settings.db.db_url},
    "apps": {
        "models": {
            "models": ["app.models", "aerich.models"],
            "default_connections": "default"
        }
    }
}