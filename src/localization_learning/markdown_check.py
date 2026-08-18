"""A dependency-free Markdown portability checker used locally and in CI."""

from __future__ import annotations

import argparse
import re
import unicodedata
from pathlib import Path
from urllib.parse import unquote

FENCE = re.compile(r"^(?P<indent> {0,3})(?P<run>`{3,}|~{3,})(?P<info>.*)$")
LEGACY_MATH_DELIMITER = re.compile(r"(?<!\\)\\(?:\(|\)|\[|\])")
LATEX_OUTSIDE_MATH = re.compile(r"(?<!\\)\\[A-Za-z]+")
MATH_ENVIRONMENT = re.compile(r"(?<!\\)\\(?P<action>begin|end)\{(?P<name>[^{}]+)\}")
UNSAFE_MATH_SPACING = re.compile(r"(?<!\\)\\[,;]")
UNSUPPORTED_GITHUB_MATH_COMMAND = re.compile(
    r"(?<!\\)\\operatorname\*?(?=\s|\{|$)"
)
LEADING_FRAME_SUPERSCRIPT = re.compile(r"^\{\}\^")
SETEXT_MARKER = re.compile(r"^[=-]+$")
INVALID_ATX_HEADING = re.compile(r"^ {0,3}#{1,6}(?=[^\s#])")
DETAILS_OPEN = re.compile(r"<details(?:\s[^>]*)?>", re.IGNORECASE)
DETAILS_CLOSE = re.compile(r"</details\s*>", re.IGNORECASE)
LINK_TARGET = re.compile(
    r'^(?P<target><[^>\n]*>|(?:\\.|[^\s])+?)'
    r'(?:\s+(?:"[^"]*"|\'[^\']*\'|\([^)]*\)))?$'
)

MASK = "\ue000"
INVALID_WHITESPACE = {
    "\u00a0": "non-breaking space",
    "\u200b": "zero-width space",
    "\ufeff": "byte-order mark",
}

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


def _is_escaped(text: str, index: int) -> bool:
    """Return whether the character at *index* follows an odd backslash run."""
    backslashes = 0
    index -= 1
    while index >= 0 and text[index] == "\\":
        backslashes += 1
        index -= 1
    return backslashes % 2 == 1


def _mask_range(characters: list[str], start: int, end: int) -> None:
    """Hide Markdown syntax while preserving positions and non-space boundaries."""
    characters[start:end] = [MASK] * (end - start)


def _mask_inline_code(line: str) -> tuple[str, bool]:
    """Mask same-line CommonMark code spans and report an unmatched opener."""
    characters = list(line)
    index = 0
    while index < len(line):
        if line[index] != "`" or _is_escaped(line, index):
            index += 1
            continue

        run_end = index + 1
        while run_end < len(line) and line[run_end] == "`":
            run_end += 1
        run_length = run_end - index

        search = run_end
        closing_end: int | None = None
        while search < len(line):
            if line[search] != "`" or _is_escaped(line, search):
                search += 1
                continue
            candidate_end = search + 1
            while candidate_end < len(line) and line[candidate_end] == "`":
                candidate_end += 1
            if candidate_end - search == run_length:
                closing_end = candidate_end
                break
            search = candidate_end

        if closing_end is None:
            _mask_range(characters, index, len(line))
            return "".join(characters), True

        _mask_range(characters, index, closing_end)
        index = closing_end

    return "".join(characters), False


def _unescaped_dollar_positions(text: str) -> list[int]:
    return [
        index
        for index, character in enumerate(text)
        if character == "$" and not _is_escaped(text, index)
    ]


def _is_word_character(character: str) -> bool:
    """Treat Latin letters, CJK characters, numbers and underscores as words."""
    return character == "_" or unicodedata.category(character)[0] in {"L", "N"}


def _balanced_braces(expression: str) -> bool:
    depth = 0
    for index, character in enumerate(expression):
        if _is_escaped(expression, index):
            continue
        if character == "{":
            depth += 1
        elif character == "}":
            depth -= 1
            if depth < 0:
                return False
    return depth == 0


def _balanced_environments(expression: str) -> bool:
    stack: list[str] = []
    for match in MATH_ENVIRONMENT.finditer(expression):
        action = match.group("action")
        name = match.group("name")
        if action == "begin":
            stack.append(name)
        elif not stack or stack.pop() != name:
            return False
    return not stack


