# Data Structures & Algorithms

[![CI](https://github.com/73anthonyL/dsa-practice/actions/workflows/ci.yml/badge.svg)](https://github.com/73anthonyL/dsa-practice/actions/workflows/ci.yml)
![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)

My solutions to LeetCode and competitive programming problems (Codeforces,
CSES, USACO, AtCoder, ...), in Python, C++ and other languages. Every solution
is kept exactly as submitted to its judge.

Space complexity excludes the output. `h` is the height of the tree.

## LeetCode

Organized by topic along the [NeetCode roadmap](https://neetcode.io/roadmap).

### Arrays & Hashing

| # | Problem | Difficulty | Solution | Time | Space |
| --: | --- | --- | --- | --- | --- |
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | [Python](solutions/leetcode/arrays-and-hashing/0001_two_sum.py) | `O(n log n)` | `O(n)` |
| 13 | [Roman to Integer](https://leetcode.com/problems/roman-to-integer/) | Easy | [Python](solutions/leetcode/arrays-and-hashing/0013_roman_to_integer.py) | `O(n)` | `O(1)` |
| 14 | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) | Easy | [Python](solutions/leetcode/arrays-and-hashing/0014_longest_common_prefix.py) | `O(n * m)` | `O(m)` |

### Two Pointers

| # | Problem | Difficulty | Solution | Time | Space |
| --: | --- | --- | --- | --- | --- |
| 26 | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | Easy | [Python](solutions/leetcode/two-pointers/0026_remove_duplicates_from_sorted_array.py) | `O(n)` | `O(1)` |
| 27 | [Remove Element](https://leetcode.com/problems/remove-element/) | Easy | [Python](solutions/leetcode/two-pointers/0027_remove_element.py) | `O(n)` | `O(n)` |
| 88 | [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) | Easy | [Python](solutions/leetcode/two-pointers/0088_merge_sorted_array.py) | `O(m + n)` | `O(1)` |
| 125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Easy | [Python](solutions/leetcode/two-pointers/0125_valid_palindrome.py) | `O(n)` | `O(1)` |

### Sliding Window

| # | Problem | Difficulty | Solution | Time | Space |
| --: | --- | --- | --- | --- | --- |
| 3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Medium | [Python](solutions/leetcode/sliding-window/0003_longest_substring_without_repeating_characters.py) | `O(n)` | `O(min(n, k))` |
| 121 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Easy | [Python](solutions/leetcode/sliding-window/0121_best_time_to_buy_and_sell_stock.py) | `O(n)` | `O(1)` |

### Stack

| # | Problem | Difficulty | Solution | Time | Space |
| --: | --- | --- | --- | --- | --- |
| 20 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Easy | [Python](solutions/leetcode/stack/0020_valid_parentheses.py) | `O(n)` | `O(n)` |

### Binary Search

| # | Problem | Difficulty | Solution | Time | Space |
| --: | --- | --- | --- | --- | --- |
| 35 | [Search Insert Position](https://leetcode.com/problems/search-insert-position/) | Easy | [Python](solutions/leetcode/binary-search/0035_search_insert_position.py) | `O(log n)` | `O(1)` |
| 69 | [Sqrt(x)](https://leetcode.com/problems/sqrtx/) | Easy | [Python](solutions/leetcode/binary-search/0069_sqrtx.py) | `O(1)` | `O(1)` |

### Linked List

| # | Problem | Difficulty | Solution | Time | Space |
| --: | --- | --- | --- | --- | --- |
| 2 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | Medium | [Python](solutions/leetcode/linked-list/0002_add_two_numbers.py) | `O(max(n, m))` | `O(1)` |
| 21 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Easy | [Python](solutions/leetcode/linked-list/0021_merge_two_sorted_lists.py) | `O(n + m)` | `O(1)` |
| 83 | [Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) | Easy | [Python](solutions/leetcode/linked-list/0083_remove_duplicates_from_sorted_list.py) | `O(n)` | `O(1)` |
| 141 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Easy | [Python](solutions/leetcode/linked-list/0141_linked_list_cycle.py) | `O(n)` | `O(1)` |

### Trees

| # | Problem | Difficulty | Solution | Time | Space |
| --: | --- | --- | --- | --- | --- |
| 94 | [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) | Easy | [Python](solutions/leetcode/trees/0094_binary_tree_inorder_traversal.py) | `O(n)` | `O(h)` |
| 100 | [Same Tree](https://leetcode.com/problems/same-tree/) | Easy | [Python](solutions/leetcode/trees/0100_same_tree.py) | `O(n)` | `O(h)` |
| 101 | [Symmetric Tree](https://leetcode.com/problems/symmetric-tree/) | Easy | [Python](solutions/leetcode/trees/0101_symmetric_tree.py) | `O(n)` | `O(h)` |
| 104 | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Easy | [Python](solutions/leetcode/trees/0104_maximum_depth_of_binary_tree.py) | `O(n)` | `O(h)` |
| 108 | [Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/) | Easy | [Python](solutions/leetcode/trees/0108_convert_sorted_array_to_binary_search_tree.py) | `O(n)` | `O(log n)` |
| 110 | [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) | Easy | [Python](solutions/leetcode/trees/0110_balanced_binary_tree.py) | `O(n)` | `O(h)` |
| 111 | [Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/) | Easy | [Python](solutions/leetcode/trees/0111_minimum_depth_of_binary_tree.py) | `O(n)` | `O(h)` |
| 112 | [Path Sum](https://leetcode.com/problems/path-sum/) | Easy | [Python](solutions/leetcode/trees/0112_path_sum.py) | `O(n)` | `O(h)` |
| 404 | [Sum of Left Leaves](https://leetcode.com/problems/sum-of-left-leaves/) | Easy | [Python](solutions/leetcode/trees/0404_sum_of_left_leaves.py) | `O(n)` | `O(h)` |

### Dynamic Programming

| # | Problem | Difficulty | Solution | Time | Space |
| --: | --- | --- | --- | --- | --- |
| 70 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | Easy | [Python](solutions/leetcode/dynamic-programming/0070_climbing_stairs.py) | `O(n)` | `O(n)` |
| 118 | [Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/) | Easy | [Python](solutions/leetcode/dynamic-programming/0118_pascals_triangle.py) | `O(n^2)` | `O(1)` |
| 119 | [Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii/) | Easy | [Python](solutions/leetcode/dynamic-programming/0119_pascals_triangle_ii.py) | `O(n^2)` | `O(1)` |
| 198 | [House Robber](https://leetcode.com/problems/house-robber/) | Medium | [C++](solutions/leetcode/dynamic-programming/0198_house_robber.cpp) | `O(n)` | `O(n)` |

### Greedy

| # | Problem | Difficulty | Solution | Time | Space |
| --: | --- | --- | --- | --- | --- |
| 455 | [Assign Cookies](https://leetcode.com/problems/assign-cookies/) | Easy | [Python](solutions/leetcode/greedy/0455_assign_cookies.py) | `O(n log n + m log m)` | `O(n + m)` |

### Math & Geometry

| # | Problem | Difficulty | Solution | Time | Space |
| --: | --- | --- | --- | --- | --- |
| 7 | [Reverse Integer](https://leetcode.com/problems/reverse-integer/) | Medium | [Python](solutions/leetcode/math-and-geometry/0007_reverse_integer.py) | `O(log x)` | `O(1)` |
| 9 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | Easy | [Python](solutions/leetcode/math-and-geometry/0009_palindrome_number.py) | `O(log x)` | `O(1)` |

### Bit Manipulation

| # | Problem | Difficulty | Solution | Time | Space |
| --: | --- | --- | --- | --- | --- |
| 67 | [Add Binary](https://leetcode.com/problems/add-binary/) | Easy | [Python](solutions/leetcode/bit-manipulation/0067_add_binary.py) | `O(n)` | `O(n)` |
| 136 | [Single Number](https://leetcode.com/problems/single-number/) | Easy | [Python](solutions/leetcode/bit-manipulation/0136_single_number.py) | `O(n)` | `O(1)` |

## Repository layout

```
.
├── workspace/   # solutions in progress; finished ones are moved to solutions/
├── solutions/
│   ├── leetcode/      # by NeetCode topic, e.g. leetcode/trees/0104_maximum_depth_of_binary_tree.py
│   ├── codeforces/    # e.g. codeforces/1352A_sum_of_round_numbers.cpp
│   ├── cses/          # by category, e.g. cses/introductory-problems/1068_weird_algorithm.cpp
│   ├── usaco/         # by division, e.g. usaco/bronze/1059_do_you_know_your_abcs.cpp
│   ├── atcoder/       # e.g. atcoder/abc300_a_n_choice_question.py
│   └── <judge>/       # any other judge, e.g. kattis/hello_world.py
├── scripts/     # promote.py moves finished solutions out of workspace/
└── tests/       # README and compile checks, plus tests for some LeetCode solutions
```

## Running the tests

Requires Python 3.10+, and `g++` or `clang++` for the C++ checks.

```bash
pip install -r requirements-dev.txt
pytest
```

Every C++ and Python solution is compiled as its judge would. LeetCode and
NeetCode code is a bare `class Solution`, so the C++ checks force-include
[`tests/cpp/leetcode.h`](tests/cpp/leetcode.h), which supplies the standard
library, `using namespace std` and `ListNode`/`TreeNode`, as LeetCode does. The
Python tests likewise provide `List`, `Optional`, `deque`, `ListNode`,
`TreeNode`, and so on. Solutions from other judges are complete programs and
compile on their own; `<bits/stdc++.h>` works with clang too.

The `compile_flags.txt` files give editors that use clangd (e.g. VS Code's
clangd extension) the same setup, so pasted LeetCode C++ shows no errors.

## Adding a solution

1. Work on the problem in `workspace/`, under any file name, e.g.
   `workspace/sum_left.py` or `workspace/round.cpp`.
2. Once it's accepted, add a header to the top of the file and push. Use `//`
   instead of `#` in C++, Java, and similar languages.

   ```python
   # problem: https://leetcode.com/problems/sum-of-left-leaves/
   # topic: trees
   # time: O(n)
   # space: O(h)
   # done
   ```

   `problem` is the problem's URL:

   | Judge | Example `problem:` | Also needs |
   | --- | --- | --- |
   | LeetCode | `https://leetcode.com/problems/two-sum/` or just `1` | `topic:`, a NeetCode topic such as `trees` or `heap-priority-queue` |
   | Codeforces | `https://codeforces.com/problemset/problem/1352/A` | |
   | CSES | `https://cses.fi/problemset/task/1068` | |
   | USACO | `https://usaco.org/index.php?page=viewproblem2&cpid=1059` | |
   | AtCoder | `https://atcoder.jp/contests/abc300/tasks/abc300_a` | |
   | Anything else | its URL, or `platform: ICPC` if it has none | `title:`, plus `slug:` (the file name) if the title has no English letters or digits |

   The title, difficulty or rating, and CSES category or USACO division are
   looked up from the URL. To skip the lookup, e.g. if the site can't be
   reached, add a `title:` line, plus `topic:` for CSES or USACO, or
   `leetcode: <number>` and `difficulty:` for LeetCode.

The [Promote solutions](.github/workflows/promote.yml) workflow then removes
the header, moves the rest of the file unchanged into `solutions/`, adds its
README row, and commits it as e.g. `Add LeetCode 0404 Sum of Left Leaves`. Run
`git pull` afterwards to get that commit locally.

To do the same locally instead, run `python scripts/promote.py` (add
`--commit` to also commit). Files without `# done` are left alone.

CI fails if a solution is missing from the README, a LeetCode row doesn't
match its file name, or a C++ or Python solution doesn't compile.
