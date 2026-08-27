---
routine: weekly-review
schedule: "0 8 * * 5"   # Fridays, 8am
skill: skills/weekly-review/SKILL.md
notify: slack
---

# Routine: weekly-review

Fires Friday mornings at 8am. Reads `skills/weekly-review/SKILL.md` in full and executes it exactly against this vault — drafts the week's review from meeting notes and project status, sends a Slack DM. Leaves the personal-reflection sections blank on purpose.

**To register**, ask Claude directly:

> "Schedule a routine called weekly-review, cron `0 8 * * 5`, that reads skills/weekly-review/SKILL.md in this vault in full and executes it exactly."

Or use the `/schedule` skill if your setup exposes one.
