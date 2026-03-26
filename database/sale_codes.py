"""Códigos de venda (#####V) e sequência."""

from __future__ import annotations

import re
import sqlite3


def format_sale_code(n: int) -> str:
    return f"{int(n):05d}V"


def _next_sale_sequence(conn: sqlite3.Connection) -> int:
    cur = conn.execute(
        """
        UPDATE sale_sequence_counter
        SET last_value = last_value + 1
        WHERE id = 1
        RETURNING last_value;
        """
    )
    row = cur.fetchone()
    if row is None:
        raise RuntimeError("Contador de sequência de venda não inicializado.")
    return int(row["last_value"])


def sync_sale_sequence_counter_from_sales(conn: sqlite3.Connection) -> None:
    max_n = 0
    for row in conn.execute(
        """
        SELECT sale_code FROM sales
        WHERE sale_code IS NOT NULL AND TRIM(sale_code) != '';
        """
    ):
        s = str(row["sale_code"] or "").strip().upper()
        m = re.match(r"^(\d{5})V$", s)
        if m:
            max_n = max(max_n, int(m.group(1)))
    row2 = conn.execute(
        "SELECT last_value FROM sale_sequence_counter WHERE id = 1;"
    ).fetchone()
    cur = int(row2["last_value"] or 0) if row2 else 0
    conn.execute(
        "UPDATE sale_sequence_counter SET last_value = ? WHERE id = 1;",
        (max(max_n, cur),),
    )
