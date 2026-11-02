"""Move finished solutions from workspace/ into solutions/ and list them in the README.

A workspace file is promoted once it starts with a header that names the
problem and marks it done. Use ``//`` instead of ``#`` in C++, Java and other
languages whose comments start that way:

    # problem: https://leetcode.com/problems/sum-of-left-leaves/
    # topic: trees
    # time: O(n)
    # space: O(h)
    # done

``problem`` is the problem's URL. For LeetCode, Codeforces, CSES, USACO and
AtCoder the title, difficulty or rating, and CSES category or USACO division
are looked up from it. LeetCode also accepts the problem number
(``# leetcode: 404``) and needs a NeetCode ``topic``.

Any other judge works too: give the problem's URL (or a ``platform:`` name if
it has none) plus a ``title:`` line. ``title:`` and ``topic:`` also override
what was looked up, for example when a site can't be reached.

Only the header lines, and blank lines right after them, are removed; the rest
of the file is moved byte for byte.

Usage:
    python scripts/promote.py           # promote, leave the changes uncommitted
    python scripts/promote.py --commit  # also make one commit per solution
"""

from __future__ import annotations

import argparse
import html
import json
import re
import subprocess
import sys
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORKSPACE = ROOT / "workspace"
SOLUTIONS = ROOT / "solutions"
README = ROOT / "README.md"
# Platform sections in the README go before this heading.
README_END = "## Repository layout"

# NeetCode topic folder -> README heading, in the order the tables appear.
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

CSES_CATEGORIES = [
    "Introductory Problems",
    "Sorting and Searching",
    "Dynamic Programming",
    "Graph Algorithms",
    "Range Queries",
    "Tree Algorithms",
    "Mathematics",
    "String Algorithms",
    "Geometry",
    "Advanced Techniques",
    "Sliding Window Problems",
    "Interactive Problems",
    "Bitwise Operations",
    "Construction Problems",
    "Advanced Graph Problems",
    "Counting Problems",
    "Additional Problems I",
    "Additional Problems II",
]

USACO_DIVISIONS = ["Bronze", "Silver", "Gold", "Platinum"]

# Order of the platform sections in the README; any other judge goes after.
PLATFORMS = ["LeetCode", "Codeforces", "CSES", "USACO", "AtCoder"]
# Order of the ### subsections within a platform's section.
SECTION_ORDER = {
    "LeetCode": list(TOPICS.values()),
    "CSES": CSES_CATEGORIES,
    "USACO": USACO_DIVISIONS,
}

LANGUAGES = {
    ".py": "Python",
    ".cpp": "C++",
    ".cc": "C++",
    ".c": "C",
    ".java": "Java",
    ".kt": "Kotlin",
    ".cs": "C#",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".go": "Go",
    ".rs": "Rust",
    ".rb": "Ruby",
    ".swift": "Swift",
}

HEADER_LINE = re.compile(
    rb"^[ \t]*(?:#|//)[ \t]*"
    rb"(problem|leetcode|platform|title|topic|slug|difficulty|time|space|done)"
    rb"[ \t]*(?::[ \t]*(.*?))?[ \t]*\r?\n?$",
    re.IGNORECASE,
)


class PromoteError(Exception):
    pass


@dataclass
class Problem:
    platform: str  # the README's "## " section
    section: str | None  # the "### " subsection, if the platform has them
    folder: str  # relative to solutions/
    key: str  # starts the file name and identifies the problem, e.g. "0404"
    name: str  # rest of the file name, e.g. "sum_of_left_leaves"
    title: str
    columns: list[tuple[str, str]]  # README (column, cell) pairs before Solution

    @property
    def stem(self) -> str:
        return f"{self.key}_{self.name}" if self.key else self.name


def slugify(text: str, sep: str = "_") -> str:
    return re.sub(r"[^a-z0-9]+", sep, text.lower()).strip(sep)


def link(text: str, url: str | None) -> str:
    text = text.replace("|", "\\|")
    return f"[{text}]({url})" if url else text


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


# --- Looking problems up -----------------------------------------------------


def fetch(url: str, payload: dict | None = None) -> str:
    """GET a page, or POST ``payload`` as JSON, and return the response body."""
    headers = {"User-Agent": "Mozilla/5.0", "Referer": url}
    body = None
    if payload is not None:
        headers["Content-Type"] = "application/json"
        body = json.dumps(payload)
    try:
        request = urllib.request.Request(
            url, data=body.encode() if body else None, headers=headers
        )
        with urllib.request.urlopen(request, timeout=30) as response:
            return response.read().decode()
    except OSError:  # URLError, HTTPError, timeouts
        pass
    # Some Python installs (e.g. python.org's on macOS) ship without CA
    # certificates; curl uses the system's.
    args = ["curl", "-sSfL", "-m", "30"]
    for key, value in headers.items():
        args += ["-H", f"{key}: {value}"]
    if body:
        args += ["-d", body]
    try:
        return subprocess.run(
            [*args, url], check=True, capture_output=True, text=True
        ).stdout
    except (OSError, subprocess.CalledProcessError) as error:
        detail = (getattr(error, "stderr", "") or "").strip() or error
        raise PromoteError(
            f"couldn't load {url} ({detail}); add a 'title:' line (and 'topic:' "
            "where needed) to skip the lookup"
        ) from error


