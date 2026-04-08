"""Smoke test pré-deploy: ``python -m database.test_postgres_runtime`` → imprime ``(1,)``.

Cursor com ``tuple_row`` porque :func:`~database.connection.get_postgres_conn` usa ``dict_row`` na ligação.
"""

from __future__ import annotations

from psycopg.rows import tuple_row

from database.connection import get_postgres_conn


def test() -> None:
    conn = get_postgres_conn()
    with conn.cursor(row_factory=tuple_row) as cur:
        cur.execute("SELECT 1", prepare=False)
        print(cur.fetchone())


if __name__ == "__main__":
    test()