def _mask_inline_math(line: str) -> tuple[str, list[str]]:
    """Mask valid inline math and return portability errors for the line."""
    characters = list(line)
    errors: list[str] = []
    positions = _unescaped_dollar_positions(line)

    double_dollar = any(
        right == left + 1 for left, right in zip(positions, positions[1:])
    )
    if double_dollar:
        errors.append("display math delimiter must be on a line by itself")
        for position in positions:
            characters[position] = MASK
        return "".join(characters), errors

    if len(positions) % 2:
        errors.append(
            "unpaired inline math delimiter; use a complete $...$ pair on one line"
        )
        # Hide the incomplete expression so that its LaTeX is not reported twice.
        _mask_range(characters, positions[-1], len(line))
        positions = positions[:-1]

    for opening, closing in zip(positions[0::2], positions[1::2]):
        expression = line[opening + 1 : closing]
        if not expression:
            errors.append("empty inline math expression")
        elif expression[0].isspace() or expression[-1].isspace():
            errors.append("inline math must not contain boundary whitespace")

        if opening > 0 and not line[opening - 1].isspace():
            errors.append(
                "inline math opening delimiter must be preceded by whitespace"
            )
        if closing + 1 < len(line) and _is_word_character(line[closing + 1]):
            errors.append(
                "inline math closing delimiter touches following text"
            )

        if not _balanced_braces(expression):
            errors.append("unbalanced braces in inline math expression")
        if not _balanced_environments(expression):
            errors.append("unbalanced LaTeX environment in inline math expression")
        if UNSAFE_MATH_SPACING.search(expression):
            errors.append(
                r"unsafe LaTeX spacing command; do not use \, or \; on GitHub"
            )
        if UNSUPPORTED_GITHUB_MATH_COMMAND.search(expression):
            errors.append(
                r"unsupported GitHub math command: do not use \operatorname "
                r"or \operatorname*"
            )
        if LEADING_FRAME_SUPERSCRIPT.match(expression.lstrip()):
            errors.append(
                "inline math beginning with {}^{...} is unreliable on GitHub; "
                "use a $$ display math block"
            )
        _mask_range(characters, opening, closing + 1)

    return "".join(characters), errors


def _find_closing_bracket(text: str, opening: int) -> int | None:
    depth = 1
    for index in range(opening + 1, len(text)):
        if _is_escaped(text, index):
            continue
        if text[index] == "[":
            depth += 1
        elif text[index] == "]":
            depth -= 1
            if depth == 0:
                return index
    return None


def _find_closing_parenthesis(text: str, opening: int) -> int | None:
    depth = 1
    angle_destination = opening + 1 < len(text) and text[opening + 1] == "<"
    for index in range(opening + 1, len(text)):
        if _is_escaped(text, index):
            continue
        if angle_destination and text[index] == ">":
            angle_destination = False
            continue
        if angle_destination:
            continue
        if text[index] == "(":
            depth += 1
        elif text[index] == ")":
            depth -= 1
            if depth == 0:
                return index
    return None


def _relative_target_error(path: Path, target: str) -> str | None:
    target = target.replace("\\(", "(").replace("\\)", ")")
    if target.startswith(("#", "/")) or re.match(
        r"^[A-Za-z][A-Za-z0-9+.-]*:", target
    ):
        return None

    relative_path = unquote(target.split("#", 1)[0].split("?", 1)[0])
    if relative_path and not (path.parent / relative_path).exists():
        return f"missing relative link target: {target}"
    return None


