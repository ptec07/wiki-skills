# Wiki Skills

Local Codex/oh-my-codex workflow skills for building and maintaining topic-specific Obsidian wiki folders.

## Included skills

- `wiki-prj-init` - create a topic wiki scaffold.
- `wiki-ingest-new-sources` - detect and ingest new source notes for a topic.
- `wiki-backfill` - backfill older relevant notes into a topic wiki.
- `wiki-entire` - run the full wiki pipeline.
- `wiki-map` - summarize a topic wiki structure.
- `wiki-seed` - seed topic pages.
- `wiki-qry` - answer questions against a topic wiki.
- `wiki-reconcile` - reconcile contradictions across topic notes.
- `wiki-lint` - lint a topic wiki.

## Install

Copy the skill directories into your local skills directory:

```sh
cp -R wiki-* ~/.agents/skills/
```

Then reference them from Codex/oh-my-codex with commands such as:

```text
Wiki prj init <topic>
Wiki Ingest <topic> [note query]
Wiki Entire <topic>
Wiki Map <topic>
Wiki Qry <topic> <question>
Wiki Reconcile <topic>
Wiki Lint <topic>
```

## Notes

These skills assume an Obsidian-style vault workflow and may reference local vault conventions. Review each `SKILL.md` before use in a different environment.
