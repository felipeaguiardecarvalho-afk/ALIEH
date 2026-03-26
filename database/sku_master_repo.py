"""Mestre de SKU: existência e total de estoque por SKU."""

from __future__ import annotations

from datetime import datetime
import sqlite3


def ensure_sku_master(conn: sqlite3.Connection, sku: str) -> None:
    if not sku or not str(sku).strip():
        raise ValueError("SKU é obrigatório para custeio de estoque.")
    sku = sku.strip()
    now = datetime.now().isoformat(timespec="seconds")
    conn.execute(
        """
        INSERT OR IGNORE INTO sku_master (sku, total_stock, avg_unit_cost, selling_price, updated_at, deleted_at)
        VALUES (?, 0, 0, 0, ?, NULL);
        """,
        (sku, now),
    )


def sync_sku_master_totals(conn: sqlite3.Connection, sku: str) -> None:
    if not sku or not str(sku).strip():
        return
    sku = sku.strip()
    exists = conn.execute(
        "SELECT 1 FROM sku_master WHERE sku = ?;",
        (sku,),
    ).fetchone()
    if exists is None:
        ensure_sku_master(conn, sku)
    total = float(
        conn.execute(
            """
            SELECT COALESCE(SUM(stock), 0) FROM products
            WHERE sku = ? AND deleted_at IS NULL;
            """,
            (sku,),
        ).fetchone()[0]
    )
    now = datetime.now().isoformat(timespec="seconds")
    conn.execute(
        """
        UPDATE sku_master SET total_stock = ?, updated_at = ? WHERE sku = ?;
        """,
        (total, now, sku),
    )
