---
name: wiki-reconcile
description: Use when the user says "Wiki Reconcile <topic>" or when multiple sources, concepts, or topics inside a topic-specific wiki root under `Wiki/<topic>/` disagree and those contradictions should be resolved or explicitly recorded.
---

# Wiki Reconcile

Resolve or explicitly record contradictions inside the compiled `Wiki/<topic>/` layer.

## When to Use

- The user says `Wiki Reconcile <topic>`
- Two or more wiki pages disagree
- Newer sources challenge older concept or topic summaries
- The wiki needs a conflict-resolution pass rather than a broad lint

## Workflow

1. Treat everything after `Wiki Reconcile` as the topic name and work inside `Wiki/<topic>/`.
2. Identify the conflicting pages or claims.
3. Read the linked `Wiki/<topic>/sources/...` or `Wiki/<topic>/ingest_complete/...` pages behind those claims.
4. Decide which of these applies:
- one claim is clearly outdated
- the claims refer to different scopes or contexts
- the evidence is mixed and the contradiction should remain explicit

5. Update the affected `Wiki/<topic>/concepts/`, `Wiki/<topic>/topics/`, or `Wiki/<topic>/entities/` pages:
- revise outdated summaries
- add scope qualifiers
- add uncertainty notes where the evidence is unresolved

6. If the reconciliation produced durable comparative analysis, file it into `Wiki/<topic>/queries/`.
7. Append a `reconcile` entry to `Wiki/<topic>/log.md` if the wiki changed materially.

## Notes

- Do not silently erase disagreement if the evidence is genuinely mixed.
- Prefer explicit revision notes over pretending there was no conflict.
