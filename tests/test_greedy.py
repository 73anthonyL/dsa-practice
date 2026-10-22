import pytest

from tests.helpers import load_solution


@pytest.mark.parametrize(
    ("g", "s", "expected"),
    [([1, 2, 3], [1, 1], 1), ([1, 2], [1, 2, 3], 2), ([10, 9, 8, 7], [5, 6, 7, 8], 2)],
)
def test_0455_assign_cookies(g, s, expected):
    assert load_solution(455).findContentChildren(g, s) == expected
