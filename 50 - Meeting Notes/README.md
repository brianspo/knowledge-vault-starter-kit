# 50 - Meeting Notes

High-volume meeting transcriptions — from an AI notetaker, or however you capture meetings. Every note is a discrete meeting event.

**Naming:** `YYYY-MM-DD - [Meeting Title].md`

**Frontmatter:** `project: [Project Name]` links the note to a project. Every meeting note should also carry a `[[Entity Name]]` wikilink near the top to every Project, Direct Report, Vendor Partner, or Key Contact it concerns — that link is what makes the meeting show up in that note's own "Related Meeting Notes" query automatically. A missing link means the meeting silently never surfaces there.

Meeting notes are **inputs**, not the system of record. Decisions and commitments get promoted into Project or Direct Report notes — that's what `daily-update` does.

**Used by:** `daily-update`, `weekly-review`, `note-creation`, `knowledge-retrieval`, `autoresearch`. Core to the kit — keep it even if you're not running `daily-update` yet, since it's where raw input accumulates either way.
