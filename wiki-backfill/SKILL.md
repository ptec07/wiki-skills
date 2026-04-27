---
name: wiki-backfill
description: Use when the user says "Wiki Backfill <topic>" or when older raw notes in Inbox or Clippings should be compiled into a topic-specific wiki root under `Wiki/<topic>/` in batches, skipping anything already represented there.
---

# Wiki Backfill

Backfill older raw source notes into the compiled `Wiki/<topic>/` layer without reprocessing already compiled notes.

## When to Use

- The user says `Wiki Backfill <topic>`
- There is a backlog of uncompiled notes in `Inbox/` or `Clippings/`
- The goal is batch maintenance rather than one-off ingest

## Workflow

1. Treat everything after `Wiki Backfill` as the topic name and set:

```bash
TOPIC_ROOT="<VAULT_ROOT>/Wiki/<TOPIC_FOLDER>"
```

2. Detect uncompiled notes:

```bash
python3 ~/.agents/skills/wiki-ingest-new-sources/scripts/detect_new_sources.py \
  --vault-root "<VAULT_ROOT>" \
  --wiki-root "$TOPIC_ROOT" \
  --source-dir Inbox \
  --source-dir Clippings \
  --format json
```

3. Sort the returned `new_sources` into a sensible batch:
- by topic similarity when possible
- otherwise by oldest filename date first

4. Process the batch one note at a time with the normal ingest flow:
- scaffold the source page
- integrate the note into `Wiki/<topic>/concepts/`, `Wiki/<topic>/topics/`, and `Wiki/<topic>/entities/` if justified
- update `Wiki/<topic>/index.md`, `Wiki/<topic>/overview.md`, and `Wiki/<topic>/log.md`

5. After each batch, re-run detection and stop when:
- the batch limit is reached, or
- no uncompiled notes remain

## Notes

- Do not reprocess notes already present in any `source_notes:` list under `Wiki/<topic>/sources/*.md` or `Wiki/<topic>/ingest_complete/*.md`.
- Prefer smaller coherent batches over dumping dozens of unrelated notes into the wiki at once.
- If a note is too weak or too off-topic, record that explicitly instead of forcing a large structural change.
