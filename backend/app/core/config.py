from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    database_url: str = "sqlite:///./mentor.db"
    secret_key: str = "development-only-change-me"
    openai_api_key: str | None = None
    openai_model: str = "gpt-4.1-mini"
    frontend_origin: str = "http://localhost:3000"
    email_from: str | None = None
    resend_api_key: str | None = None

settings = Settings()
