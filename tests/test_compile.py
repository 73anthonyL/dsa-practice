"""Check that every C++ and Python solution compiles, unchanged, as its judge would.

LeetCode C++ solutions are compiled with tests/cpp/leetcode.h force-included,
since LeetCode provides the standard library and ListNode/TreeNode without any
#include. Solutions from other judges are complete programs and compile alone.
"""

import os
import shutil
import subprocess
from pathlib import Path

import pytest

from scripts.promote import LANGUAGES
from tests.helpers import SOLUTIONS_DIR

CPP_DIR = Path(__file__).resolve().parent / "cpp"


def _find_compiler():
    """Return the first C++ compiler that can build a trivial program."""
    for name in (os.environ.get("CXX"), "g++", "clang++"):
        compiler = name and shutil.which(name)
        if not compiler:
            continue
        probe = subprocess.run(
            [compiler, "-std=c++20", "-fsyntax-only", "-x", "c++", "-"],
            input="#include <cassert>\n#include <cmath>\n#include <vector>\nint main() {}\n",
            capture_output=True,
            text=True,
            check=False,
        )
        if probe.returncode == 0:
            return compiler
    return None


CXX = _find_compiler()

SOLUTIONS = [
    path
    for path in sorted(SOLUTIONS_DIR.rglob("*"))
    if path.suffix in LANGUAGES and not path.name.startswith(".")
]
CPP_SOLUTIONS = [path for path in SOLUTIONS if LANGUAGES[path.suffix] == "C++"]
PY_SOLUTIONS = [path for path in SOLUTIONS if LANGUAGES[path.suffix] == "Python"]


def _id(path):
    return path.relative_to(SOLUTIONS_DIR).as_posix()


@pytest.mark.skipif(CXX is None, reason="no working C++ compiler found")
@pytest.mark.parametrize("path", CPP_SOLUTIONS, ids=_id)
def test_cpp_solution_compiles(path):
    flags = ["-std=c++20", "-fsyntax-only", "-I", str(CPP_DIR / "include")]
    if path.relative_to(SOLUTIONS_DIR).parts[0] == "leetcode":
        flags += ["-include", str(CPP_DIR / "leetcode.h")]
    result = subprocess.run(
        [CXX, *flags, str(path)], capture_output=True, text=True, check=False
    )
    assert result.returncode == 0, result.stderr


@pytest.mark.parametrize("path", PY_SOLUTIONS, ids=_id)
def test_python_solution_compiles(path):
    compile(path.read_bytes(), str(path), "exec")
