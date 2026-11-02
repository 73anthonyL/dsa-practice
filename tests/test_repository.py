"""Checks that keep the README in step with the solutions folder."""

import re
from pathlib import Path

import pytest

from scripts.promote import LANGUAGES
from tests.helpers import SOLUTIONS_DIR

ROOT = SOLUTIONS_DIR.parent
README = (ROOT / "README.md").read_text()

# Every solution file, in any language. Skips editor files like
# compile_flags.txt and dotfiles such as macOS's .DS_Store.
SOLUTIONS = sorted(
    path
    for path in SOLUTIONS_DIR.rglob("*")
    if path.suffix in LANGUAGES and not path.name.startswith(".")
)

# Every link from the README to a solution, e.g. "[C++](solutions/...)".
SOLUTION_LINK = re.compile(r"\]\((solutions/[^)]+)\)")

# A LeetCode table row, e.g.
# | 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | [Python](solutions/leetcode/...) |
LEETCODE_ROW = re.compile(
    r"^\| (\d+) \| \[[^\]]+\]\(https://leetcode\.com/problems/([a-z0-9-]+)/\) "
    r"\| (?:Easy|Medium|Hard) \| \[[^\]]+\]\((solutions/leetcode/[^)]+)\) \|",
    re.MULTILINE,
)
LEETCODE_ROWS = LEETCODE_ROW.findall(README)


def test_readme_lists_every_solution_once():
    listed = sorted(SOLUTION_LINK.findall(README))
    on_disk = sorted(path.relative_to(ROOT).as_posix() for path in SOLUTIONS)
    assert listed == on_disk


def test_every_leetcode_solution_has_a_full_row():
    listed = sorted(path for _, _, path in LEETCODE_ROWS)
    on_disk = sorted(
        path.relative_to(ROOT).as_posix()
        for path in SOLUTIONS
        if path.relative_to(SOLUTIONS_DIR).parts[0] == "leetcode"
    )
    assert listed == on_disk


@pytest.mark.parametrize(
    ("number", "slug", "path"), LEETCODE_ROWS, ids=[row[2] for row in LEETCODE_ROWS]
)
def test_leetcode_row_matches_file_name(number, slug, path):
    assert Path(path).stem == f"{int(number):04d}_{slug.replace('-', '_')}"
