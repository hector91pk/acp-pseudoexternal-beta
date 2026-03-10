def normalize_spaces(text: str) -> str:
    return " ".join(text.split())


def slugify(text: str) -> str:
    return normalize_spaces(text).strip().lower().replace(" ", "-")


def truncate_text(text: str, max_len: int) -> str:
    if max_len < 0:
        raise ValueError("max_len must be >= 0")
    if len(text) <= max_len:
        return text
    if max_len <= 3:
        return text[:max_len]
    return text[: max_len - 3] + "..."