import pytest

from tests.helpers import load_solution


@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True),
        ("([)]", False),
        ("{[]}", True),
        ("(", False),
        ("]", False),
    ],
)
def test_0020_valid_parentheses(s, expected):
    assert load_solution(20).isValid(s) is expected
