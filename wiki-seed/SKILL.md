---
name: wiki-seed
description: Use when the user says "Wiki Seed <topic>" or when a topic-specific wiki root under `Wiki/<topic>/` needs an initial set of concept, topic, or entity pages before enough sources exist for full compilation.
---

# Wiki Seed

Create the first stable skeleton inside the compiled `Wiki/<topic>/`.

## When to Use

- The user says `Wiki Seed <topic>`
- A new topic area needs starting pages
- Existing sources point to an important missing concept or topic
- The wiki needs a scaffold before more ingest work continues

## Workflow

1. Treat everything after `Wiki Seed` as the topic name and work inside `Wiki/<topic>/`.
2. Read `Wiki/<topic>/index.md`, `Wiki/<topic>/overview.md`, and the most relevant existing pages.
3. Decide the smallest useful skeleton:
- one topic page
- a few concept pages
- entity pages only if durable named objects are already central

4. Create minimal canonical pages under:
- `Wiki/<topic>/topics/`
- `Wiki/<topic>/concepts/`
- `Wiki/<topic>/entities/` when needed

5. Keep seed pages small and provenance-heavy:
- definition or summary
- why it matters
- related pages
- open questions
- linked sources if available

6. Update `Wiki/<topic>/index.md`, `Wiki/<topic>/overview.md`, and `Wiki/<topic>/log.md`.

## Notes

- `Wiki Seed` creates the first structure. It should not pretend the topic is already mature.
- Prefer the fewest pages that make future ingest cleaner.
- If the user wants a brand-new top-level folder like `Wiki/<Topic>/`, use `wiki-prj-init` first and seed inside that new sidecar root afterward.
