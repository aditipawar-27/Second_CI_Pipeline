import importlib

module = importlib.import_module("36_most_frequent")


def test_most_frequent_basic():
    assert module.most_frequent([1, 2, 2, 3, 2, 4]) == 2


def test_most_frequent_another_list():
    assert module.most_frequent([5, 5, 3, 3, 3, 2]) == 3


def test_single_element():
    assert module.most_frequent([7]) == 7


def test_empty_list():
    assert module.most_frequent([]) is None