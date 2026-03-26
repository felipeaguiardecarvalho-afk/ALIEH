"""
Página: Painel.

Somente leituras agregadas (receita ao longo do tempo, indicadores, estoque baixo).
Não há tabelas dedicadas a esta tela.
"""

TABLES = ()  # sem tabelas próprias

AGGREGATE_SOURCES = (
    "sales",
    "products",
    "sku_master",
)
