"""Tests for the dependency-free Markdown checker."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from localization_learning.markdown_check import check_file


class MarkdownCheckTest(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
