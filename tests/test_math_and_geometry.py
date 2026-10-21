import pytest

from tests.helpers import load_solution


@pytest.mark.parametrize(
    ("x", "expected"),
    [(123, 321), (-123, -321), (120, 21), (0, 0), (1534236469, 0), (-(2**31), 0)],
)
def test_0007_reverse_integer(x, expected):
    assert load_solution(7).reverse(x) == expected


@pytest.mark.parametrize(
    ("x", "expected"),
    [(121, True), (-121, False), (10, False), (0, True), (1221, True)],
)
def test_0009_palindrome_number(x, expected):
    assert load_solution(9).isPalindrome(x) is expected
