"""Testes mínimos de adaptação SQL (? ↔ %s)."""

from __future__ import annotations

import importlib

from database.sql_compat import percent_s_to_qmarks, qmarks_to_percent_s


def test_qmarks_skips_quoted_literals():
    sql = "SELECT * FROM t WHERE a = ? AND note = 'What?' AND b = ?"
    assert qmarks_to_percent_s(sql) == (
        "SELECT * FROM t WHERE a = %s AND note = 'What?' AND b = %s"
    )


def test_percent_s_skips_quoted_literals():
    sql = "SELECT * FROM t WHERE a = %s AND note = 'Say %s' AND b = %s"
    assert percent_s_to_qmarks(sql) == (
        "SELECT * FROM t WHERE a = ? AND note = 'Say %s' AND b = ?"
    )


def test_adapt_sql_respects_provider(monkeypatch):
    monkeypatch.setenv("DB_PROVIDER", "postgres")
    import database.config as cfg

    importlib.reload(cfg)
    import database.sql_compat as sc

    importlib.reload(sc)
    assert (
        sc.adapt_sql("SELECT * WHERE x = %s AND y = %s") == "SELECT * WHERE x = %s AND y = %s"
    )
    assert sc.adapt_sql("SELECT * WHERE x = ? AND y = ?") == (
        "SELECT * WHERE x = %s AND y = %s"
    )
    monkeypatch.setenv("DB_PROVIDER", "sqlite")
    importlib.reload(cfg)
    importlib.reload(sc)
    assert sc.adapt_sql("SELECT * WHERE x = %s AND y = %s") == (
        "SELECT * WHERE x = ? AND y = ?"
    )
