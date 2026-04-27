---
name: wiki-qry
description: Use when the user says "Wiki Qry <topic>" or when a question should be answered against a topic-specific compiled wiki root under `Wiki/<topic>/` first, with durable answers filed back into that topic's wiki pages when appropriate.
---

# Wiki Qry

Query the compiled `Wiki/<topic>/` layer first. Do not start from raw sources unless the wiki clearly lacks the needed evidence.

## When to Use

- The user says `Wiki Qry <topic>`
- The user wants an answer based on the current wiki state
- The answer should prefer `Wiki/<topic>/` pages over raw vault notes

## Workflow

1. Treat everything after `Wiki Qry` as the topic name and work inside `Wiki/<topic>/`.
2. Read `Wiki/<topic>/index.md` first.
3. Open the most relevant pages under:
- `Wiki/<topic>/concepts/`
- `Wiki/<topic>/topics/`
- `Wiki/<topic>/entities/`
- `Wiki/<topic>/queries/`
- `Wiki/<topic>/sources/` only if needed for provenance or missing synthesis
- `Wiki/<topic>/ingest_complete/` when completed source provenance has been archived out of `sources/`

4. Answer the question from the compiled wiki state.

5. If the answer creates durable value, file it back:
- update an existing `concepts/`, `topics/`, or `entities/` page when it naturally belongs there
- otherwise create or update a page under `Wiki/<topic>/queries/`

6. If the wiki was materially updated, also update:
- `Wiki/<topic>/index.md` if a new page was created
- `Wiki/<topic>/log.md` with a `query` entry

## Notes

- `Wiki Qry` is for question answering against the wiki, not raw-source ingest.
- Prefer updating existing canonical pages over creating fragmented one-off notes.
- If the wiki is missing key evidence, say so explicitly and then inspect raw notes as a fallback.
