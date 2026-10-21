"""Checks that keep the README and tests in step with the solutions folder."""

import re
from pathlib import Path

import pytest

from tests.helpers import SOLUTIONS_DIR

ROOT = SOLUTIONS_DIR.parent
SOLUTIONS = sorted(SOLUTIONS_DIR.glob("*/*.py"))
TEST_SOURCE = "\n".join(path.read_text() for path in (ROOT / "tests").glob("test_*.py"))

# A README table row, e.g.
# | 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | [Python](solutions/...) |
README_ROW = re.compile(
    r"^\| (\d+) \| \[[^\]]+\]\(https://leetcode\.com/problems/([a-z0-9-]+)/\) "
    r"\| (?:Easy|Medium|Hard) \| \[Python\]\((solutions/[^)]+)\) \|",
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
    assert Path(path).name == f"{int(number):04d}_{slug.replace('-', '_')}.py"


@pytest.mark.parametrize("path", SOLUTIONS, ids=lambda path: path.stem)
def test_every_solution_has_a_test(path):
    assert f"def test_{path.stem}(" in TEST_SOURCE
