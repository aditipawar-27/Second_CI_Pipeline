import importlib

module = importlib.import_module("33_first_non_repeating")


def test_first_non_repeating_basic():
    assert module.first_non_repeating("swiss") == "w"


def test_first_non_repeating_first_character():
    assert module.first_non_repeating("hello") == "h"


def test_first_non_repeating_no_unique_character():
    assert module.first_non_repeating("aabb") is None


def test_first_non_repeating_single_character():
    assert module.first_non_repeating("a") == "a"
