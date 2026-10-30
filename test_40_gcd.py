
import importlib.util
from pathlib import Path

file_path = Path(__file__).with_name("40_gcd.py")

spec = importlib.util.spec_from_file_location("gcd_module", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

find_gcd = module.find_gcd


def test_gcd_of_two_numbers():
    assert find_gcd(48, 18) == 6


def test_gcd_of_equal_numbers():
    assert find_gcd(25, 25) == 25


def test_gcd_when_one_number_is_zero():
    assert find_gcd(10, 0) == 10


def test_gcd_of_coprime_numbers():
    assert find_gcd(7, 13) == 1


def test_gcd_with_negative_numbers():
    assert find_gcd(-48, 18) == 6


def test_gcd_of_two_zeros():
    assert find_gcd(0, 0) == 0
