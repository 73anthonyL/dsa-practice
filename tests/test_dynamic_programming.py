import pytest

from tests.helpers import load_solution


@pytest.mark.parametrize(("n", "expected"), [(1, 1), (2, 2), (3, 3), (5, 8)])
def test_0070_climbing_stairs(n, expected):
    assert load_solution(70).climbStairs(n) == expected


@pytest.mark.parametrize(
    ("num_rows", "expected"),
    [
        (1, [[1]]),
        (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
    ],
)
def test_0118_pascals_triangle(num_rows, expected):
    assert load_solution(118).generate(num_rows) == expected


@pytest.mark.parametrize(
    ("row_index", "expected"), [(0, [1]), (1, [1, 1]), (3, [1, 3, 3, 1])]
)
def test_0119_pascals_triangle_ii(row_index, expected):
    assert load_solution(119).getRow(row_index) == expected
