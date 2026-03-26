"""Linhas de composição de custo por SKU."""

from __future__ import annotations

from datetime import datetime
import sqlite3

from database.constants import SKU_COST_COMPONENT_DEFINITIONS


def ensure_sku_cost_component_rows(conn: sqlite3.Connection, sku: str) -> None:
    if not sku or not str(sku).strip():
        return
    sku = sku.strip()
    now = datetime.now().isoformat(timespec="seconds")
    for key, label in SKU_COST_COMPONENT_DEFINITIONS:
        conn.execute(
            """
            INSERT OR IGNORE INTO sku_cost_components (
                sku, component_key, label, unit_price, quantity, line_total, updated_at
            ) VALUES (?, ?, ?, 0, 0, 0, ?);
            """,
            (sku, key, label, now),
        )
        conn.execute(
            "UPDATE sku_cost_components SET label = ? WHERE sku = ? AND component_key = ?;",
            (label, sku, key),
        )


def recompute_sku_structured_cost_total(conn: sqlite3.Connection, sku: str) -> float:
    sku = sku.strip()
    row = conn.execute(
        """
        SELECT COALESCE(SUM(line_total), 0) AS t
        FROM sku_cost_components
        WHERE sku = ?;
        """,
        (sku,),
    ).fetchone()
    total = float(row["t"] or 0.0)
    now = datetime.now().isoformat(timespec="seconds")
    conn.execute(
        """
        UPDATE sku_master
        SET structured_cost_total = ?, updated_at = ?
        WHERE sku = ?;
        """,
        (total, now, sku),
    )
    return total
