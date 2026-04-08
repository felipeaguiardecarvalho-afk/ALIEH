"""
Camada de persistência.

**App:** :func:`database.connection.get_db_conn` usa **só PostgreSQL** (sem fallback SQLite).

- **SQLite (ficheiro, migrações / ferramentas):** ``database.connection.DB_PATH``.

- `init_db` em `database.init_db`: cria/migra o schema **apenas em SQLite** (sem recriar tabelas
  nem apagar dados — ``CREATE IF NOT EXISTS`` / ``ALTER`` condicionais).
- Módulos `db_*.py`: mapa tabelas ↔ páginas Streamlit.
- :mod:`database.sql_compat`: ``db_execute``, ``adapt_sql``, ``run_insert_returning_id`` (placeholders portáveis).
"""

from database.config import (
    BASE_DIR,
    get_database_provider,
    get_database_url,
    get_db_provider,
    get_postgres_dsn,
    get_supabase_db_url,
)
from database.connection import (
    DB_PATH,
    check_database_health,
    get_db_conn,
    get_postgres_conn,
    maybe_run_periodic_database_health,
)
from database.health_check import (
    schedule_postgres_connectivity_probe_on_startup,
    test_postgres_connection,
)
from database.init_db import init_db
from database.sqlite_export import export_all_data, export_all_data_safe
from database.sql_compat import adapt_sql, db_execute, run_insert_returning_id

__all__ = [
    "BASE_DIR",
    "DB_PATH",
    "check_database_health",
    "get_db_conn",
    "get_database_provider",
    "get_database_url",
    "get_db_provider",
    "get_postgres_conn",
    "get_postgres_dsn",
    "get_supabase_db_url",
    "init_db",
    "maybe_run_periodic_database_health",
    "schedule_postgres_connectivity_probe_on_startup",
    "test_postgres_connection",
    "export_all_data",
    "export_all_data_safe",
    "adapt_sql",
    "db_execute",
    "run_insert_returning_id",
]
