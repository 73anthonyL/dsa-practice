import pytest

from tests.helpers import load_solution


@pytest.mark.parametrize(
    ("nums", "target", "expected"),
    [([2, 7, 11, 15], 9, [0, 1]), ([3, 2, 4], 6, [1, 2]), ([3, 3], 6, [0, 1])],
)
def test_0001_two_sum(nums, target, expected):
    assert sorted(load_solution(1).twoSum(nums, target)) == expected


@pytest.mark.parametrize(
    ("s", "expected"), [("III", 3), ("LVIII", 58), ("MCMXCIV", 1994), ("IV", 4)]
)
def test_0013_roman_to_integer(s, expected):
    assert load_solution(13).romanToInt(s) == expected


@pytest.mark.parametrize(
    ("strs", "expected"),
    [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        (["alone"], "alone"),
        (["ab", "a"], "a"),
        (["a", "a", "b"], ""),
    ],
)
def test_0014_longest_common_prefix(strs, expected):
    assert load_solution(14).longestCommonPrefix(strs) == expected
