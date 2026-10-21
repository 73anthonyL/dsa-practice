import pytest

from tests.helpers import build_tree, inorder_values, load_solution


@pytest.mark.parametrize(
    ("tree", "expected"),
    [
        ([1, None, 2, 3], [1, 3, 2]),
        ([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9], [4, 2, 6, 5, 7, 1, 3, 9, 8]),
        ([], []),
        ([1], [1]),
    ],
)
def test_0094_binary_tree_inorder_traversal(tree, expected):
    assert load_solution(94).inorderTraversal(build_tree(tree)) == expected


@pytest.mark.parametrize(
    ("p", "q", "expected"),
    [
        ([1, 2, 3], [1, 2, 3], True),
        ([1, 2], [1, None, 2], False),
        ([1, 2, 1], [1, 1, 2], False),
        ([], [], True),
    ],
)
def test_0100_same_tree(p, q, expected):
    assert load_solution(100).isSameTree(build_tree(p), build_tree(q)) is expected


@pytest.mark.parametrize(
    ("tree", "expected"),
    [([1, 2, 2, 3, 4, 4, 3], True), ([1, 2, 2, None, 3, None, 3], False), ([], True)],
)
def test_0101_symmetric_tree(tree, expected):
    assert load_solution(101).isSymmetric(build_tree(tree)) is expected


@pytest.mark.parametrize(
    ("tree", "expected"),
    [([3, 9, 20, None, None, 15, 7], 3), ([1, None, 2], 2), ([], 0)],
)
def test_0104_maximum_depth_of_binary_tree(tree, expected):
    assert load_solution(104).maxDepth(build_tree(tree)) == expected


def _height(node):
    return 1 + max(_height(node.left), _height(node.right)) if node else 0


def _is_balanced(node):
    if not node:
        return True
    return (
        abs(_height(node.left) - _height(node.right)) <= 1
        and _is_balanced(node.left)
        and _is_balanced(node.right)
    )


@pytest.mark.parametrize(
    "nums", [[-10, -3, 0, 5, 9], [1, 3], [0], list(range(1, 16)), list(range(10))]
)
def test_0108_convert_sorted_array_to_binary_search_tree(nums):
    # Several trees are valid, so check the properties instead of one exact shape.
    root = load_solution(108).sortedArrayToBST(nums)
    assert inorder_values(root) == nums
    assert _is_balanced(root)


@pytest.mark.parametrize(
    ("tree", "expected"),
    [
        ([3, 9, 20, None, None, 15, 7], True),
        ([1, 2, 2, 3, 3, None, None, 4, 4], False),
        ([1, 2, 2, 3, None, None, 3, 4, None, None, 4], False),
        ([], True),
    ],
)
def test_0110_balanced_binary_tree(tree, expected):
    assert load_solution(110).isBalanced(build_tree(tree)) is expected


@pytest.mark.parametrize(
    ("tree", "expected"),
    [
        ([3, 9, 20, None, None, 15, 7], 2),
        ([2, None, 3, None, 4, None, 5, None, 6], 5),
        ([], 0),
    ],
)
def test_0111_minimum_depth_of_binary_tree(tree, expected):
    assert load_solution(111).minDepth(build_tree(tree)) == expected


@pytest.mark.parametrize(
    ("tree", "target", "expected"),
    [
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22, True),
        ([1, 2, 3], 5, False),
        ([1, 2], 1, False),
        ([], 0, False),
    ],
)
def test_0112_path_sum(tree, target, expected):
    assert load_solution(112).hasPathSum(build_tree(tree), target) is expected
