from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.config import settings

DATABASE_URL = (
    f"postgresql+psycopg2://{settings.db_user}:{settings.db_password}"
    f"@{settings.db_host}:{settings.db_port}/{settings.db_name}"
)

# pool_pre_ping evita erros co conexões que ficarma ociosas por muito tempo
engine = create_engine(DATABASE_URL, pool_pre_ping=True, pool_size=5, max_overflow=0)
SessionLocal = sessionmaker(bind=engine)