"""
Página: Vendas.

Registro de vendas (`sales` com `sale_code`, cliente, desconto, COGS), sequência `sale_sequence_counter`.
Relaciona `products` e `customers`.
"""

TABLES = (
    "sales",
    "sale_sequence_counter",
    "products",
    "customers",
    "sku_master",
)
