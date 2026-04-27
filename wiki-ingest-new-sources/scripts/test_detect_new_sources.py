from __future__ import annotations

import json
import subprocess
import tempfile
import textwrap
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).with_name("detect_new_sources.py")


class DetectNewSourcesTests(unittest.TestCase):
    def test_lists_only_uncompiled_markdown_notes_from_configured_source_dirs(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            vault_root = Path(tmpdir)
            wiki_root = vault_root / "Wiki"
            sources_root = wiki_root / "sources"
            complete_root = wiki_root / "ingest_complete"
            inbox_root = vault_root / "00. Inbox"
            clippings_root = vault_root / "Clippings"
            sources_root.mkdir(parents=True)
            complete_root.mkdir(parents=True)
            inbox_root.mkdir(parents=True)
            clippings_root.mkdir(parents=True)

            (inbox_root / "done.md").write_text("# Done\n", encoding="utf-8")
            (inbox_root / "new-a.md").write_text("# New A\n", encoding="utf-8")
            (clippings_root / "new-b.md").write_text("# New B\n", encoding="utf-8")
            (clippings_root / "ignore.txt").write_text("not markdown\n", encoding="utf-8")

            compiled_source = textwrap.dedent(
                """\
                ---
                type: source
                source_notes:
                  - 00. Inbox/done.md
                ---

                # Source: Done
                """
            )
            (sources_root / "compiled-done.md").write_text(compiled_source, encoding="utf-8")
            archived_source = textwrap.dedent(
                """\
                ---
                type: source
                source_notes:
                  - Clippings/new-b.md
                ---

                # Source: Archived
                """
            )
            (complete_root / "archived-new-b.md").write_text(archived_source, encoding="utf-8")

            result = subprocess.run(
                [
                    "python3",
                    str(SCRIPT_PATH),
                    "--vault-root",
                    str(vault_root),
                    "--wiki-root",
                    str(wiki_root),
                    "--format",
                    "json",
                ],
                check=True,
                capture_output=True,
                text=True,
            )

            payload = json.loads(result.stdout)
            self.assertEqual(payload["compiled_count"], 2)
            self.assertEqual(payload["new_count"], 1)
            self.assertEqual(
                payload["new_sources"],
                ["00. Inbox/new-a.md"],
            )


if __name__ == "__main__":
    unittest.main()
