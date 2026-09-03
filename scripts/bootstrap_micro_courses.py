"""One-shot bootstrap for the 20-hour localization and mapping micro-course.

The payload is split into text files only to keep the initial GitHub API writes small.
This script validates, decodes, and materializes the final repository tree.
"""

from __future__ import annotations

import base64
import bz2
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote

REPO_ROOT = Path(__file__).resolve().parents[1]
PART_DIR = REPO_ROOT / "scripts" / ".micro_course_payload"
EXPECTED_COMPRESSED_SHA256 = "8e4bc86ee8ffde561a63331155870b1bfe8b8262f05a587f803b29874645535a"
EXPECTED_FILE_COUNT = 126
EXPECTED_LESSON_COUNT = 100

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def safe_target(relative_path: str) -> Path:
    target = (REPO_ROOT / relative_path).resolve()
    try:
        target.relative_to(REPO_ROOT)
    except ValueError as exc:
        raise RuntimeError(f"unsafe payload path: {relative_path}") from exc
    return target


def load_payload() -> dict[str, str]:
    part_paths = sorted(PART_DIR.glob("part_*.txt"))
    if len(part_paths) != 8:
        raise RuntimeError(f"expected 8 payload parts, found {len(part_paths)}")

    encoded = "".join(path.read_text(encoding="ascii").strip() for path in part_paths)
    compressed = base64.b64decode(encoded, validate=True)

    actual_sha256 = hashlib.sha256(compressed).hexdigest()
    if actual_sha256 != EXPECTED_COMPRESSED_SHA256:
        raise RuntimeError(
            "payload checksum mismatch: "
            f"expected {EXPECTED_COMPRESSED_SHA256}, got {actual_sha256}"
        )

    decoded = bz2.decompress(compressed)
    payload = json.loads(decoded.decode("utf-8"))
    if not isinstance(payload, dict) or len(payload) != EXPECTED_FILE_COUNT:
        raise RuntimeError(
            f"expected {EXPECTED_FILE_COUNT} files, got "
            f"{len(payload) if isinstance(payload, dict) else type(payload)}"
        )
    return payload


def write_payload(payload: dict[str, str]) -> None:
    for relative_path, content in payload.items():
        if not isinstance(relative_path, str) or not isinstance(content, str):
            raise TypeError("payload paths and contents must both be strings")
        target = safe_target(relative_path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")


def validate_generated_tree() -> None:
    course_root = REPO_ROOT / "docs" / "micro_courses"
    unit_dirs = sorted(
        path
        for path in course_root.iterdir()
        if path.is_dir() and re.fullmatch(r"\d{2}_[a-z0-9_]+", path.name)
    )
    if len(unit_dirs) != 10:
        raise RuntimeError(f"expected 10 units, found {len(unit_dirs)}")

    lesson_files = [
        path
        for unit_dir in unit_dirs
        for path in sorted(unit_dir.glob("lesson_*.md"))
    ]
    if len(lesson_files) != EXPECTED_LESSON_COUNT:
        raise RuntimeError(
            f"expected {EXPECTED_LESSON_COUNT} lessons, found {len(lesson_files)}"
        )

    required = (
        "预计用时：约 12 分钟",
        "## 7 分钟：本课微课程",
        "## 3 分钟：最小练习",
        "## 1 分钟：合上资料复述",
        "## 本课完成标准",
    )
    for path in lesson_files:
        text = path.read_text(encoding="utf-8")
        missing = [marker for marker in required if marker not in text]
        if missing:
            raise RuntimeError(f"{path} missing markers: {missing}")

    markdown_files = [
        REPO_ROOT / "README.md",
        REPO_ROOT / "MICRO_COURSE.md",
        REPO_ROOT / "docs" / "00_learning_system" / "micro_lesson_workflow.md",
        *sorted(course_root.rglob("*.md")),
    ]
    unresolved: list[tuple[str, str]] = []
    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        for raw_target in LINK_RE.findall(text):
            target_text = unquote(raw_target.split("#", 1)[0].strip())
            if not target_text or target_text.startswith(
                ("http://", "https://", "mailto:")
            ):
                continue
            target = (path.parent / target_text).resolve()
            if not target.exists():
                unresolved.append((str(path.relative_to(REPO_ROOT)), raw_target))
    if unresolved:
        raise RuntimeError(f"unresolved Markdown links: {unresolved[:20]}")


def main() -> None:
    payload = load_payload()
    write_payload(payload)
    validate_generated_tree()
    print(
        f"materialized {len(payload)} files, "
        f"including {EXPECTED_LESSON_COUNT} micro-lessons"
    )


if __name__ == "__main__":
    main()
