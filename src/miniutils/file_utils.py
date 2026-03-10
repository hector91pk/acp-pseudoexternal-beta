from pathlib import Path


def filename_without_ext(path: str) -> str:
    return Path(path).stem


def ensure_trailing_newline(text: str) -> str:
    return text if text.endswith("\n") else text + "\n"