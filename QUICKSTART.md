# Quickstart

This kit is a working skeleton, not a finished product. Expect to spend an afternoon on setup, then let it accrete over a few weeks — it gets useful once it has real content in it, not before.

## 1. Set up the vault

1. Copy this whole folder into a new Obsidian vault (or a folder you'll open as one). The full folder structure — `00 - Inbox` through `90 - Templates`, plus `_resources` — already exists, each with a short README explaining what goes there and which skill populates it.
2. Install the **Templater** and **Dataview** community plugins. Point Templater's template folder at `90 - Templates/`.
3. **Delete what you don't need.** Not every folder earns its place in every setup — a few likely candidates:
   - `05 - Clippings/` if you don't web-clip
   - `51 - Emails/` if you don't forward emails into your vault
   - `55 - Daily News/` if you're skipping the `news-brief` skill
   - `30 - Resources/Research Briefs/` (and its `Sources/` subfolder) if you're skipping `autoresearch`
   - `20 - Areas/Vendor Partners/` or `20 - Areas/Key Contacts/` if that distinction doesn't apply to your role
   - `20 - Areas/Professional/` if you're skipping `accomplishments-reflection`

   Deleting a folder and skipping its matching skill go together — each folder's own README says which skill it belongs to. You can always add a folder back later; there's no migration cost, it's just a directory.

## 2. Find and replace the placeholders

Every file in this kit uses the same bracketed placeholders. Search the whole folder for these and replace them once, consistently:

- `[Your Name]` — you
- `[Your Title]` — your role
- `[Your Organization]` — your company/institution
- `[YOUR_SLACK_USER_ID]` — your Slack member ID, if you're wiring up Slack DMs (Slack profile → "Copy member ID")

Do **not** try to pre-populate example projects, direct reports, or vendors — let real content accumulate from real meetings and 1:1s. A vault seeded with fake data is harder to trust than an empty one.

## 3. Connect the tools

- **Obsidian ↔ Claude Code:** install the Local REST API community plugin in Obsidian, then connect an Obsidian MCP server (e.g. `@bitbonsai/mcpvault`) so Claude Code can read/write notes directly.
- **Slack (optional):** only needed if you want the scheduled agents to DM you. Skip this if you'd rather just read the vault directly.
- **Scheduling (optional):** Claude's routines feature is what runs `daily-update`, `weekly-review`, and `news-brief` on their own — see `claude/README.md` for how to register each one, and `claude/routines/` for the exported schedule for each. Without it, you can still run any skill manually.

## 4. Start with two or three skills, not eight

Don't turn everything on at once. A sensible order:

1. **`note-creation`** and **`note-update`** first — these are the ones you'll invoke manually, constantly, as you build up real Project and Direct Report notes. Get comfortable with the conventions before automating anything.
2. **`daily-update`** once you have a real cadence of meeting notes landing in `50 - Meeting Notes/`. This is the highest-leverage automation, but it's only useful once there's real input for it to process.
3. **`weekly-review`** once daily-update is working and you trust its staging-note output.
4. The rest — `news-brief`, `accomplishments-reflection`, `autoresearch`, `knowledge-retrieval` — add as you find you want them. None of them depend on each other.

## 5. The one rule that makes this safe

Every skill in this kit that touches a Project or Direct Report note does it in two steps: draft to a staging note, then wait for you to explicitly say "apply." Keep that pattern if you extend or write your own skills. It's not there to slow you down — it's there so nothing about a real person's record changes without you reading it first.

## 6. Platform setup: Claude or Codex

This kit was built for Claude Code — `claude/README.md` covers registering the three time-based skills as routines (step 3 above, made concrete).

It also runs on OpenAI's Codex (CLI, Desktop, or Cloud), close to full parity — same MCP servers, same skills, its own native scheduling instead of routines. See `codex/README.md` for that setup. The `AGENTS.md` at the kit root is what Codex auto-loads; it's the Codex-native counterpart to this file.
