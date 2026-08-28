# [Your Organization] — Leadership Knowledge Vault (Starter Kit)

**Owner:** [Your Name], [Your Title]
**Purpose:** A personal knowledge management system for leadership work — tracking active projects, managing direct reports, capturing meeting intelligence, distilling institutional knowledge, and maintaining organizational memory, with a set of AI agents that keep it current.

This is an opinionated and sanitized starter kit, stripped of any specific organization's or person's content. The full folder structure ships pre-built, each folder with its own short README — delete whatever you don't need (and skip installing the matching skill). Fork it, fill in the placeholders, and start with two or three skills rather than all eight — see `QUICKSTART.md`.

This approach assumes you're using Obsidian, along with its MCP server and a couple of plugins, and an agentic coding tool like Codex, Claude, GitHub Copilot, Cursor, etc.

---

## Organization Model

This vault uses a **modified PARA + CODE model** (Projects, Areas, Resources, Archives; Capture, Organize, Distill, Express) with a `35 - Techniques` folder added to support the Distill stage of the CODE workflow. Folders are numbered to enforce sort order and signal the flow of information: raw input enters at the left, distilled knowledge accumulates toward the middle, and outputs emerge at the right.

For more info on these techniques (or use your favorite search agent):

- PARA - https://fortelabs.com/blog/para/
- CODE - https://fortelabs.com/blog/basboverview/

There's a whole cottage industry out there of blog articles and GitHub repos to do this for you and the amount of breathless hype can be a bit much. I tried one and it was way too heavyweight, so I asked my favorite LLM to suggest a better starting point (I started Claude so I had as much control and featuers as possible but this works with Codex as well now). I've iterated for a few months and this is what I have right now.


```
Dashboard.md        ← top-level state-of-the-world note (live queries + agent-written flags)
AGENTS.md           ← auto-loaded by Codex (and similar agents); Codex-native counterpart to this README
claude/              ← this kit's native platform — how to turn the time-based skills into routines
codex/               ← setup guide for running this kit on OpenAI's Codex instead
00 - Inbox          ← capture & staging (process weekly)
05 - Clippings      ← raw web/article captures, not yet distilled
10 - Projects       ← active work with defined outcomes
20 - Areas          ← ongoing responsibilities (no end date)
30 - Resources      ← reference material (articles, briefs, vendor docs)
35 - Techniques     ← distilled, generalizable knowledge extracted from experience
40 - Archives       ← completed, inactive, or deprioritized
50 - Meeting Notes  ← AI-transcribed meeting intelligence (high volume)
51 - Emails         ← emails forwarded into the vault for context
55 - Daily News     ← daily news briefs from the news-brief skill
60 - Blog Posts     ← leadership blog drafts and published posts
70 - Weekly Reviews ← cadenced reflection notes
90 - Templates      ← Templater templates (not content)
_resources          ← attachments and images (managed by Obsidian)
skills/             ← AI skills for vault operations (this kit's equivalent of Claude Code's Skills/skills/)
```

### Information Flow (CODE)

| Stage | Where | What happens |
|---|---|---|
| **Capture** | `00 - Inbox`, `50 - Meeting Notes` | Raw input lands here |
| **Organize** | `10 - Projects`, `20 - Areas` | Context is maintained and updated |
| **Distill** | `35 - Techniques`, `30 - Resources` | Knowledge is extracted and made reusable |
| **Express** | `60 - Blog Posts`, `70 - Weekly Reviews` | Knowledge becomes output |

---

## Folder Reference

Every folder listed below has its own README with the same content plus which skill populates it — this section is the quick-reference version.

### `05 - Clippings`
Raw capture of a web page or external content, not yet processed into a Resource or Technique. No skill writes here automatically.

### `00 - Inbox`
Landing zone for quick capture and AI-proposed vault updates.
- **`Vault Updates YYYY-MM-DD.md`** — staged change proposals written by the daily-update agent after reviewing meeting notes. Review, then say "apply today's vault updates" to write changes to their target notes.
- Temporary holding for anything not yet filed.

**Process cadence:** Clear weekly. Nothing here is permanent.

### `10 - Projects`
One note per active program or initiative. A **Project** has a defined outcome and a natural end state. When complete or deprioritized, move to `40 - Archives`.

**Project note structure:**

| Section | Purpose |
|---|---|
| What Success Looks Like | Defines done. Rewrite as scope clarifies. |
| Current Status | Always present state — rewrite in place, date each update. |
| Key Stakeholders | Name, role, what they need from this project. |
| Decisions Log | Append-only table. Date, decision, owner, rationale. |
| Open Questions | Checkbox list. Check off when resolved. |
| Risks | Likelihood, impact, mitigation. |
| See Also | Wikilinks to related Projects, Techniques, Resources. |

### `20 - Areas`
Ongoing responsibilities with no end date.

**`20 - Areas/Direct Reports/`** — one note per direct report.

**Direct report note structure:**

