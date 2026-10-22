# Data Structures & Algorithms

[![CI](https://github.com/73anthonyL/dsa-practice/actions/workflows/ci.yml/badge.svg)](https://github.com/73anthonyL/dsa-practice/actions/workflows/ci.yml)
![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)

My Python solutions to LeetCode problems, organized by topic along the
[NeetCode roadmap](https://neetcode.io/roadmap). Solutions are kept exactly as
submitted to LeetCode, and every one is tested against the problem's examples.

## Solutions

Space complexity excludes the output. `h` is the height of the tree.

### Arrays & Hashing

| # | Problem | Difficulty | Solution | Time | Space |
| --: | --- | --- | --- | --- | --- |
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | [Python](solutions/arrays-and-hashing/0001_two_sum.py) | `O(n log n)` | `O(n)` |
| 13 | [Roman to Integer](https://leetcode.com/problems/roman-to-integer/) | Easy | [Python](solutions/arrays-and-hashing/0013_roman_to_integer.py) | `O(n)` | `O(1)` |
| 14 | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) | Easy | [Python](solutions/arrays-and-hashing/0014_longest_common_prefix.py) | `O(n * m)` | `O(m)` |

### Two Pointers

| # | Problem | Difficulty | Solution | Time | Space |
| --: | --- | --- | --- | --- | --- |
| 26 | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | Easy | [Python](solutions/two-pointers/0026_remove_duplicates_from_sorted_array.py) | `O(n)` | `O(1)` |
| 27 | [Remove Element](https://leetcode.com/problems/remove-element/) | Easy | [Python](solutions/two-pointers/0027_remove_element.py) | `O(n)` | `O(n)` |
| 88 | [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) | Easy | [Python](solutions/two-pointers/0088_merge_sorted_array.py) | `O(m + n)` | `O(1)` |
| 125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Easy | [Python](solutions/two-pointers/0125_valid_palindrome.py) | `O(n)` | `O(1)` |

### Sliding Window

| # | Problem | Difficulty | Solution | Time | Space |
| --: | --- | --- | --- | --- | --- |
| 3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Medium | [Python](solutions/sliding-window/0003_longest_substring_without_repeating_characters.py) | `O(n)` | `O(min(n, k))` |
| 121 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Easy | [Python](solutions/sliding-window/0121_best_time_to_buy_and_sell_stock.py) | `O(n)` | `O(1)` |

### Stack

| # | Problem | Difficulty | Solution | Time | Space |
| --: | --- | --- | --- | --- | --- |
| 20 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Easy | [Python](solutions/stack/0020_valid_parentheses.py) | `O(n)` | `O(n)` |

### Binary Search

| # | Problem | Difficulty | Solution | Time | Space |
| --: | --- | --- | --- | --- | --- |
| 35 | [Search Insert Position](https://leetcode.com/problems/search-insert-position/) | Easy | [Python](solutions/binary-search/0035_search_insert_position.py) | `O(log n)` | `O(1)` |
| 69 | [Sqrt(x)](https://leetcode.com/problems/sqrtx/) | Easy | [Python](solutions/binary-search/0069_sqrtx.py) | `O(1)` | `O(1)` |

### Linked List

| # | Problem | Difficulty | Solution | Time | Space |
| --: | --- | --- | --- | --- | --- |
| 2 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | Medium | [Python](solutions/linked-list/0002_add_two_numbers.py) | `O(max(n, m))` | `O(1)` |
| 21 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Easy | [Python](solutions/linked-list/0021_merge_two_sorted_lists.py) | `O(n + m)` | `O(1)` |
| 83 | [Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) | Easy | [Python](solutions/linked-list/0083_remove_duplicates_from_sorted_list.py) | `O(n)` | `O(1)` |
| 141 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Easy | [Python](solutions/linked-list/0141_linked_list_cycle.py) | `O(n)` | `O(1)` |

### Trees

| # | Problem | Difficulty | Solution | Time | Space |
| --: | --- | --- | --- | --- | --- |
| 94 | [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) | Easy | [Python](solutions/trees/0094_binary_tree_inorder_traversal.py) | `O(n)` | `O(h)` |
| 100 | [Same Tree](https://leetcode.com/problems/same-tree/) | Easy | [Python](solutions/trees/0100_same_tree.py) | `O(n)` | `O(h)` |
| 101 | [Symmetric Tree](https://leetcode.com/problems/symmetric-tree/) | Easy | [Python](solutions/trees/0101_symmetric_tree.py) | `O(n)` | `O(h)` |
| 104 | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Easy | [Python](solutions/trees/0104_maximum_depth_of_binary_tree.py) | `O(n)` | `O(h)` |
| 108 | [Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/) | Easy | [Python](solutions/trees/0108_convert_sorted_array_to_binary_search_tree.py) | `O(n)` | `O(log n)` |
| 110 | [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) | Easy | [Python](solutions/trees/0110_balanced_binary_tree.py) | `O(n)` | `O(h)` |
| 111 | [Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/) | Easy | [Python](solutions/trees/0111_minimum_depth_of_binary_tree.py) | `O(n)` | `O(h)` |
| 112 | [Path Sum](https://leetcode.com/problems/path-sum/) | Easy | [Python](solutions/trees/0112_path_sum.py) | `O(n)` | `O(h)` |

### Dynamic Programming

| # | Problem | Difficulty | Solution | Time | Space |
| --: | --- | --- | --- | --- | --- |
| 70 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | Easy | [Python](solutions/dynamic-programming/0070_climbing_stairs.py) | `O(n)` | `O(n)` |
| 118 | [Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/) | Easy | [Python](solutions/dynamic-programming/0118_pascals_triangle.py) | `O(n^2)` | `O(1)` |
| 119 | [Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii/) | Easy | [Python](solutions/dynamic-programming/0119_pascals_triangle_ii.py) | `O(n^2)` | `O(1)` |

### Greedy

| # | Problem | Difficulty | Solution | Time | Space |
| --: | --- | --- | --- | --- | --- |
| 455 | [Assign Cookies](https://leetcode.com/problems/assign-cookies/) | Easy | [Python](solutions/greedy/0455_assign_cookies.py) | `O(n log n + m log m)` | `O(n + m)` |

### Math & Geometry

| # | Problem | Difficulty | Solution | Time | Space |
| --: | --- | --- | --- | --- | --- |
| 7 | [Reverse Integer](https://leetcode.com/problems/reverse-integer/) | Medium | [Python](solutions/math-and-geometry/0007_reverse_integer.py) | `O(log x)` | `O(1)` |
| 9 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | Easy | [Python](solutions/math-and-geometry/0009_palindrome_number.py) | `O(log x)` | `O(1)` |

### Bit Manipulation

| # | Problem | Difficulty | Solution | Time | Space |
| --: | --- | --- | --- | --- | --- |
| 67 | [Add Binary](https://leetcode.com/problems/add-binary/) | Easy | [Python](solutions/bit-manipulation/0067_add_binary.py) | `O(n)` | `O(n)` |
| 136 | [Single Number](https://leetcode.com/problems/single-number/) | Easy | [Python](solutions/bit-manipulation/0136_single_number.py) | `O(n)` | `O(1)` |

## Repository layout

```
.
├── solutions/   # one folder per topic, e.g. solutions/trees/0104_maximum_depth_of_binary_tree.py
└── tests/       # pytest cases for every solution, one file per topic
```

## Running the tests

Requires Python 3.10+.

```bash
pip install -r requirements-dev.txt
pytest
```

The tests run each solution with the names LeetCode provides without imports
(`List`, `Optional`, `deque`, `ListNode`, `TreeNode`, ...), so solution files
don't need any changes to run locally.

## Adding a solution

1. Paste the accepted submission, unchanged, into
   `solutions/<topic>/<number>_<slug>.py`. Pad the number to four digits and
   take the slug from the LeetCode URL, for example
   `solutions/arrays-and-hashing/0217_contains_duplicate.py`. New topic folders
   follow NeetCode's category names, such as `heap-priority-queue`,
   `backtracking`, or `graphs`.
2. Add a row for it to the matching table above.
3. Add a `test_<number>_<slug>` test to `tests/test_<topic>.py`.

CI fails if a solution is missing from the README, a row's link doesn't match
its file name, or a solution has no test.
