---
name: wiki-lint
description: Use when the user says "Wiki Lint <topic>" or when a topic-specific compiled wiki root under `Wiki/<topic>/` should be checked for contradictions, stale summaries, orphan pages, weak cross-links, missing canonical pages, or source pages that never propagated into the wiki layer.
---

# Wiki Lint

Run a health check over the compiled `Wiki/<topic>/` layer. Look for structural and synthesis issues, then make the smallest useful repairs.

## When to Use

- The user says `Wiki Lint <topic>`
- The wiki needs a consistency or maintenance pass
- You want to find stale, weakly linked, contradictory, or under-integrated pages

## Workflow

1. Treat everything after `Wiki Lint` as the topic name and work inside `Wiki/<topic>/`.
2. Read `Wiki/<topic>/index.md`, `Wiki/<topic>/overview.md`, and `Wiki/<topic>/log.md`.

3. Inspect the most central pages in:
- `Wiki/<topic>/concepts/`
- `Wiki/<topic>/topics/`
- `Wiki/<topic>/entities/`
- `Wiki/<topic>/queries/`
- `Wiki/<topic>/sources/`
- `Wiki/<topic>/ingest_complete/`

4. Check for:
- contradictions between pages
- stale summaries not reflecting newer source pages
- source pages whose claims never made it into concepts or topics
- concepts, entities, or topics repeatedly referenced but lacking canonical pages
- orphan or weakly linked pages
- index entries that no longer match the actual wiki structure

5. Make the minimum repairs that are clearly justified.

6. If you changed the wiki materially:
- update `Wiki/<topic>/index.md` if needed
- append a `lint` entry to `Wiki/<topic>/log.md`

## Notes

- `Wiki Lint` is a health check, not a broad rewrite.
- Prefer small consistency fixes over reorganizing the whole wiki.
- If a problem requires new raw sources instead of wiki edits, record that explicitly rather than guessing.
