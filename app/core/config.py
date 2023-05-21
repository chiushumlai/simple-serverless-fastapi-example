from pydantic import BaseSettings


class Settings(BaseSettings):
    prefix: str = "/api/v1"
    secret_key: str = None
    postgres_host: str = None
    postgres_port: int = None
    postgres_username: str = None
    postgres_password: str = None
    postgres_database: str = None

    class Config:
      env_file = ".env"


settings = Settings()