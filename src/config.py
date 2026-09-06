from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    db_host: str
    db_port: int = 5432
    db_name: str
    db_user: str
    db_password: str

    aws_region: str
    bedrock_model_id: str

    langfuse_public_key: str
    langfuse_secret_key: str
    langfuse_host: str

    agentcore_memory_id: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()