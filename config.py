"""
Configuration management using environment variables
"""
from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    # API Configuration
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    environment: str = "development"
    
    # CORS Configuration
    cors_origins: str = "http://localhost:5173,http://localhost:3000"
    
    # JWT Configuration
    secret_key: str = "demo-secret-key-change-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # OpenAI Configuration
    openai_api_key: str = ""
    
    # Database Configuration
    database_url: str = ""
    
    # Demo Mode
    demo_mode: bool = True
    
    @property
    def cors_origins_list(self) -> List[str]:
        """Parse CORS origins from comma-separated string"""
        return [origin.strip() for origin in self.cors_origins.split(",")]
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Global settings instance
settings = Settings()
