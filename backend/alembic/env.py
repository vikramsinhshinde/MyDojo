
from logging.config import fileConfig
import os
from sqlalchemy import engine_from_config, pool
from sqlalchemy import create_engine
from alembic import context
from dotenv import load_dotenv

# ✅ Load environment variables from .env
load_dotenv()

# ✅ Load Alembic config
config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# ✅ Set DB URL dynamically from .env
config.set_main_option("sqlalchemy.url", os.getenv("DATABASE_URL"))

# ✅ Import your models' metadata
from app.db.base import Base  # <-- This should import all models via __init__.py

target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = create_engine(config.get_main_option("sqlalchemy.url"))

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

