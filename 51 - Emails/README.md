# 51 - Emails

Emails forwarded into the vault for context — the same kind of raw input as `50 - Meeting Notes`, just from a different channel.

The `daily-update` skill expects a specific frontmatter-normalization pass here (Step 0 of that skill): extracting `original-from`/`original-to`/`original-cc`/`original-date` from the forwarded headers in the body, and setting `vault-saved` to when it was forwarded. See `skills/daily-update/SKILL.md` for the exact mechanics — don't hand-write this frontmatter, let the skill do it on first run.

**Used by:** `daily-update` only. Delete this folder if you don't forward emails into your vault — `daily-update` will just process meeting notes without it.
