---
name: wiki-ingest
description: Use when the user says "Wiki Ingest <topic> [note-query]" and either wants one specific raw source integrated into `Wiki/<topic>/` or wants the skill to auto-pick only topic-related 00. Inbox notes when no note query is provided.
---

# Wiki Ingest

Compile a specific raw source note into the topic-specific `Wiki/<topic>/` layer. The ingest is not complete until the source page, affected concept/topic/entity pages, and topic root docs are all updated.

## When to Use

- The user says `Wiki Ingest <topic> <note-query>`
- The user says `Wiki Ingest <topic>` with no note query and expects up to 7 relevant uncompiled `00. Inbox/` notes to be ingested
- A specific note in `00. Inbox/` or `Clippings/` should be integrated into one topic wiki
- The ingest should finish the compiled pass, not stop at a draft source page
- Existing compiled source pages in `Wiki/<topic>/sources/` or `Wiki/<topic>/ingest_complete/` must not be duplicated
- Raw source notes preserved in `00. Inbox/` after ingest must not be selected again for the same topic.

## Duplicate Rule

A raw note counts as already compiled if its vault-relative path appears in any `source_notes:` list inside `Wiki/<topic>/sources/*.md` or `Wiki/<topic>/ingest_complete/*.md`.
This duplicate rule applies to both automatic topic selection and explicit note-query selection.

## Workflow

1. Parse the command as:

```text
Wiki Ingest <TOPIC_FOLDER> [NOTE_QUERY]
```

Use the first argument after `Wiki Ingest` as the topic folder name.
If more text remains, treat it as the note query.
If no note query remains, scan `00. Inbox/` only and select up to 7 top-ranked uncompiled notes whose filenames or contents are relevant enough to the topic.
Use both the topic name and the existing context already present under `Wiki/<topic>/` such as topic pages, concept pages, and integrated source summaries when judging relevance.

2. Resolve the exact source note and scaffold it:

```bash
python3 "<VAULT_ROOT>/Wiki/tools/run_topic_ingest.py" "<TOPIC_FOLDER>" "<NOTE_QUERY>"
```

If no note query was provided:

```bash
python3 "<VAULT_ROOT>/Wiki/tools/run_topic_ingest.py" "<TOPIC_FOLDER>"
```

3. Open the selected source note and the generated source page.

4. Complete the ingest as a compiled wiki pass:
- finish the `Wiki/<topic>/sources/...` page
- update affected `Wiki/<topic>/concepts/...`
- update affected `Wiki/<topic>/topics/...`
- update `Wiki/<topic>/entities/...` if a durable named object emerges
- update `Wiki/<topic>/index.md`, `Wiki/<topic>/overview.md`, and `Wiki/<topic>/log.md`

5. Remove any remaining `TODO` placeholders in the files touched by this ingest.

6. If the source page is complete and no errors occurred, archive it:

```bash
python3 "<VAULT_ROOT>/Wiki/tools/archive_completed_ingest.py" \
  --topic-root "<VAULT_ROOT>/Wiki/<TOPIC_FOLDER>" \
  "<SOURCE_SLUG>"
```

Archiving moves the compiled source page to `ingest_complete/`.
Raw source notes are preserved in place after ingest, including notes under `00. Inbox/`.

7. Report the exact source note or notes selected, because note resolution is part of the command contract.

## Notes

- Default raw source roots are `00. Inbox/` and `Clippings/`.
- This skill always expects a topic folder. The note query is optional.
- If no note query is provided, only `00. Inbox/` is scanned and up to 7 top-ranked uncompiled topic-related notes are selected. Unrelated notes must be skipped.
- `run_topic_ingest.py` only resolves note selection and runs the scaffolding step. The skill must still finish the compiled wiki integration in the same turn.
- Source notes with Korean-only titles are scaffolded with a stable ASCII fallback slug such as `YYYY-MM-DD-source-<hash>`.
- Only archive a source page when its `TODO` placeholders are gone and the ingest finished without errors.
- Archiving a completed source page must not delete linked raw notes recorded in `source_notes:`.
- Use this skill for incremental maintenance. Use broader ingest or lint workflows for major reorganization.