def first(pattern: str, text: str) -> str | None:
    match = re.search(pattern, text, re.DOTALL)
    return html.unescape(match[1]).strip() if match else None


def leetcode(ref: str, fields: dict[str, str]) -> Problem:
    topic = fields.get("topic", "")
    if topic not in TOPICS:
        raise PromoteError(
            f"LeetCode needs a NeetCode topic, not {topic!r}; use one of: "
            + ", ".join(TOPICS)
        )
    slug_match = re.search(r"leetcode\.(?:com|cn)/problems/([a-z0-9-]+)", ref)
    if ref.isdigit() and all(fields.get(k) for k in ("title", "slug", "difficulty")):
        number, title = int(ref), fields["title"]
        slug, difficulty = fields["slug"], fields["difficulty"]
    else:
        if slug_match:
            query = """query($slug: String!) { question(titleSlug: $slug) {
                questionFrontendId title titleSlug difficulty } }"""
            variables = {"slug": slug_match[1]}
        elif ref.isdigit():
            query = """query($keywords: String) { questionList(categorySlug: "",
                limit: 100, skip: 0, filters: {searchKeywords: $keywords}) {
                data { questionFrontendId title titleSlug difficulty } } }"""
            variables = {"keywords": ref}
        else:
            raise PromoteError(f"{ref!r} isn't a LeetCode problem URL or number")
        payload = {"query": query, "variables": variables}
        try:
            data = json.loads(fetch("https://leetcode.com/graphql", payload))["data"]
            questions = (
                [data["question"]] if slug_match else data["questionList"]["data"]
            )
        except (ValueError, KeyError, TypeError) as error:
            raise PromoteError(f"unexpected reply from LeetCode ({error})") from None
        question = next(
            (
                q
                for q in questions
                if q and (slug_match or q["questionFrontendId"] == ref)
            ),
            None,
        )
        if question is None:
            raise PromoteError(f"LeetCode has no problem {ref}")
        number, title = int(question["questionFrontendId"]), question["title"]
        slug, difficulty = question["titleSlug"], question["difficulty"]

    difficulty = difficulty.capitalize()
    if difficulty not in ("Easy", "Medium", "Hard"):
        raise PromoteError(f"difficulty {difficulty!r} isn't Easy, Medium or Hard")
    if not re.fullmatch(r"[a-z0-9-]+", slug):
        raise PromoteError(f"slug {slug!r} should look like 'sum-of-left-leaves'")
    return Problem(
        platform="LeetCode",
        section=TOPICS[topic],
        folder=f"leetcode/{topic}",
        key=f"{number:04d}",
        name=slug.replace("-", "_"),
        title=title,
        columns=[
            ("#", str(number)),
            ("Problem", link(title, f"https://leetcode.com/problems/{slug}/")),
            ("Difficulty", difficulty),
        ],
    )


def codeforces(match: re.Match, fields: dict[str, str]) -> Problem:
    kind, contest, index = match[1], match[2], match[3].upper()
    gym = kind == "gym"
    url = (
        f"https://codeforces.com/gym/{contest}/problem/{index}"
        if gym
        else f"https://codeforces.com/problemset/problem/{contest}/{index}"
    )
    title, rating = fields.get("title"), None
    if not title:
        if gym:
            raise PromoteError("add a 'title:' line; gym problems can't be looked up")
        try:
            reply = json.loads(fetch("https://codeforces.com/api/problemset.problems"))
            problems = reply["result"]["problems"]
        except (ValueError, KeyError, TypeError) as error:
            raise PromoteError(f"unexpected reply from Codeforces ({error})") from None
        found = next(
            (
                p
                for p in problems
                if str(p["contestId"]) == contest and p["index"] == index
            ),
            None,
        )
        if found is None:
            raise PromoteError(f"Codeforces has no problem {contest}{index}")
        title, rating = found["name"], found.get("rating")
    return Problem(
        platform="Codeforces",
        section=None,
        folder="codeforces",
        key=f"{contest}{index}",
        name=slugify(title),
        title=title,
        columns=[
            ("Problem", link(f"{contest}{index} - {title}", url)),
            ("Rating", str(rating) if rating else "—"),
        ],
    )


