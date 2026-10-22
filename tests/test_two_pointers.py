import pytest

from tests.helpers import load_solution


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        ([1, 1, 2], [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4]),
        ([7], [7]),
    ],
)
def test_0026_remove_duplicates_from_sorted_array(nums, expected):
    k = load_solution(26).removeDuplicates(nums)
    assert nums[:k] == expected


@pytest.mark.parametrize(
    ("nums", "val", "expected"),
    [
        ([3, 2, 2, 3], 3, [2, 2]),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, [0, 0, 1, 3, 4]),
        ([1], 1, []),
    ],
)
def test_0027_remove_element(nums, val, expected):
    k = load_solution(27).removeElement(nums, val)
    assert sorted(nums[:k]) == expected


@pytest.mark.parametrize(
    ("nums1", "m", "nums2", "n", "expected"),
    [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ([1], 1, [], 0, [1]),
        ([0], 0, [1], 1, [1]),
    ],
)
def test_0088_merge_sorted_array(nums1, m, nums2, n, expected):
    load_solution(88).merge(nums1, m, nums2, n)
    assert nums1 == expected


@pytest.mark.parametrize(
    ("s", "expected"),
    [("A man, a plan, a canal: Panama", True), ("race a car", False), (" ", True)],
)
def test_0125_valid_palindrome(s, expected):
    assert load_solution(125).isPalindrome(s) is expected
