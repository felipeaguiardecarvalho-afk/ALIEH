"""
Página: Precificação.

Fluxo de markup/impostos/juros (`sku_pricing_records`), histórico de preço (`price_history`),
preço de venda e custo médio em `sku_master` (espelhado em `products.price` nas operações do app).
"""

TABLES = (
    "sku_pricing_records",
    "price_history",
    "sku_master",
    "products",
)
