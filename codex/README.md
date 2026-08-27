# Using this kit with Codex

This vault and its skills were built and run in Claude Code — that's the native setup (see `../claude/README.md` for how that's wired up as routines). This file documents the port to OpenAI's Codex (CLI, Desktop, or Cloud) for anyone using that instead.

The two are close in capability: both read/write files, run commands, connect to MCP servers, and support scheduled/recurring runs. So this isn't a workaround or a downgrade — it's close to a direct port. The main differences are naming (`AGENTS.md` vs. `CLAUDE.md`) and where scheduling lives (Codex's own automations/cron vs. Claude's routines). Check current Codex docs for exact command syntax — this surface has been moving fast and the commands below may drift.

## 1. AGENTS.md does the work CLAUDE.md would do

Codex auto-loads `AGENTS.md` from the repo/folder root — that file is already sitting at the top of this kit. It points Codex at the vault conventions and tells it to read a skill's `SKILL.md` in full before acting on it. You shouldn't need to change it unless you restructure the skills.

## 2. Connect the same MCP servers

Codex supports MCP servers directly. Add the same Obsidian MCP server used for Claude Code:

```
codex mcp add obsidian -- <your obsidian MCP server command>
```

And, if you want Slack DMs from the scheduled skills, add a Slack MCP server the same way. Exact flags depend on your installed Codex version — run `codex mcp --help` or check OpenAI's current docs rather than trusting a copy-pasted command here.

Once connected, the tool names Codex exposes may differ slightly from Claude Code's `mcp__obsidian__*` naming — that's fine, the skill files describe *what* to call (read a note, patch a note, search notes), not a hardcoded tool name.

## 3. Set up scheduling for the time-based skills

Three skills expect to run on a schedule: `daily-update` (weekdays, e.g. 5pm), `weekly-review` (Friday mornings), `news-brief` (weekday mornings). `accomplishments-reflection` is manual/on-demand on either platform.

Where Claude Code has routines, Codex has its own recurring-task mechanism — automations in the Desktop/Cloud apps, or cron-style scheduling in the CLI. For each scheduled skill, create an automation/cron entry whose prompt is essentially: *"Read skills/daily-update/SKILL.md in full and execute it exactly."* Point it at this vault as the working directory so `AGENTS.md` loads automatically.

If your Codex version doesn't yet have built-in scheduling, `codex exec` runs a single prompt non-interactively and returns a real exit code — wire that into system cron (`crontab`) or `launchd` as a fallback; the skill itself doesn't care what triggered it.

## 4. Test one skill before wiring up all of them

Start with `note-update` or `note-creation` run manually — ask Codex to read the skill and execute it against a real note. Confirm it respects the staging-note pattern (drafts to `00 - Inbox/`, doesn't touch real notes without confirmation) before trusting it with anything scheduled.

## What's genuinely different from the Claude Code setup

- **Skill invocation is instruction-following, not a formal registry.** Claude Code's Skill tool loads a skill by name; Codex just reads whatever `AGENTS.md` points it to. Functionally similar, mechanically different.
- **Scheduling UX varies by which Codex surface you're on** (CLI vs. Desktop vs. Cloud) and has changed release to release — verify against current docs rather than this file.
- Everything else — the vault structure, the staging/apply safety pattern, the note conventions, the Dashboard — is identical. This kit was designed to not care which agent is running it.
