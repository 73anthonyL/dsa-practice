import pytest

from tests.helpers import build_list, list_values, load_solution


@pytest.mark.parametrize(
    ("l1", "l2", "expected"),
    [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
    ],
)
def test_0002_add_two_numbers(l1, l2, expected):
    result = load_solution(2).addTwoNumbers(build_list(l1), build_list(l2))
    assert list_values(result) == expected


@pytest.mark.parametrize(
    ("list1", "list2", "expected"),
    [([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]), ([], [], []), ([], [0], [0])],
)
def test_0021_merge_two_sorted_lists(list1, list2, expected):
    result = load_solution(21).mergeTwoLists(build_list(list1), build_list(list2))
    assert list_values(result) == expected


@pytest.mark.parametrize(
    ("values", "expected"),
    [([1, 1, 2], [1, 2]), ([1, 1, 2, 3, 3], [1, 2, 3]), ([], [])],
)
def test_0083_remove_duplicates_from_sorted_list(values, expected):
    result = load_solution(83).deleteDuplicates(build_list(values))
    assert list_values(result) == expected


@pytest.mark.parametrize(
    ("values", "pos", "expected"),
    [([3, 2, 0, -4], 1, True), ([1, 2], 0, True), ([1], -1, False), ([], -1, False)],
)
def test_0141_linked_list_cycle(values, pos, expected):
    assert load_solution(141).hasCycle(build_list(values, pos)) is expected
