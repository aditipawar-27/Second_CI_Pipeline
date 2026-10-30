
import importlib.util
from pathlib import Path
import pytest

file_path = Path(__file__).with_name("39_transpose_matrix.py")

spec = importlib.util.spec_from_file_location("transpose_module", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

transpose_matrix = module.transpose_matrix


def test_transpose_rectangular_matrix():
    matrix = [[1, 2, 3], [4, 5, 6]]
    assert transpose_matrix(matrix) == [[1, 4], [2, 5], [3, 6]]


def test_transpose_square_matrix():
    matrix = [[1, 2], [3, 4]]
    assert transpose_matrix(matrix) == [[1, 3], [2, 4]]


def test_transpose_single_row():
    matrix = [[1, 2, 3]]
    assert transpose_matrix(matrix) == [[1], [2], [3]]


def test_transpose_single_column():
    matrix = [[1], [2], [3]]
    assert transpose_matrix(matrix) == [[1, 2, 3]]


def test_empty_matrix():
    assert transpose_matrix([]) == []


def test_invalid_matrix():
    matrix = [[1, 2], [3]]

    with pytest.raises(ValueError):
        transpose_matrix(matrix)
