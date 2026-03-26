"""Códigos de cliente e sequência."""

import sqlite3


def format_customer_code(n: int) -> str:
    return f"{int(n):05d}"


def sync_customer_sequence_counter_from_customers(conn: sqlite3.Connection) -> None:
    row = conn.execute(
        """
        SELECT MAX(CAST(customer_code AS INTEGER)) AS m
        FROM customers
        WHERE customer_code GLOB '[0-9][0-9][0-9][0-9][0-9]';
        """
    ).fetchone()
    max_n = int(row["m"] or 0) if row else 0
    r2 = conn.execute(
        "SELECT last_value FROM customer_sequence_counter WHERE id = 1;"
    ).fetchone()
    cur = int(r2["last_value"] or 0) if r2 else 0
    conn.execute(
        "UPDATE customer_sequence_counter SET last_value = ? WHERE id = 1;",
        (max(max_n, cur),),
    )
