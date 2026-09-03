"""Structural checks for the 20-hour micro-course branch."""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote

REPO_ROOT = Path(__file__).resolve().parents[1]
COURSE_ROOT = REPO_ROOT / "docs" / "micro_courses"
UNIT_RE = re.compile(r"^\d{2}_[a-z0-9_]+$")
LESSON_RE = re.compile(r"^lesson_\d{2}_[a-z0-9_]+\.md$")
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")

REQUIRED_LESSON_MARKERS = (
    "预计用时：约 12 分钟",
    "## 1 分钟：",
    "## 7 分钟：本课微课程",
    "## 3 分钟：最小练习",
    "## 1 分钟：合上资料复述",
    "## 本课完成标准",
)


def unit_dirs() -> list[Path]:
    return sorted(
        path
        for path in COURSE_ROOT.iterdir()
        if path.is_dir() and UNIT_RE.fullmatch(path.name)
    )


def lesson_files() -> list[Path]:
    return [
        path
        for unit_dir in unit_dirs()
        for path in sorted(unit_dir.iterdir())
        if path.is_file() and LESSON_RE.fullmatch(path.name)
    ]


def test_ten_units_and_one_hundred_lessons() -> None:
    units = unit_dirs()
    assert len(units) == 10, f"expected 10 units, found {len(units)}"

    counts = {unit.name: len(list(unit.glob("lesson_*.md"))) for unit in units}
    assert all(count == 10 for count in counts.values()), counts
    assert len(lesson_files()) == 100


def test_every_lesson_has_complete_micro_learning_loop() -> None:
    failures: dict[str, list[str]] = {}

    for path in lesson_files():
        text = path.read_text(encoding="utf-8")
        missing = [marker for marker in REQUIRED_LESSON_MARKERS if marker not in text]
        if missing:
            failures[str(path.relative_to(REPO_ROOT))] = missing

    assert not failures, failures


def test_every_unit_has_readme_and_workbook() -> None:
    missing: list[str] = []
    for unit in unit_dirs():
        for filename in ("README.md", "workbook.md"):
            if not (unit / filename).is_file():
                missing.append(str((unit / filename).relative_to(REPO_ROOT)))
    assert not missing, missing


def test_relative_markdown_links_resolve() -> None:
    failures: list[tuple[str, str]] = []
    markdown_files = [
        COURSE_ROOT / "README.md",
        COURSE_ROOT / "progress.md",
        REPO_ROOT / "MICRO_COURSE.md",
        REPO_ROOT / "README.md",
        REPO_ROOT / "docs" / "00_learning_system" / "micro_lesson_workflow.md",
        *sorted(COURSE_ROOT.rglob("*.md")),
    ]

    for path in dict.fromkeys(markdown_files):
        text = path.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK_RE.findall(text):
            target = unquote(raw_target.split("#", 1)[0].strip())
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                failures.append((str(path.relative_to(REPO_ROOT)), raw_target))

    assert not failures, failures
