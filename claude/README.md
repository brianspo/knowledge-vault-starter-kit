# Using this kit with Claude (the native setup)

This vault and its skills were built for Claude Code — everything else in this kit assumes that as the primary platform. This file exists to make one specific step concrete: turning the three time-based skills into autonomous routines. Everything else already just works once the skills are in place.

## What a routine is

A Claude Code routine (scheduled task) is three things: a name, a cron-style schedule, and a prompt. When it fires, Claude loads the prompt — in this kit's case, that's just "read and execute the matching skill file in full" — and runs it non-interactively, the same as if you'd typed the instruction yourself. State (like "when did this last successfully run") is tracked in a small JSON file the skill itself reads and writes — see each `SKILL.md`'s "run-state file" step.

## 1. Connect the tools

Set up the Obsidian MCP server (so Claude can read/write your vault) and, if you want Slack DMs, a Slack MCP server. See `../QUICKSTART.md` step 3.

## 2. Register the three time-based routines

Use the `/schedule` skill (or your scheduled-task tooling directly) to create each routine. You don't need to hand-craft anything — just tell Claude what you want, e.g.:

> "Schedule a routine called daily-update that runs weekdays at 5pm. When it fires, read skills/daily-update/SKILL.md in this vault in full and execute it exactly."

Repeat for `weekly-review` (Friday mornings) and `news-brief` (weekday mornings). The manifests in `routines/` record the schedule this kit assumes elsewhere (the Dashboard copy, the skill descriptions) — keep them in sync if you change the cadence.

## 3. Everything else runs on demand, not on a schedule

`accomplishments-reflection`, `note-update`, `note-creation`, `knowledge-retrieval`, and `autoresearch` are invoked directly, whenever needed — no routine required. Just ask Claude to run the skill.

## Exported routine manifests

- `routines/daily-update.md`
- `routines/weekly-review.md`
- `routines/news-brief.md`

Each is a small manifest — name, schedule, which skill file it runs — not a duplicate of the skill's instructions. The routine's actual behavior always lives in `skills/<name>/SKILL.md`; the manifest just says when to run it. Keeping them separate means editing a skill's logic never requires touching its schedule, and vice versa.
