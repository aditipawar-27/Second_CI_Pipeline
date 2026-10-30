import importlib

module = importlib.import_module("37_rotate_string")


def test_rotate_string_basic():
    assert module.rotate_string("abcdef", 2) == "efabcd"


def test_rotate_string_zero_positions():
    assert module.rotate_string("hello", 0) == "hello"


def test_rotate_string_more_than_length():
    assert module.rotate_string("abc", 4) == "cab"


def test_rotate_empty_string():
    assert module.rotate_string("", 2) == ""