"""A dependency-free basic Markdown checker used by local and CI workflows."""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from urllib.parse import unquote

MARKDOWN_LINK = re.compile(r"(?<!!)\[[^]]+\]\(([^)]+)\)")

IGNORED_PARTS = {
    ".git",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".venv",
    "build",
    "dist",
    "site-packages",
}


def markdown_files(roots: list[Path]) -> list[Path]:
    """Return sorted Markdown files below the supplied roots."""
    found: set[Path] = set()
    for root in roots:
        if root.is_file() and root.suffix.lower() == ".md":
            found.add(root)
            continue
        if root.is_dir():
            for path in root.rglob("*.md"):
                if not any(part in IGNORED_PARTS for part in path.parts):
                    found.add(path)
    return sorted(found)


def check_file(path: Path) -> list[str]:
    """Check basic formatting and local relative-link targets."""
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []

    if text and not text.endswith("\n"):
        errors.append(f"{path}: file must end with a newline")

    active_fence: tuple[str, int] | None = None
    for line_number, line in enumerate(text.splitlines(), start=1):
        if line.rstrip(" \t") != line:
            errors.append(f"{path}:{line_number}: trailing whitespace")

        stripped = line.lstrip()
        marker = ""
        if stripped.startswith("```"):
            marker = "```"
        elif stripped.startswith("~~~"):
            marker = "~~~"

        if marker:
            if active_fence is None:
                active_fence = (marker, line_number)
            elif active_fence[0] == marker:
                active_fence = None
            continue

        if active_fence is None:
            for match in MARKDOWN_LINK.finditer(line):
                raw_target = match.group(1).strip()
                # Ignore an optional Markdown title after the URL.
                target = raw_target.split(maxsplit=1)[0].strip("<>")
                if target.startswith(("#", "/", "http://", "https://", "mailto:")):
                    continue

                relative_path = unquote(target.split("#", 1)[0].split("?", 1)[0])
                if not relative_path:
                    continue
                if not (path.parent / relative_path).exists():
                    errors.append(
                        f"{path}:{line_number}: missing relative link target: {target}"
                    )

    if active_fence is not None:
        marker, line_number = active_fence
        errors.append(
            f"{path}:{line_number}: unclosed Markdown fence starting with {marker}"
        )
    return errors


def main() -> int:
    """Run the checker and return a process exit status."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        default=[Path(".")],
        help="Markdown file or directory to check (default: repository root)",
    )
    args = parser.parse_args()

    files = markdown_files(args.paths)
    errors = [error for path in files for error in check_file(path)]
    if errors:
        print("\n".join(errors))
        return 1

    print(f"Markdown check passed: {len(files)} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
