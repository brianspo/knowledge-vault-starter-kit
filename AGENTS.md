# Vault Operating Instructions

This file is auto-loaded by Codex (and any other agent that reads `AGENTS.md`-style repo instructions) whenever it works in this vault. It's the Codex-native equivalent of the guidance in `README.md` — read that file too for the full folder reference and note conventions; this file exists so Codex picks the essentials up automatically without being told to go find them.

## What this vault is

A personal knowledge management system for leadership work: active Projects, ongoing Areas (direct reports, vendors, key contacts), Meeting Notes as raw input, Techniques as distilled lessons, and a `Dashboard.md` at the root that surfaces state-of-the-world at a glance. Full structure and conventions: `README.md`.

## Skills

This kit doesn't rely on a formal skills-registration system. Each "skill" is just a markdown procedure in `skills/<name>/SKILL.md`. When asked to do something a skill covers — process meeting notes, draft a weekly review, update or create a note, run research — **read the matching `skills/<name>/SKILL.md` file in full first, then follow it exactly**, including its file paths, output formats, and rules. Don't paraphrase or shortcut a skill from memory once you've read it once; re-read it each time, since these files get edited.

Skill index:
- `skills/daily-update/` — process new meeting notes/emails into a staging note
- `skills/weekly-review/` — draft the Friday weekly review
- `skills/news-brief/` — curate a daily news brief
- `skills/accomplishments-reflection/` — monthly accomplishments coaching session
- `skills/note-update/` — update an existing note
- `skills/note-creation/` — create a new note from the right template
- `skills/knowledge-retrieval/` — search the vault before going external
- `skills/autoresearch/` — multi-round web research → Decision Brief

## Tools

These skills assume MCP access to Obsidian (read/write notes) and, optionally, Slack (send a DM). If those aren't connected yet, see `codex/README.md` for setup — the same MCP servers used for Claude Code work here too.

## The one rule that matters most

Every skill that touches a Project or Direct Report note drafts to a staging note first (`00 - Inbox/Vault Updates YYYY-MM-DD.md`) and waits for an explicit "apply" instruction before writing to the real note. **Never skip the staging step**, even if asked to "just do it" — propose the change, then apply only on confirmation. This is the load-bearing safety property of the whole system: nothing about a real person's record changes without a human reading it first.

## Tagging

When creating or updating notes, apply `tags:` frontmatter using the controlled vocabulary documented in `README.md` (Tagging Convention section). Rules:

- Use kebab-case topic tags drawn from the vocabulary — do not invent new tags without a clear gap
- Apply tags to: Project notes, Meeting notes, Techniques, Research briefs
- Do NOT tag folder membership (`DirectReport`, `Technique`, `VendorPartner`) — remove these if you encounter them
- A project note gets its own project tag + any strategic themes it touches
- A meeting note gets the tag(s) for the project(s) discussed
- When uncertain whether a new tag is warranted, stage the question rather than inventing one

## Conventions worth repeating here

- Always set `last-updated` frontmatter to today's date on any note you touch
- Never invent content — only use what's in the meeting notes, emails, or explicit instructions
- Decisions Log entries are append-only; Open Questions get checked off, never deleted
- Running Context sections get new dated bullets added, never replaced wholesale
