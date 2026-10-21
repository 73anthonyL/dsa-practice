import pytest

from tests.helpers import load_solution


@pytest.mark.parametrize(
    ("nums", "target", "expected"),
    [
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
        ([1, 3, 5, 6], 0, 0),
    ],
)
def test_0035_search_insert_position(nums, target, expected):
    assert load_solution(35).searchInsert(nums, target) == expected


@pytest.mark.parametrize(
    ("x", "expected"), [(4, 2), (8, 2), (0, 0), (1, 1), (2**31 - 1, 46340)]
)
def test_0069_sqrtx(x, expected):
    assert load_solution(69).mySqrt(x) == expected
