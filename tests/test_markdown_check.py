"""Tests for the dependency-free Markdown checker."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from localization_learning.markdown_check import check_file


class MarkdownCheckTest(unittest.TestCase):
    def check_text(
        self,
        text: str,
        relative_files: tuple[str, ...] = (),
    ) -> list[str]:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for relative_file in relative_files:
                target = root / relative_file
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text("target\n", encoding="utf-8")
            source = root / "source.md"
            source.write_text(text, encoding="utf-8")
            return check_file(source)

    def test_valid_relative_link(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "target.md").write_text("# Target\n", encoding="utf-8")
            source = root / "source.md"
            source.write_text("[target](target.md)\n", encoding="utf-8")

            self.assertEqual(check_file(source), [])

    def test_missing_relative_link_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source.md"
            source.write_text("[missing](missing.md)\n", encoding="utf-8")

            errors = check_file(source)

            self.assertEqual(len(errors), 1)
            self.assertIn("missing relative link target", errors[0])

    def test_links_inside_code_fences_are_ignored(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source.md"
            source.write_text(
                "```markdown\n[example](not-a-real-file.md)\n```\n",
                encoding="utf-8",
            )

            self.assertEqual(check_file(source), [])

    def test_external_and_anchor_links_are_ignored(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source.md"
            source.write_text(
                "[web](https://example.com) and [section](#section)\n",
                encoding="utf-8",
            )

            self.assertEqual(check_file(source), [])

    def test_github_math_delimiters_are_accepted(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source.md"
            source.write_text(
                "Inline $x^2$ .\n\n$$\n"
                "\\begin{bmatrix}1\\\\2\\end{bmatrix}\n"
                "$$\n",
                encoding="utf-8",
            )

            self.assertEqual(check_file(source), [])

    def test_legacy_math_delimiters_are_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source.md"
            source.write_text(
                "Inline \\(x^2\\).\n\n\\[\ny=2\n\\]\n",
                encoding="utf-8",
            )

            errors = check_file(source)

            self.assertEqual(len(errors), 3)
            self.assertTrue(
                all("unsupported GitHub math delimiter" in error for error in errors)
            )

    def test_legacy_delimiter_examples_in_inline_code_are_ignored(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source.md"
            source.write_text(
                "Do not use `\\(...\\)` or `\\[...\\]`.\n",
                encoding="utf-8",
            )

            self.assertEqual(check_file(source), [])

    def test_unpaired_inline_math_delimiter_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source.md"
            source.write_text("Inline $x^2 is incomplete.\n", encoding="utf-8")

            errors = check_file(source)

            self.assertEqual(len(errors), 1)
            self.assertIn("unpaired inline math delimiter", errors[0])

    def test_unclosed_display_math_block_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source.md"
            source.write_text("$$\nx=1\n", encoding="utf-8")

            errors = check_file(source)

            self.assertEqual(len(errors), 1)
            self.assertIn("unclosed display math block", errors[0])

    def test_empty_display_math_block_is_reported(self) -> None:
        errors = self.check_text("$$\n$$\n")

        self.assertEqual(len(errors), 1)
        self.assertIn("empty display math block", errors[0])

    def test_display_math_requires_surrounding_blank_lines(self) -> None:
        errors = self.check_text("Before\n$$\nx=1\n$$\nAfter\n")

        self.assertEqual(len(errors), 2)
        self.assertTrue(all("blank line" in error for error in errors))

    def test_setext_marker_inside_display_math_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source.md"
            source.write_text("$$\nx\n=\ny\n$$\n", encoding="utf-8")

            errors = check_file(source)

            self.assertEqual(len(errors), 1)
            self.assertIn("standalone Markdown heading marker", errors[0])

    def test_inline_code_masks_markdown_examples(self) -> None:
        errors = self.check_text(
            "Examples: `** broken`, `$x$，`, `\\mathbf T`, "
            "`[missing](none.md)` and `#bad`.\n"
        )

        self.assertEqual(errors, [])

    def test_multi_backtick_inline_code_is_supported(self) -> None:
        errors = self.check_text("Use ``a ` character`` here.\n")

        self.assertEqual(errors, [])

    def test_unclosed_inline_code_is_reported_without_cascade(self) -> None:
        errors = self.check_text("Use `** broken $x and [missing](none.md).\n")

        self.assertEqual(len(errors), 1)
        self.assertIn("unclosed inline code span", errors[0])

    def test_long_fence_can_contain_shorter_fence_and_examples(self) -> None:
        errors = self.check_text(
            "````markdown\n"
            "```\n"
            "** broken $x \\mathbf T [missing](none.md)\n"
            "```\n"
            "````\n"
        )

        self.assertEqual(errors, [])

    def test_shorter_or_different_fence_does_not_close_block(self) -> None:
        errors = self.check_text("~~~~text\n```\n~~~\n~~~~\n")

        self.assertEqual(errors, [])

    def test_opening_code_fence_requires_a_language(self) -> None:
        errors = self.check_text("```\ncontent\n```\n")

        self.assertEqual(len(errors), 1)
        self.assertIn("must name a language", errors[0])

    def test_unclosed_fence_is_reported(self) -> None:
        errors = self.check_text("```text\ncontent\n")

        self.assertEqual(len(errors), 1)
        self.assertIn("unclosed Markdown fence", errors[0])

    def test_portable_strong_emphasis_is_accepted(self) -> None:
        errors = self.check_text(
            "**结论** 之后。\n：**结论**。\n**`map` 坐标系**。\n"
        )

        self.assertEqual(errors, [])

    def test_strong_emphasis_touching_text_is_reported(self) -> None:
        errors = self.check_text(
            "前文 **结论**这篇继续。\n文本**重点**。\n"
        )

        self.assertEqual(len(errors), 2)
        self.assertTrue(all("delimiter touches surrounding text" in e for e in errors))

    def test_strong_emphasis_boundary_space_and_pairing_are_reported(self) -> None:
        errors = self.check_text("** 结论**\n**结论 **\n**未闭合\n")

        self.assertEqual(len(errors), 3)
        self.assertEqual(
            sum("boundary whitespace" in error for error in errors),
            2,
        )
        self.assertTrue(any("unpaired **" in error for error in errors))

    def test_inline_math_requires_whitespace_or_line_boundaries(self) -> None:
        errors = self.check_text("位置 $x$，继续；以及：$y$。\n$x$\n")

        self.assertEqual(len(errors), 1)
        self.assertTrue(all("must be" in error for error in errors))

    def test_inline_math_with_portable_spacing_is_accepted(self) -> None:
        errors = self.check_text(
            "位置 $x$，变换 ${}^{A}\\mathbf T_B$。\n"
        )

        self.assertEqual(errors, [])

    def test_inline_math_closing_delimiter_must_not_touch_text(self) -> None:
        errors = self.check_text("位置 $x$继续变化。\n")

        self.assertEqual(len(errors), 1)
        self.assertIn("touches following text", errors[0])

    def test_inline_math_boundary_whitespace_is_reported(self) -> None:
        errors = self.check_text("Bad $ x$ and $x $ expressions.\n")

        self.assertEqual(len(errors), 2)
        self.assertTrue(all("boundary whitespace" in error for error in errors))

    def test_inline_math_braces_are_checked(self) -> None:
        errors = self.check_text("Bad $x_{i$ expression.\n")

        self.assertEqual(len(errors), 1)
        self.assertIn("unbalanced braces", errors[0])

    def test_inline_display_math_is_reported(self) -> None:
        errors = self.check_text("Bad $$x=1$$ block.\n")

        self.assertEqual(len(errors), 1)
        self.assertIn("line by itself", errors[0])

    def test_unsafe_math_spacing_commands_are_reported(self) -> None:
        errors = self.check_text(
            "Inline $2\\,\\mathrm{h}$ .\n\n$$\na\\;b\n$$\n"
        )

        self.assertEqual(len(errors), 2)
        self.assertTrue(all("unsafe LaTeX spacing command" in e for e in errors))

    def test_latex_command_outside_math_is_reported(self) -> None:
        errors = self.check_text("The value is \\mathbf T.\n")

        self.assertEqual(len(errors), 1)
        self.assertIn("LaTeX command outside math/code", errors[0])

    def test_escaped_currency_dollar_is_accepted(self) -> None:
        errors = self.check_text("The price is \\$100.\n")

        self.assertEqual(errors, [])

    def test_relative_image_target_and_alt_text_are_checked(self) -> None:
        valid = self.check_text(
            "![diagram](assets/diagram.png)\n",
            ("assets/diagram.png",),
        )
        missing = self.check_text("![diagram](assets/missing.png)\n")
        empty_alt = self.check_text("![](https://example.com/image.png)\n")

        self.assertEqual(valid, [])
        self.assertEqual(len(missing), 1)
        self.assertIn("missing relative link target", missing[0])
        self.assertEqual(len(empty_alt), 1)
        self.assertIn("non-empty alt text", empty_alt[0])

    def test_malformed_links_are_reported(self) -> None:
        separated = self.check_text(
            "[target] (target.md)\n",
            ("target.md",),
        )
        unclosed = self.check_text("[target](target.md\n")
        empty = self.check_text("[target]()\n")

        self.assertTrue(any("must not be separated" in e for e in separated))
        self.assertTrue(any("missing )" in e for e in unclosed))
        self.assertTrue(any("empty target" in e for e in empty))

    def test_invalid_whitespace_and_heading_are_reported(self) -> None:
        errors = self.check_text("#Bad heading\nA\u00a0B\nA\u200bB\nA\tB\n")

        self.assertEqual(len(errors), 4)
        self.assertTrue(any("ATX heading" in error for error in errors))
        self.assertTrue(any("non-breaking space" in error for error in errors))
        self.assertTrue(any("zero-width space" in error for error in errors))
        self.assertTrue(any("tab outside" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
