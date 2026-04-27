---
name: wiki-prj-init
description: Use when the user says "Wiki prj init <topic>" or wants to create a new top-level topic folder under `Wiki/` and scaffold its initial sidecar wiki structure from the trailing topic string.
---

# Wiki Prj Init

Create a topic-specific sidecar wiki under `Wiki/<Topic>/`.

## When to Use

- The user says `Wiki prj init <topic>`
- A new domain needs its own top-level folder directly under `Wiki/`
- The user wants the topic string after the command to become the folder seed

## Workflow

1. Treat everything after `Wiki prj init` as the topic name.
2. Run:

```bash
python3 "<VAULT_ROOT>/Wiki/tools/init_topic_wiki.py" "<TOPIC_NAME>"
```

3. Verify the scaffold:

```bash
find "<VAULT_ROOT>/Wiki/<TOPIC_FOLDER>" -maxdepth 2 | sort
```

4. Report:
- created topic root
- canonical topic slug
- created control pages and seed topic page

## Notes

- Create the topic folder one level below `Wiki/`, not inside `Wiki/topics/`.
- Keep `Wiki/tools/` and `Wiki/templates/` shared at the root unless the user explicitly asks for per-topic copies.
- Use the trailing command string as the naming source. The script converts whitespace to hyphens and strips filesystem-unsafe characters.
