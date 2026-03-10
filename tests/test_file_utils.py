from miniutils.file_utils import filename_without_ext, ensure_trailing_newline


def test_filename_without_ext():
    assert filename_without_ext("docs/readme.md") == "readme"


def test_ensure_trailing_newline():
    assert ensure_trailing_newline("hola") == "hola\n"
    assert ensure_trailing_newline("hola\n") == "hola\n"