| Section | Purpose |
|---|---|
| Role & Scope | Title, team, tenure. |
| Current Focus Areas | Top 2-3 priorities right now. |
| Running Context | Evolving situational awareness — add dated bullets as things change. |
| What They Need From Me | Most important thing you can do for this person right now. |
| Open Commitments I've Made | Checkbox list. |

**`20 - Areas/Vendor Partners/`** and **`20 - Areas/Key Contacts/`** follow the same running-context pattern — see `90 - Templates/`.

**`20 - Areas/Professional/`** — your own career artifacts (Accomplishments Log, Resume Seed), not about anyone else. Built by the `accomplishments-reflection` skill.

### `30 - Resources`
Reference material not tied to a specific active project. Subfolders:
- `Research Briefs/` — Decision Briefs from the autoresearch skill (`YYYY-MM-DD - [Topic].md`)
- `Research Briefs/Sources/` — individual source pages created during research (`YYYY-MM-DD - [Domain] - [Title Slug].md`)

**Resource frontmatter convention:**
```yaml
type: research-brief | source | resource
source: "[domain or publisher]"
tags: [Resource, ResearchBrief | Source]
last-updated: YYYY-MM-DD
```

### `35 - Techniques`
**Distilled, generalizable knowledge** extracted from experience — the Distill stage of CODE. A Technique is not a meeting note or a project summary. It's what generalizes *beyond* the specific situation: a framework, a mental model, a process that worked, a failure mode to avoid.

**When to create a Technique:**
- After closing a project phase and reflecting on what generalized
- When a "What I Learned" weekly review bullet deserves a permanent home
- When autoresearch surfaces a reusable framework

**Naming convention:** Name by the generalizable skill, not the specific project.
- ✅ `Structuring a Multi-Phase Strategy Engagement.md`
- ❌ `Project X Lessons.md`

### `40 - Archives`
Completed projects, ended relationships, superseded resources. Move here rather than delete. Retain original structure.

### `50 - Meeting Notes`
High-volume meeting transcriptions (from an AI notetaker, or however you capture meetings). Every note is a discrete meeting event.

**Naming:** `YYYY-MM-DD - [Meeting Title].md`

**Frontmatter:** `project: [Project Name]` links the note to a project.

Meeting notes are **inputs**, not the system of record. Decisions and commitments should be promoted into Project or Direct Report notes — this is what the daily-update agent does.

### `51 - Emails`
Emails forwarded into the vault for context, same role as Meeting Notes but a different input channel. `daily-update`'s Step 0 normalizes frontmatter on first read (extracting the real sender/date from the forwarded headers) — don't hand-write it.

### `55 - Daily News`
Daily news briefs from the `news-brief` skill. Check off what you read, tag `#useful` on what's worth keeping — that feedback tunes future briefs.

### `60 - Blog Posts`
Leadership blog drafts and published posts.

### `70 - Weekly Reviews`
Cadenced weekly reflection notes. Filename: `YYYY-WWW.md` (ISO week numbering).

Drafted by the weekly-review scheduled agent every Friday morning and sent as a Slack DM for review and editing.

### `90 - Templates`
Templater plugin templates. Not content.

| Template | Use for |
|---|---|
| `Technique.md` | New entry in `35 - Techniques` |
| `Project Note.md` | New entry in `10 - Projects` |
| `Area Note - Direct Report.md` | New entry in `20 - Areas/Direct Reports` |
| `Area Note - Vendor Partner.md` | New entry in `20 - Areas/Vendor Partners` |
| `Area Note - Key Contact.md` | New entry in `20 - Areas/Key Contacts` |
| `Weekly Review.md` | Weekly reflection in `70 - Weekly Reviews` |
| `Leadership Blog Post.md` | New entry in `60 - Blog Posts` |

### `skills/`
AI skills for vault operations. In Claude Code, these live in a plugin's `Skills/skills/` directory; adapt the path to whatever your tool expects.

| Skill | Purpose |
|---|---|
| `autoresearch` | Multi-round web research → Decision Brief saved to `30 - Resources/Research Briefs/` |
| `knowledge-retrieval` | Search the vault before going external; synthesize what's already known |
| `note-creation` | Create properly structured notes in the correct folder with cross-links |
| `note-update` | Update existing notes, add running context, promote lessons to Techniques |
| `daily-update` | scheduled, e.g. 5pm weekdays — process meeting notes → staging note in `00 - Inbox` → Slack DM → updates `Dashboard.md` |
| `weekly-review` | scheduled, e.g. 8am Friday — draft weekly review → `70 - Weekly Reviews/` → Slack DM → updates `Dashboard.md` |
| `news-brief` | scheduled, e.g. 7am weekdays — curate 5–10 articles → `55 - Daily News/` → Slack DM → updates `Dashboard.md` |
| `accomplishments-reflection` | manual, ~monthly — reflection session → `20 - Areas/Professional/Accomplishments Log.md` → updates `Dashboard.md` |