def cses(match: re.Match, fields: dict[str, str]) -> Problem:
    task = match[1]
    url = f"https://cses.fi/problemset/task/{task}"
    title, category = fields.get("title"), fields.get("topic")
    if not (title and category):
        page = fetch(url)
        title = title or first(r"<h1>(.*?)</h1>", page)
        category = category or first(r"<h4>(.*?)</h4>", page)
        if not (title and category):
            raise PromoteError(f"couldn't find the title and category on {url}")
    return Problem(
        platform="CSES",
        section=category,
        folder=f"cses/{slugify(category, '-')}",
        key=task,
        name=slugify(title),
        title=title,
        columns=[("Problem", link(title, url))],
    )


def usaco(match: re.Match, fields: dict[str, str]) -> Problem:
    cpid = match[1]
    url = f"https://usaco.org/index.php?page=viewproblem2&cpid={cpid}"
    title, division, contest = fields.get("title"), fields.get("topic"), "—"
    if not (title and division):
        page = fetch(url)
        headings = re.findall(r"<h2>\s*(.*?)\s*</h2>", page, re.DOTALL)
        for heading in map(html.unescape, headings):
            if found := re.match(r"USACO (\d{4}) (.+?)(?: Contest)?, (\w+)", heading):
                contest = f"{found[1]} {found[2]}"
                division = division or found[3]
            elif found := re.match(r"Problem \d+\.\s*(.+)", heading):
                # Older problems end in e.g. "(Bronze Level)".
                title = title or re.sub(r"\s*\(\w+ Level\)$", "", found[1])
        if not (title and division):
            raise PromoteError(f"couldn't find the title and division on {url}")
    return Problem(
        platform="USACO",
        section=division,
        folder=f"usaco/{slugify(division, '-')}",
        key=cpid,
        name=slugify(title),
        title=title,
        columns=[("Contest", contest), ("Problem", link(title, url))],
    )


def atcoder(match: re.Match, fields: dict[str, str]) -> Problem:
    contest, task = match[1], match[2]
    url = f"https://atcoder.jp/contests/{contest}/tasks/{task}"
    title = fields.get("title") or first(r"<title>(.*?)</title>", fetch(url))
    if not title:
        raise PromoteError(f"couldn't find the title on {url}")
    return Problem(
        platform="AtCoder",
        section=None,
        folder="atcoder",
        key=task,
        # "A - N-choice question" -> "n_choice_question"
        name=slugify(title.split(" - ", 1)[-1]),
        title=title,
        columns=[("Problem", link(f"{contest.upper()} {title}", url))],
    )


def other_judge(ref: str, fields: dict[str, str]) -> Problem:
    url = ref if ref.startswith(("http://", "https://")) else None
    platform = fields.get("platform")
    if not platform and url:
        host = (urllib.parse.urlparse(url).hostname or "").removeprefix("www.")
        parts = host.split(".")
        platform = (parts[-2] if len(parts) > 1 else parts[0]).capitalize()
    if not platform:
        raise PromoteError("'problem:' should be the problem's URL")
    title = fields.get("title")
    if not title:
        raise PromoteError(f"add a 'title:' line; {platform} problems aren't looked up")
    return Problem(
        platform=platform,
        section=None,
        folder=slugify(platform, "-"),
        key="",
        name=slugify(title),
        title=title,
        columns=[("Problem", link(title, url))],
    )


JUDGES = [
    (
        re.compile(
            r"codeforces\.com/(problemset/problem|contest|gym)/(\d+)/(?:problem/)?"
            r"([A-Za-z]\d*)\b"
        ),
        codeforces,
    ),
    (re.compile(r"cses\.fi/\w+/task/(\d+)"), cses),
    (re.compile(r"usaco\.org/.*[?&]cpid=(\d+)"), usaco),
    (re.compile(r"atcoder\.jp/contests/([\w-]+)/tasks/(\w+)"), atcoder),
]


def identify(fields: dict[str, str]) -> Problem:
    ref = fields.get("problem") or fields.get("leetcode") or ""
    if "leetcode" in fields or ref.isdigit() or "leetcode." in ref:
        return leetcode(ref, fields)
    for pattern, judge in JUDGES:
        if match := pattern.search(ref):
            problem = judge(match, fields)
            if fields.get("topic") and problem.platform not in SECTION_ORDER:
                raise PromoteError(f"'topic:' isn't used for {problem.platform}")
            return problem
    if fields.get("topic"):
        raise PromoteError("'topic:' isn't used for this judge")
    return other_judge(ref, fields)


# --- Updating the README -----------------------------------------------------


def sort_key(row: str) -> list:
    """Natural sort on the linked file name: 0094 < 0404, 999A < 1352A."""
    match = re.search(r"\]\((solutions/[^)]+)\)", row)
    stem = Path(match[1]).stem.lower() if match else row
    return [int(part) if part.isdigit() else part for part in re.split(r"(\d+)", stem)]


