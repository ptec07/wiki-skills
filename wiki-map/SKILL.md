---
name: wiki-map
description: Use when the user says "Wiki Map <topic>" or when the current structure of a topic-specific wiki root under `Wiki/<topic>/` should be summarized into its main concepts, topics, entities, source clusters, and obvious gaps.
---

# Wiki Map

Summarize the current shape of the compiled `Wiki/<topic>/` layer.

## When to Use

- The user says `Wiki Map <topic>`
- The user wants a quick orientation to what the wiki currently covers
- You need to identify hubs, clusters, and gaps before ingest or lint work

## Workflow

1. Treat everything after `Wiki Map` as the topic name and set `TOPIC_ROOT=Wiki/<topic>/`.
2. Read `TOPIC_ROOT/index.md` and `TOPIC_ROOT/overview.md`.
3. Inspect the main folders:
- `TOPIC_ROOT/concepts/`
- `TOPIC_ROOT/topics/`
- `TOPIC_ROOT/entities/`
- `TOPIC_ROOT/queries/`
- `TOPIC_ROOT/sources/`
- `TOPIC_ROOT/ingest_complete/`

4. Summarize:
- main topic hubs
- most central concepts
- entity coverage, if any
- newest or most influential sources
- obvious missing pages or weak areas

5. If the user wants persistence, file the map into:
- `TOPIC_ROOT/queries/` for a durable map artifact, or
- an existing topic/overview page if it naturally belongs there

## Notes

- `Wiki Map` is descriptive first. Do not reorganize the wiki unless the user asks.
- Prefer a structural summary over a file-by-file inventory.
