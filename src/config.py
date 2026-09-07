import os

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

    cognito_user_pool_id: str
    cognito_client_id: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

def carregar_settings() -> Settings:
    settings_carregadas  = Settings()

    usar_secrets_manager = os.getenv("USER_SECRETS_MANAGER", "false").lower() == "true"
    if usar_secrets_manager:
        from src.aws.secrets import obter_segredo

        segredo_db = obter_segredo("agente-sql-ia/db", region_name=settings_carregadas.aws_region)
        settings_carregadas.db_user = segredo_db["db_user"]
        settings_carregadas.db_password = segredo_db["db_password"]

    return settings_carregadas

settings = carregar_settings()