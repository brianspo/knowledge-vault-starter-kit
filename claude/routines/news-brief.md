---
routine: news-brief
schedule: "0 7 * * 1-5"   # weekdays, 7am
skill: skills/news-brief/SKILL.md
notify: slack
---

# Routine: news-brief

Fires weekdays at 7am. Reads `skills/news-brief/SKILL.md` in full and executes it exactly against this vault — curates 5–10 articles based on active priorities and prior feedback, sends a Slack DM. Reads and writes `skills/news-brief/references/topics.md` to learn from what gets checked off, tagged `#useful`, or ignored.

**To register**, ask Claude directly:

> "Schedule a routine called news-brief, cron `0 7 * * 1-5`, that reads skills/news-brief/SKILL.md in this vault in full and executes it exactly."

Or use the `/schedule` skill if your setup exposes one.
