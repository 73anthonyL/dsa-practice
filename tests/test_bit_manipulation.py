import pytest

from tests.helpers import load_solution


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [("11", "1", "100"), ("1010", "1011", "10101"), ("0", "0", "0")],
)
def test_0067_add_binary(a, b, expected):
    assert load_solution(67).addBinary(a, b) == expected


@pytest.mark.parametrize(
    ("nums", "expected"), [([2, 2, 1], 1), ([4, 1, 2, 1, 2], 4), ([1], 1)]
)
def test_0136_single_number(nums, expected):
    assert load_solution(136).singleNumber(nums) == expected