---

## Tagging Convention

Tags serve one purpose: **cross-cutting discovery across note types**. The folder structure handles organization; tags let you find everything touching a topic — projects, meeting notes, research briefs, techniques — in one search.

Two kinds of tags, one field (`tags:` in frontmatter):

```yaml
tags: [topic-tag, topic-tag, state-tag]
```

### Topic tags

Kebab-case. Build your own controlled vocabulary based on your active projects and recurring strategic themes. A few examples to seed from:

| Tag | Covers |
|---|---|
| `[your-project-name]` | One tag per active project or program |
| `[strategic-theme]` | Recurring topics that cut across projects (e.g., `ai-governance`, `security-posture`, `budget-planning`) |

**Rules:**
- One tag per active project — use the same tag on the project note, meeting notes, research briefs, and techniques related to it
- Strategic theme tags let you find all notes touching a topic regardless of which folder they're in
- Add new tags when a genuinely new topic emerges — don't create one-off tags for specific meetings or people
- Keep the vocabulary in a single place (this README or a `AGENTS.md` section) so the AI agent stays consistent

### State tags (optional, use sparingly)

| Tag | Meaning |
|---|---|
| `waiting` | Blocked on someone outside your control |
| `share` | Worth distributing to the team or stakeholders |
| `stale` | Hasn't been updated — needs a review pass |

### Where to apply

| Note type | Apply tags for |
|---|---|
| Project notes | The project's own tag + any strategic themes it touches |
| Meeting notes | The project(s) discussed |
| Techniques | Strategic themes the technique applies to |
| Research briefs | Subject matter covered |

### What NOT to tag

- **Don't replicate folder membership** — `DirectReport`, `Technique`, `VendorPartner` are redundant with the folder structure
- **Don't create one-off tags** for specific meetings, people, or incidents
- **Don't tag with type/status** already expressed in `type:` or `status:` frontmatter fields

---

## Plugins

### Templater
Dynamic templates with auto-filled dates and prompts.

### Dataview
Live queries in Project and Direct Report notes, and in `Dashboard.md`. Key patterns:

```
LIST FROM "50 - Meeting Notes" WHERE contains(file.name, "Project Name") SORT file.mtime DESC
```
```
TASK WHERE !completed AND contains(file.name, "Project Name") SORT file.mtime ASC
```

Only checkboxes, list items, and frontmatter fields are live-queryable — markdown tables (like a Risks table) are not structured data Dataview can query. If you want a live "risks across all projects" view, you'd need to restructure Risks as checkbox/list items with inline fields; the starting Dashboard leaves risk synthesis to the daily-update agent instead, since that requires judgment a query can't express.

### Obsidian Local REST API
Required for an MCP server (e.g. `@bitbonsai/mcpvault`) to read and write your vault from Claude Code.

---

## Dashboard (`Dashboard.md`, vault root)
The single top-level note — open this first. Two kinds of content, clearly separated:
- **Live Dataview queries** (Needs Your Review, Active Projects, Upcoming Target Dates, Open Commitments) — always current, computed from frontmatter and checkboxes on every open. No agent maintains these.
- **Agent-written blocks**, each delimited by `<!-- AGENT:... -->` HTML comment markers and owned by exactly one scheduled task, which patches only its own marker pair on every run: Risks & Flags and Direct-Report Follow-ups (`daily-update`), and one line each in Latest Outputs (`news-brief`, `weekly-review`, `accomplishments-reflection`).

The Active Projects table depends on every Project and Direct Report note keeping its `last-updated` frontmatter current — every template in this kit already has the field; keep setting it on every edit.

---

## Key Conventions for LLM Agents

**Writing:**
- Never write directly to `10 - Projects` or `20 - Areas` without explicit review, unless the user has said "apply today's vault updates" or equivalent
- Stage proposed changes in `00 - Inbox/Vault Updates YYYY-MM-DD.md`
- Prefer targeted patches over full-note rewrites for any update to an existing note
- Use `write_note`-equivalent only for new notes or complete rewrites that have been approved

**Updating notes:**
- "Current Status" in Project notes → always present state, rewrite in place, date each update
- "Decisions Log" → append-only, never edit existing rows
- "Open Questions" → check off when resolved, do not delete
- "Running Context" in Direct Report notes → add dated bullets, do not replace wholesale
- **Always update `last-updated` frontmatter on every edit** — the Dashboard's Active Projects table sorts on it to surface stale projects, so a missed update makes a project look more current than it is

**Cross-linking:**
- Every new note should link to at least one existing note
- Techniques link back to source Projects/Meeting Notes
- Research Briefs link to related Projects and any Techniques created from the research

**General:**
- Do not invent content — only capture what appears in meeting notes or what's stated directly
- When uncertain whether something is a decision vs. a discussion point: include with "(confirm: was this decided?)"
- Prefer patching over rewriting for any update to an existing note
