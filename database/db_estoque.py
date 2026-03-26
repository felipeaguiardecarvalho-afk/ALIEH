"""
Página: Estoque.

Listagem e filtros sobre lotes com estoque > 0; exclusão de lote (zera estoque/custo/preço).
Não há tabelas exclusivas: usa principalmente `products` e funções que atualizam `sku_master`.
"""

TABLES = (
    "products",
    "sku_master",
)
