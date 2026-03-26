"""
Camada de persistência: um único SQLite (`business.db` na raiz do projeto).

- `init_db` em `database.init_db`: cria/migra o schema no go-live local.
- Módulos `db_*.py`: mapa tabelas ↔ páginas Streamlit.
"""

from database.connection import BASE_DIR, DB_PATH, get_conn
from database.init_db import init_db

__all__ = ["BASE_DIR", "DB_PATH", "get_conn", "init_db"]
