from miniutils.math_utils import add, clamp, safe_div


def test_add():
    assert add(2, 3) == 5


def test_clamp():
    assert clamp(10, 0, 5) == 5
    assert clamp(-1, 0, 5) == 0
    assert clamp(3, 0, 5) == 3


def test_safe_div():
    assert safe_div(10, 2) == 5
    assert safe_div(10, 0) is None