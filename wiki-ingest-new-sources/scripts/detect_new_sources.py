#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def parse_frontmatter(text: str) -> dict[str, object]:
    if not text.startswith("---\n"):
        return {}
    _, rest = text.split("---\n", 1)
    if "\n---\n" not in rest:
        return {}
    frontmatter_blob, _ = rest.split("\n---\n", 1)
    data: dict[str, object] = {}
    current_list_key: str | None = None
    for raw_line in frontmatter_blob.splitlines():
        if not raw_line.strip():
            continue
        if raw_line.startswith("  - ") and current_list_key:
            data.setdefault(current_list_key, [])
            assert isinstance(data[current_list_key], list)
            data[current_list_key].append(raw_line[4:].strip().strip('"'))
            continue
        current_list_key = None
        if ":" not in raw_line:
            continue
        key, value = raw_line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not value:
            data[key] = []
            current_list_key = key
            continue
        data[key] = value.strip('"')
    return data


def collect_compiled_source_notes(wiki_root: Path) -> set[str]:
    compiled: set[str] = set()
    candidate_roots = [wiki_root / "sources", wiki_root / "ingest_complete"]
    for source_root in candidate_roots:
        if not source_root.exists():
            continue
        for source_page in sorted(source_root.rglob("*.md")):
            text = source_page.read_text(encoding="utf-8")
            frontmatter = parse_frontmatter(text)
            source_notes = frontmatter.get("source_notes", [])
            if isinstance(source_notes, list):
                compiled.update(str(note) for note in source_notes)
    return compiled


def collect_candidate_sources(vault_root: Path, source_dirs: list[str]) -> list[str]:
    candidates: list[str] = []
    for source_dir in source_dirs:
        source_root = vault_root / source_dir
        if not source_root.exists():
            continue
        for note_path in sorted(source_root.rglob("*.md")):
            candidates.append(str(note_path.relative_to(vault_root)))
    return sorted(candidates)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="List raw source notes that are not yet represented in the selected topic wiki's sources folder."
    )
    parser.add_argument("--vault-root", required=True, help="Absolute path to the Obsidian vault root.")
    parser.add_argument("--wiki-root", required=True, help="Absolute path to the compiled topic wiki root, for example /Vault/Wiki/AI-Systems.")
    parser.add_argument(
        "--source-dir",
        action="append",
        dest="source_dirs",
        default=[],
        help="Vault-relative raw source directory. Repeat to include multiple directories.",
    )
    parser.add_argument(
        "--format",
        choices=("text", "json"),
        default="text",
        help="Output format.",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    vault_root = Path(args.vault_root).resolve()
    wiki_root = Path(args.wiki_root).resolve()
    source_dirs = args.source_dirs or ["00. Inbox", "Clippings"]

    compiled = collect_compiled_source_notes(wiki_root)
    candidates = collect_candidate_sources(vault_root, source_dirs)
    new_sources = sorted(note for note in candidates if note not in compiled)

    if args.format == "json":
        print(
            json.dumps(
                {
                    "vault_root": str(vault_root),
                    "wiki_root": str(wiki_root),
                    "source_dirs": source_dirs,
                    "compiled_count": len(compiled),
                    "candidate_count": len(candidates),
                    "new_count": len(new_sources),
                    "new_sources": new_sources,
                },
                ensure_ascii=True,
                indent=2,
            )
        )
    else:
        for note in new_sources:
            print(note)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
