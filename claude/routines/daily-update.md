---
routine: daily-update
schedule: "0 17 * * 1-5"   # weekdays, 5pm
skill: skills/daily-update/SKILL.md
notify: slack
---

# Routine: daily-update

Fires weekdays at 5pm. Reads `skills/daily-update/SKILL.md` in full and executes it exactly against this vault — scans new meeting notes/emails, drafts a staging note, sends a Slack DM. Never writes to a real Project or Direct Report note directly (the skill enforces this itself).

**To register**, ask Claude directly:

> "Schedule a routine called daily-update, cron `0 17 * * 1-5`, that reads skills/daily-update/SKILL.md in this vault in full and executes it exactly."

Or use the `/schedule` skill if your setup exposes one.
