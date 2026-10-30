import importlib

module = importlib.import_module("38_missing_number_xor")


def test_missing_number_basic():
    assert module.missing_number([3, 0, 1]) == 2


def test_missing_number_two():
    assert module.missing_number([0, 1]) == 2


def test_missing_number_large():
    assert module.missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8


def test_missing_number_empty():
    assert module.missing_number([]) == 0