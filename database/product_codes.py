"""Código de entrada do lote (nome + data)."""


def _slugify_code_part(text: str) -> str:
    cleaned_chars = []
    last_was_dash = False
    for ch in (text or "").strip():
        if ch.isalnum():
            cleaned_chars.append(ch.upper())
            last_was_dash = False
        elif ch in (" ", "-", "_", "/", "\\"):
            if not last_was_dash:
                cleaned_chars.append("-")
                last_was_dash = True

    slug = "".join(cleaned_chars).strip("-")
    if not slug:
        slug = "ITEM"
    return slug


def make_product_enter_code(product_name: str, registered_date) -> str:
    date_part = registered_date.strftime("%Y%m%d")
    return f"{_slugify_code_part(product_name)}-{date_part}"