def table_header(columns: list[str]) -> list[str]:
    return [
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join("--:" if c == "#" else "---" for c in columns) + " |",
    ]


def next_heading(lines: list[str], start: int, prefixes: tuple[str, ...]) -> int:
    i = start + 1
    while i < len(lines) and not lines[i].startswith(prefixes):
        i += 1
    return i


def add_readme_row(readme: str, problem: Problem, header: list[str], row: str) -> str:
    """Insert a row into the problem's table, creating sections as needed."""
    lines = readme.split("\n")
    if README_END not in lines:
        raise PromoteError(f"README.md has no {README_END!r} heading")

    # The platform's "## " section.
    h2 = f"## {problem.platform}"
    if h2 in lines:
        start = lines.index(h2)
    else:
        platform = problem.platform
        later = (
            PLATFORMS[PLATFORMS.index(platform) + 1 :] if platform in PLATFORMS else []
        )
        start = next(
            (
                i
                for i, line in enumerate(lines)
                if line.startswith("## ") and line[3:] in later
            ),
            lines.index(README_END),
        )
        lines[start:start] = [h2, ""]
    end = next_heading(lines, start, ("## ",))

    # The "### " subsection within it, if this platform has them.
    if problem.section:
        h3 = f"### {problem.section}"
        if h3 in lines[start:end]:
            start = lines.index(h3, start, end)
            end = next_heading(lines, start, ("## ", "### "))
        else:
            order = SECTION_ORDER.get(problem.platform, [])
            section = problem.section
            later = order[order.index(section) + 1 :] if section in order else []
            at = next(
                (
                    i
                    for i in range(start, end)
                    if lines[i].startswith("### ") and lines[i][4:] in later
                ),
                end,
            )
            lines[at:at] = [h3, "", *header, row, ""]
            return "\n".join(lines)

    # The table itself, kept sorted.
    table = next((i for i in range(start, end) if lines[i].startswith("|")), None)
    if table is None:
        lines[end:end] = [*header, row, ""]
        return "\n".join(lines)
    i = table + 2
    while i < len(lines) and lines[i].startswith("|"):
        if sort_key(lines[i]) > sort_key(row):
            break
        i += 1
    lines.insert(i, row)
    return "\n".join(lines)


# --- Promoting a file --------------------------------------------------------


def git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args], cwd=ROOT, check=True, capture_output=True, text=True
    )
    return result.stdout.strip()


def promote(src: Path, fields: dict[str, str], code: bytes, commit: bool) -> str:
    if src.suffix not in LANGUAGES:
        raise PromoteError(
            f"unsupported file type {src.suffix!r}; add it to LANGUAGES "
            "in scripts/promote.py"
        )
    time, space = (fields.get(key, "").strip("`") for key in ("time", "space"))
    if not time or not space:
        raise PromoteError("header needs 'time:' and 'space:' complexities")
    problem = identify(fields)

    platform_dir = SOLUTIONS / problem.folder.split("/")[0]
    pattern = f"{problem.key}_*" if problem.key else problem.stem
    existing = [p for p in platform_dir.rglob(pattern + src.suffix)]
    if existing:
        raise PromoteError(f"{existing[0].relative_to(ROOT)} already exists")
    dst = SOLUTIONS / problem.folder / f"{problem.stem}{src.suffix}"
    rel_src = src.relative_to(ROOT).as_posix()
    rel_dst = dst.relative_to(ROOT).as_posix()

    columns = [*problem.columns, ("Solution", f"[{LANGUAGES[src.suffix]}]({rel_dst})")]
    columns += [("Time", f"`{time}`"), ("Space", f"`{space}`")]
    header = table_header([name for name, _ in columns])
    row = "| " + " | ".join(cell for _, cell in columns) + " |"
    original_readme, original_src = README.read_bytes(), src.read_bytes()
    readme = add_readme_row(original_readme.decode(), problem, header, row)

    created = [d for d in [dst.parent, *dst.parent.parents] if not d.exists()]
    try:
        dst.parent.mkdir(parents=True, exist_ok=True)
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
            key = f" {problem.key}" if problem.key else ""
            message = f"Add {problem.platform}{key} {problem.title}"
            author_args = ["--author", author] if author else []
            git("commit", "-q", "-m", message, *author_args)
    except (OSError, subprocess.CalledProcessError) as error:
        # Put everything back so the file can simply be promoted again.
        if commit:
            subprocess.run(["git", "reset", "-q"], cwd=ROOT, check=False)
        README.write_bytes(original_readme)
        src.write_bytes(original_src)
        dst.unlink(missing_ok=True)
        for folder in created:  # deepest first
            folder.rmdir()
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