def _mask_links(line: str, path: Path) -> tuple[str, list[str]]:
    """Validate inline links and images, and mask their destinations."""
    characters = list(line)
    errors: list[str] = []
    index = 0

    while index < len(line):
        if line[index] != "[" or _is_escaped(line, index):
            index += 1
            continue

        image = index > 0 and line[index - 1] == "!" and not _is_escaped(
            line, index - 1
        )
        closing_bracket = _find_closing_bracket(line, index)
        if closing_bracket is None:
            if image or "(" in line[index + 1 :]:
                errors.append("malformed Markdown link or image: missing ]")
            break

        destination_opening = closing_bracket + 1
        if destination_opening < len(line) and line[destination_opening].isspace():
            probe = destination_opening
            while probe < len(line) and line[probe].isspace():
                probe += 1
            if probe < len(line) and line[probe] == "(":
                errors.append("link label and destination must not be separated")
                destination_opening = probe

        if (
            destination_opening >= len(line)
            or line[destination_opening] != "("
        ):
            index = closing_bracket + 1
            continue

        destination_closing = _find_closing_parenthesis(line, destination_opening)
        if destination_closing is None:
            errors.append("malformed Markdown link or image: missing )")
            _mask_range(characters, destination_opening, len(line))
            break

        raw = line[destination_opening + 1 : destination_closing].strip()
        if not raw:
            errors.append("Markdown link or image has an empty target")
        else:
            target_match = LINK_TARGET.fullmatch(raw)
            if target_match is None:
                errors.append("malformed Markdown link or image target")
            else:
                target = target_match.group("target").strip("<>")
                target_error = _relative_target_error(path, target)
                if target_error:
                    errors.append(target_error)

        if image and closing_bracket == index + 1:
            errors.append("Markdown image must have non-empty alt text")

        _mask_range(
            characters,
            closing_bracket + 1,
            destination_closing + 1,
        )
        index = destination_closing + 1

    return "".join(characters), errors


def _strong_emphasis_errors(line: str) -> list[str]:
    """Check the repository's portable ``**text**`` convention."""
    positions: list[int] = []
    index = 0
    while index < len(line):
        if line[index] != "*" or _is_escaped(line, index):
            index += 1
            continue
        run_end = index + 1
        while run_end < len(line) and line[run_end] == "*":
            run_end += 1
        if run_end - index == 2:
            positions.append(index)
        index = run_end

    errors: list[str] = []
    if len(positions) % 2:
        errors.append("unpaired ** strong-emphasis delimiter")

    for opening, closing in zip(positions[0::2], positions[1::2]):
        content = line[opening + 2 : closing]
        if not content:
            errors.append("empty ** strong-emphasis span")
        elif content[0].isspace() or content[-1].isspace():
            errors.append("** strong emphasis must not contain boundary whitespace")

        if opening > 0 and _is_word_character(line[opening - 1]):
            errors.append("opening ** delimiter touches surrounding text")
        if closing + 2 < len(line) and _is_word_character(line[closing + 2]):
            errors.append("closing ** delimiter touches surrounding text")

    return errors


def _display_math_line_errors(
    line: str,
    brace_depth: int,
    environments: list[str],
) -> tuple[int, list[str]]:
    errors: list[str] = []
    if UNSAFE_MATH_SPACING.search(line):
        errors.append(r"unsafe LaTeX spacing command; do not use \, or \; on GitHub")
    if UNSUPPORTED_GITHUB_MATH_COMMAND.search(line):
        errors.append(
            r"unsupported GitHub math command: do not use \operatorname "
            r"or \operatorname*"
        )
    for index, character in enumerate(line):
        if _is_escaped(line, index):
            continue
        if character == "{":
            brace_depth += 1
        elif character == "}":
            brace_depth -= 1
            if brace_depth < 0:
                errors.append("unexpected } in display math block")
                brace_depth = 0

    for match in MATH_ENVIRONMENT.finditer(line):
        action = match.group("action")
        name = match.group("name")
        if action == "begin":
            environments.append(name)
        elif not environments or environments[-1] != name:
            errors.append(f"mismatched \\end{{{name}}} in display math block")
        else:
            environments.pop()
    return brace_depth, errors


