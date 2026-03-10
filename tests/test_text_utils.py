from miniutils.text_utils import normalize_spaces, slugify, truncate_text


def test_normalize_spaces():
    assert normalize_spaces("hola   mundo") == "hola mundo"


def test_slugify():
    assert slugify("Hola Mundo") == "hola-mundo"


def test_truncate_text():
    assert truncate_text("abcdef", 4) == "a..."
    assert truncate_text("abc", 10) == "abc"