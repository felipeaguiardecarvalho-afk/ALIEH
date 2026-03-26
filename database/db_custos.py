"""
Página: Custos.

Composição de custo por SKU (`sku_cost_components`), entradas de estoque e CMP
(`stock_cost_entries`), totais planejados em `sku_master.structured_cost_total` / `avg_unit_cost`.
"""

TABLES = (
    "sku_cost_components",
    "stock_cost_entries",
    "sku_master",
    "products",
)
