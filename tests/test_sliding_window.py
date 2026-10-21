import pytest

from tests.helpers import load_solution


@pytest.mark.parametrize(
    ("s", "expected"),
    [("abcabcbb", 3), ("bbbbb", 1), ("pwwkew", 3), ("", 0), ("abba", 2), ("dvdf", 3)],
)
def test_0003_longest_substring_without_repeating_characters(s, expected):
    assert load_solution(3).lengthOfLongestSubstring(s) == expected


@pytest.mark.parametrize(
    ("prices", "expected"), [([7, 1, 5, 3, 6, 4], 5), ([7, 6, 4, 3, 1], 0), ([1], 0)]
)
def test_0121_best_time_to_buy_and_sell_stock(prices, expected):
    assert load_solution(121).maxProfit(prices) == expected
