"""Move finished solutions from workspace/ into solutions/ and list them in the README.

A workspace file is promoted once it starts with a header like this one
(use ``//`` instead of ``#`` in languages such as C++):

    # leetcode: 404
    # topic: trees
    # time: O(n)
    # space: O(h)
    # done

Only the header lines (and blank lines right after them) are removed; the rest
of the file is moved byte for byte. The title, URL slug and difficulty come
from LeetCode, or from optional ``title:``, ``slug:`` and ``difficulty:`` header
lines if all three are given.

Usage:
    python scripts/promote.py           # promote, leave the changes uncommitted
    python scripts/promote.py --commit  # also make one commit per solution
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORKSPACE = ROOT / "workspace"
SOLUTIONS = ROOT / "solutions"
README = ROOT / "README.md"

# Topic folder -> README heading, in the order the tables appear in the README.
TOPICS = {
    "arrays-and-hashing": "Arrays & Hashing",
    "two-pointers": "Two Pointers",
    "sliding-window": "Sliding Window",
    "stack": "Stack",
    "binary-search": "Binary Search",
    "linked-list": "Linked List",
    "trees": "Trees",
    "tries": "Tries",
    "heap-priority-queue": "Heap / Priority Queue",
    "backtracking": "Backtracking",
    "graphs": "Graphs",
    "advanced-graphs": "Advanced Graphs",
    "dynamic-programming": "Dynamic Programming",
    "2d-dynamic-programming": "2-D Dynamic Programming",
    "greedy": "Greedy",
    "intervals": "Intervals",
    "math-and-geometry": "Math & Geometry",
    "bit-manipulation": "Bit Manipulation",
}

LANGUAGES = {
    ".py": "Python",
    ".cpp": "C++",
    ".c": "C",
    ".java": "Java",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".go": "Go",
    ".rs": "Rust",
}

HEADER_LINE = re.compile(
    rb"^[ \t]*(?:#|//)[ \t]*(leetcode|topic|time|space|title|slug|difficulty|done)"
    rb"[ \t]*(?::[ \t]*(.*?))?[ \t]*\r?\n?$",
    re.IGNORECASE,
)

TABLE_HEADER = [
    "| # | Problem | Difficulty | Solution | Time | Space |",
    "| --: | --- | --- | --- | --- | --- |",
]

QUERY = """
query($keywords: String) {
  questionList(categorySlug: "", limit: 50, skip: 0,
               filters: {searchKeywords: $keywords}) {
    data { questionFrontendId title titleSlug difficulty }
  }
}
"""


class PromoteError(Exception):
    pass


def parse_header(path: Path) -> tuple[dict[str, str], bytes] | None:
    """Split a workspace file into its header fields and its code.

    Returns None if the file isn't marked done yet.
    """
    data = path.read_bytes()
    # Some editors start files with a byte order mark; keep it on the code.
    bom = b"\xef\xbb\xbf" if data.startswith(b"\xef\xbb\xbf") else b""
    lines = data[len(bom) :].splitlines(keepends=True)
    fields: dict[str, str] = {}
    i = 0
    while i < len(lines) and (match := HEADER_LINE.match(lines[i])):
        fields[match[1].decode().lower()] = (match[2] or b"").decode().strip()
        i += 1
    if "done" not in fields:
        return None
    while i < len(lines) and not lines[i].strip():
        i += 1
    return fields, bom + b"".join(lines[i:])


def fetch_problem(number: int) -> tuple[str, str, str]:
    """Return (title, slug, difficulty) for a LeetCode problem number."""
    url = "https://leetcode.com/graphql"
    body = json.dumps({"query": QUERY, "variables": {"keywords": str(number)}})
    headers = {
        "Content-Type": "application/json",
        "Referer": "https://leetcode.com",
        "User-Agent": "Mozilla/5.0",
    }
    try:
        try:
            request = urllib.request.Request(url, data=body.encode(), headers=headers)
            with urllib.request.urlopen(request, timeout=30) as response:
                text = response.read().decode()
        except OSError:  # URLError, HTTPError, timeouts
            # Some Python installs (e.g. python.org's on macOS) ship without CA
            # certificates; curl uses the system's.
            header_args = [
                arg for k, v in headers.items() for arg in ("-H", f"{k}: {v}")
            ]
            text = subprocess.run(
                ["curl", "-sSf", "-m", "30", *header_args, "-d", body, url],
                check=True,
                capture_output=True,
                text=True,
            ).stdout
        questions = json.loads(text)["data"]["questionList"]["data"]
    except (
        OSError,
        subprocess.CalledProcessError,
        KeyError,
        TypeError,
        ValueError,
    ) as error:
        raise PromoteError(
            f"couldn't look up problem {number} on LeetCode ({error}); "
            "add 'title:', 'slug:' and 'difficulty:' lines to the header instead"
        ) from error
    for question in questions:
        if question["questionFrontendId"] == str(number):
            return question["title"], question["titleSlug"], question["difficulty"]
    raise PromoteError(f"LeetCode has no problem {number}")


def add_readme_row(readme: str, topic: str, number: int, row: str) -> str:
    """Insert a row into the topic's table, keeping it sorted by number."""
    lines = readme.split("\n")
    heading = f"### {TOPICS[topic]}"
    if heading in lines:
        i = lines.index(heading) + 1
        while not lines[i].startswith("|"):
            i += 1
        i += len(TABLE_HEADER)
        while (
            i < len(lines)
            and lines[i].startswith("|")
            and int(lines[i].split("|")[1]) <= number
        ):
            i += 1
        lines.insert(i, row)
    else:
        # New topic: add its table before the next topic that already has one.
        order = list(TOPICS)
        later = {f"### {TOPICS[t]}" for t in order[order.index(topic) + 1 :]}
        start = lines.index("## Solutions") + 1
        i = next(
            (
                j
                for j in range(start, len(lines))
                if lines[j] in later or lines[j].startswith("## ")
            ),
            len(lines),
        )
        lines[i:i] = [heading, "", *TABLE_HEADER, row, ""]
    return "\n".join(lines)


