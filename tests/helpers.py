"""Shared helpers: run a solution as LeetCode would, and build LeetCode inputs."""

from __future__ import annotations

from collections import deque
from pathlib import Path

SOLUTIONS_DIR = Path(__file__).resolve().parent.parent / "solutions"

# Solutions are kept exactly as submitted, so they use names that LeetCode's
# Python 3 environment provides without imports (List, Optional, deque, ...).
LEETCODE_PRELUDE = """
import bisect, collections, functools, heapq, itertools, math, re, string
from bisect import *
from collections import *
from functools import *
from heapq import *
from itertools import *
from typing import *
"""


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(
        self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


def load_solution(number: int):
    """Return a fresh ``Solution`` for the given problem, wherever its file lives."""
    paths = list(SOLUTIONS_DIR.glob(f"*/{number:04d}_*.py"))
    if len(paths) != 1:
        raise LookupError(f"expected 1 file for problem {number}, found {len(paths)}")
    namespace = {"ListNode": ListNode, "TreeNode": TreeNode}
    exec(LEETCODE_PRELUDE, namespace)  # noqa: S102
    exec(compile(paths[0].read_text(), str(paths[0]), "exec"), namespace)  # noqa: S102
    return namespace["Solution"]()


def build_list(values: list[int], pos: int = -1) -> ListNode | None:
    """Build a linked list; if ``pos`` >= 0, link the tail back to that index."""
    dummy = tail = ListNode()
    nodes = []
    for value in values:
        node = ListNode(value)
        tail.next = node
        tail = node
        nodes.append(node)
    if pos >= 0:
        tail.next = nodes[pos]
    return dummy.next


def list_values(head: ListNode | None) -> list[int]:
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


def build_tree(values: list[int | None]) -> TreeNode | None:
    """Build a tree from LeetCode's level-order format, e.g. ``[1, None, 2, 3]``."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    children = iter(values[1:])
    while queue:
        node = queue.popleft()
        for side in ("left", "right"):
            value = next(children, None)
            if value is not None:
                child = TreeNode(value)
                setattr(node, side, child)
                queue.append(child)
    return root


def inorder_values(root: TreeNode | None) -> list[int]:
    if not root:
        return []
    return inorder_values(root.left) + [root.val] + inorder_values(root.right)
