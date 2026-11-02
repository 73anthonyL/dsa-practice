"""Checks that keep the README in step with the solutions folder."""

import re
from pathlib import Path

import pytest

from tests.helpers import SOLUTIONS_DIR

ROOT = SOLUTIONS_DIR.parent
SOLUTIONS = sorted(path for path in SOLUTIONS_DIR.glob("*/*") if path.is_file())

# A README table row, e.g.
# | 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | [Python](solutions/...) |
# The link text is the language: Python, C++, ...
README_ROW = re.compile(
    r"^\| (\d+) \| \[[^\]]+\]\(https://leetcode\.com/problems/([a-z0-9-]+)/\) "
    r"\| (?:Easy|Medium|Hard) \| \[[^\]]+\]\((solutions/[^)]+)\) \|",
    re.MULTILINE,
)
README_ROWS = README_ROW.findall((ROOT / "README.md").read_text())


def test_readme_lists_every_solution_once():
    listed = sorted(path for _, _, path in README_ROWS)
    on_disk = sorted(path.relative_to(ROOT).as_posix() for path in SOLUTIONS)
    assert listed == on_disk


@pytest.mark.parametrize(
    ("number", "slug", "path"), README_ROWS, ids=[row[2] for row in README_ROWS]
)
def test_readme_row_matches_file_name(number, slug, path):
    assert Path(path).stem == f"{int(number):04d}_{slug.replace('-', '_')}"
