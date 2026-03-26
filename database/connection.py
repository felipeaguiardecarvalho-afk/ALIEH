"""Conexão SQLite compartilhada por todas as páginas."""

from __future__ import annotations

import sqlite3
from pathlib import Path

_PKG_DIR = Path(__file__).resolve().parent
BASE_DIR = _PKG_DIR.parent
DB_PATH = BASE_DIR / "business.db"


def get_conn() -> sqlite3.Connection:
    # Nova conexão por uso; Streamlit pode executar código em várias threads.
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn
