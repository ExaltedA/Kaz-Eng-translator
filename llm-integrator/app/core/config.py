# app/core/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_name: str = ''
    logging_level: str = 'INFO'
    api_port: int = 8000

    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

settings = Settings()

# Print the settings to debug
print(f"Model Path: {settings.model_name}")
print(f"Logging Level: {settings.logging_level}")
print(f"API Port: {settings.api_port}")