def check_file(path: Path) -> list[str]:
    """Check portable Markdown syntax and local relative-link targets."""
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []

    if text and not text.endswith("\n"):
        errors.append(f"{path}: file must end with a newline")

    active_fence: tuple[str, int, int, str] | None = None
    display_math_start: int | None = None
    display_brace_depth = 0
    display_has_content = False
    display_environments: list[str] = []
    details_depth = 0
    lines = text.splitlines()

    for line_number, line in enumerate(lines, start=1):
        if line.rstrip(" \t") != line:
            errors.append(f"{path}:{line_number}: trailing whitespace")

        fence_match = FENCE.match(line)
        if active_fence is not None:
            character, length, _, _ = active_fence
            if fence_match:
                run = fence_match.group("run")
                if (
                    run[0] == character
                    and len(run) >= length
                    and not fence_match.group("info").strip()
                ):
                    active_fence = None
            continue

        if fence_match:
            run = fence_match.group("run")
            info = fence_match.group("info")
            if not info.strip():
                errors.append(
                    f"{path}:{line_number}: opening code fence must name a language"
                )
            if run[0] == "`" and "`" in info:
                errors.append(
                    f"{path}:{line_number}: backtick fence info string "
                    "must not contain backticks"
                )
            active_fence = (run[0], len(run), line_number, run)
            continue

        code_masked, unclosed_code = _mask_inline_code(line)
        if unclosed_code:
            errors.append(f"{path}:{line_number}: unclosed inline code span")

        details_depth += len(DETAILS_OPEN.findall(code_masked))
        details_depth = max(
            0,
            details_depth - len(DETAILS_CLOSE.findall(code_masked)),
        )

        if "\t" in code_masked:
            errors.append(f"{path}:{line_number}: tab outside a code fence or span")
        for character, name in INVALID_WHITESPACE.items():
            if character in code_masked:
                errors.append(f"{path}:{line_number}: forbidden {name}")

        if INVALID_ATX_HEADING.match(code_masked):
            errors.append(
                f"{path}:{line_number}: ATX heading marker must be followed by a space"
            )

        legacy_delimiters = LEGACY_MATH_DELIMITER.findall(code_masked)
        if legacy_delimiters:
            rendered = ", ".join(f"`{item}`" for item in legacy_delimiters)
            errors.append(
                f"{path}:{line_number}: unsupported GitHub math delimiter(s): "
                f"{rendered}; use $...$ or $$...$$"
            )

        if code_masked.strip() == "$$":
            if code_masked != "$$":
                errors.append(
                    f"{path}:{line_number}: display math delimiter must start "
                    "at column 1"
                )
            if display_math_start is None:
                if details_depth:
                    errors.append(
                        f"{path}:{line_number}: display math inside <details> "
                        "is unreliable on GitHub; move it outside the collapsible "
                        "section"
                    )
                if line_number > 1 and lines[line_number - 2].strip():
                    errors.append(
                        f"{path}:{line_number}: display math block must have a "
                        "blank line before it"
                    )
                display_math_start = line_number
                display_brace_depth = 0
                display_has_content = False
                display_environments = []
            else:
                if not display_has_content:
                    errors.append(
                        f"{path}:{display_math_start}: empty display math block"
                    )
                if display_brace_depth:
                    errors.append(
                        f"{path}:{display_math_start}: unbalanced braces in display "
                        "math block"
                    )
                if display_environments:
                    environments = ", ".join(display_environments)
                    errors.append(
                        f"{path}:{display_math_start}: unclosed LaTeX environment(s) "
                        f"in display math block: {environments}"
                    )
                if line_number < len(lines) and lines[line_number].strip():
                    errors.append(
                        f"{path}:{line_number}: display math block must have a "
                        "blank line after it"
                    )
                display_math_start = None
            continue

        if display_math_start is not None:
            if code_masked.strip():
                display_has_content = True
            if SETEXT_MARKER.fullmatch(code_masked.strip()):
                errors.append(
                    f"{path}:{line_number}: standalone Markdown heading marker "
                    "inside $$ block; keep the operator on an equation line"
                )
            display_brace_depth, math_errors = _display_math_line_errors(
                code_masked,
                display_brace_depth,
                display_environments,
            )
            errors.extend(f"{path}:{line_number}: {error}" for error in math_errors)
            continue

        math_masked, math_errors = _mask_inline_math(code_masked)
        errors.extend(f"{path}:{line_number}: {error}" for error in math_errors)

        latex_command = LATEX_OUTSIDE_MATH.search(math_masked)
        if latex_command:
            errors.append(
                f"{path}:{line_number}: LaTeX command outside math/code: "
                f"`{latex_command.group()}`"
            )

        link_masked, link_errors = _mask_links(math_masked, path)
        errors.extend(f"{path}:{line_number}: {error}" for error in link_errors)
        errors.extend(
            f"{path}:{line_number}: {error}"
            for error in _strong_emphasis_errors(link_masked)
        )

    if active_fence is not None:
        _, _, line_number, marker = active_fence
        errors.append(
            f"{path}:{line_number}: unclosed Markdown fence starting with {marker}"
        )
    if display_math_start is not None:
        errors.append(
            f"{path}:{display_math_start}: unclosed display math block starting with $$"
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
