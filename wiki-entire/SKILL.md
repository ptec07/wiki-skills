---
name: wiki-entire
description: "Use when the user says \"Wiki Entire <topic> [focus terms]\" or wants to run a complete topic wiki maintenance cycle: init, ingest, reconcile, map, lint, and focused backfill for a `Wiki/<topic>/` sidecar wiki."
---

# Wiki Entire

Run one complete lifecycle for a topic-specific sidecar wiki under `Wiki/<topic>/`.

## When to Use

- The user says `Wiki Entire <topic> [focus terms]`
- The user wants the full wiki cycle in one autonomous pass
- A topic wiki should be created or refreshed end-to-end instead of running each wiki skill manually

## Workflow

1. Parse the command as:

```text
Wiki Entire <TOPIC_FOLDER> [FOCUS_TERMS]
```

Use the first argument after `Wiki Entire` as the topic folder name.
Treat any remaining text as optional focused backfill terms.

2. Run the cycle in this order:

- `wiki-prj-init`: create `Wiki/<topic>/` if it does not already exist; if it already exists, verify the expected folders and control pages instead of overwriting content.
- `wiki-ingest`: ingest topic-related raw notes. With no explicit note query, select only relevant uncompiled notes according to the `wiki-ingest` skill.
- `wiki-reconcile`: resolve or explicitly scope contradictions introduced by the ingest pass.
- `wiki-map`: inspect and summarize topic, concept, entity, source, and query coverage.
- `wiki-lint`: repair the smallest justified structural or consistency issues.
- `wiki-backfill`: run a focused backfill using `FOCUS_TERMS` when provided. If no focus terms are provided, derive a narrow focus from `wiki-map` or `wiki-lint` gaps; if no clear gap exists, skip backfill and record why.

3. During each phase, follow the corresponding skill contract:

- `~/.agents/skills/wiki-prj-init/SKILL.md`
- `~/.agents/skills/wiki-ingest-new-sources/SKILL.md`
- `~/.agents/skills/wiki-reconcile/SKILL.md`
- `~/.agents/skills/wiki-map/SKILL.md`
- `~/.agents/skills/wiki-lint/SKILL.md`
- `~/.agents/skills/wiki-backfill/SKILL.md`

4. Keep durable records inside the topic wiki:

- append lifecycle entries to `Wiki/<topic>/log.md`
- create query artifacts under `Wiki/<topic>/queries/` for source manifests, reconciliation notes, lint findings, and focused backfill results when materially useful
- update `Wiki/<topic>/index.md` and `Wiki/<topic>/overview.md` after material structure changes

5. Verify before reporting completion:

```bash
find "<VAULT_ROOT>/Wiki/<TOPIC_FOLDER>/sources" -maxdepth 1 -type f | wc -l
find "<VAULT_ROOT>/Wiki/<TOPIC_FOLDER>/ingest_complete" -maxdepth 1 -type f | wc -l
```

Also check:

- no unresolved `TODO`, `TBD`, `FIXME`, `placeholder`, or stale seed wording in curated root/topic/concept/entity/query pages
- no missing wikilinks among curated wiki pages
- focused backfill notes selected in the cycle are no longer detected as uncompiled for the same topic

## Notes

- This is an orchestration skill, not a replacement for the individual wiki skills. Load and follow the specific phase skill before doing phase-specific work.
- Prefer one coherent ingest/backfill batch over forcing every available raw note into the wiki.
- Preserve raw source notes in `00. Inbox/` and `Clippings/`.
- If the topic already exists, never reset or recreate it destructively; continue from the current state.
- If automatic ingest or backfill would be too broad, choose a small evidence-backed batch and record the skipped scope.
