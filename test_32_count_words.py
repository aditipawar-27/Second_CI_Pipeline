import importlib

module = importlib.import_module("32_count_words")


def test_count_words_basic():
    assert module.count_words("I love Python programming") == 4


def test_count_words_single_word():
    assert module.count_words("Hello") == 1


def test_count_words_empty_sentence():
    assert module.count_words("") == 0


def test_count_words_extra_spaces():
    assert module.count_words("  Hello   world  ") == 2