def git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args], cwd=ROOT, check=True, capture_output=True, text=True
    )
    return result.stdout.strip()


def promote(src: Path, fields: dict[str, str], code: bytes, commit: bool) -> str:
    try:
        number = int(fields.get("leetcode", ""))
    except ValueError:
        raise PromoteError("header needs 'leetcode: <problem number>'") from None
    topic = fields.get("topic", "")
    if topic not in TOPICS:
        raise PromoteError(f"unknown topic {topic!r}; use one of: {', '.join(TOPICS)}")
    time, space = (fields.get(key, "").strip("`") for key in ("time", "space"))
    if not time or not space:
        raise PromoteError("header needs 'time:' and 'space:' complexities")

    if all(fields.get(key) for key in ("title", "slug", "difficulty")):
        title, slug, difficulty = fields["title"], fields["slug"], fields["difficulty"]
    else:
        title, slug, difficulty = fetch_problem(number)
    # Match what tests/test_repository.py accepts in a README row.
    difficulty = difficulty.capitalize()
    if difficulty not in ("Easy", "Medium", "Hard"):
        raise PromoteError(f"difficulty {difficulty!r} isn't Easy, Medium or Hard")
    if not re.fullmatch(r"[a-z0-9-]+", slug):
        raise PromoteError(f"slug {slug!r} should look like 'sum-of-left-leaves'")

    existing = sorted(SOLUTIONS.glob(f"*/{number:04d}_*{src.suffix}"))
    if existing:
        raise PromoteError(f"{existing[0].relative_to(ROOT)} already exists")
    dst = SOLUTIONS / topic / f"{number:04d}_{slug.replace('-', '_')}{src.suffix}"
    rel_src, rel_dst = (
        src.relative_to(ROOT).as_posix(),
        dst.relative_to(ROOT).as_posix(),
    )

    row = (
        f"| {number} | [{title}](https://leetcode.com/problems/{slug}/) "
        f"| {difficulty} | [{LANGUAGES[src.suffix]}]({rel_dst}) "
        f"| `{time}` | `{space}` |"
    )
    original_readme, original_src = README.read_bytes(), src.read_bytes()
    readme = add_readme_row(original_readme.decode(), topic, number, row)

    new_folder = not dst.parent.exists()
    try:
        dst.parent.mkdir(exist_ok=True)
        dst.write_bytes(code)
        README.write_bytes(readme.encode())
        author = ""
        if commit:
            # Credit whoever last committed the workspace file, not the bot.
            author = git("log", "-1", "--format=%an <%ae>", "--", rel_src)
            git("rm", "-q", "--cached", "--ignore-unmatch", "--", rel_src)
        src.unlink()
        if commit:
            git("add", "--", rel_dst, "README.md")
            message = f"Add {number:04d} {title}"
            author_args = ["--author", author] if author else []
            git("commit", "-q", "-m", message, *author_args)
    except (OSError, subprocess.CalledProcessError) as error:
        # Put everything back so the file can simply be promoted again.
        if commit:
            subprocess.run(["git", "reset", "-q"], cwd=ROOT, check=False)
        README.write_bytes(original_readme)
        src.write_bytes(original_src)
        dst.unlink(missing_ok=True)
        if new_folder:
            dst.parent.rmdir()
        detail = getattr(error, "stderr", "") or error
        raise PromoteError(f"couldn't promote, nothing changed ({detail})") from error
    return f"{rel_src} -> {rel_dst}"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Promote finished workspace solutions."
    )
    parser.add_argument(
        "--commit", action="store_true", help="make one commit per solution"
    )
    args = parser.parse_args()

    if args.commit and git("status", "--porcelain", "--", "README.md"):
        print("README.md has uncommitted changes; commit them first.", file=sys.stderr)
        return 1
    if args.commit and git("diff", "--cached", "--name-only"):
        print(
            "There are staged changes; commit or unstage them first.", file=sys.stderr
        )
        return 1

    failed = promoted = 0
    for src in sorted(WORKSPACE.rglob("*")):
        if not src.is_file() or src.name.startswith("."):
            continue
        parsed = parse_header(src)
        if parsed is None:
            continue
        try:
            if src.suffix not in LANGUAGES:
                raise PromoteError(
                    f"unsupported file type {src.suffix!r}; add it to LANGUAGES "
                    "in scripts/promote.py"
                )
            print(promote(src, *parsed, commit=args.commit))
            promoted += 1
        except Exception as error:  # noqa: BLE001 -- report it, go on to the next file
            message = error if isinstance(error, PromoteError) else repr(error)
            print(f"{src.relative_to(ROOT)}: {message}", file=sys.stderr)
            failed += 1

    if not promoted and not failed:
        print("Nothing marked done in workspace/.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
