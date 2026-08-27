---
name: note-creation
description: Create a new note in the vault in the correct folder with proper frontmatter and cross-links. Use when asked to create a project note, technique, area, resource, or person note.
---

# Note Creation

Create well-structured notes in the vault that follow the templates, use proper frontmatter, and cross-link to related notes. A note that doesn't link to anything is an island — every new note should connect to the graph.

## Vault Structure (where things go)

| Type | Folder | When to use |
|---|---|---|
| Active project | `10 - Projects/` | Has a goal, target date, and owner — always built from `90 - Templates/Project Note.md` |
| Ongoing responsibility / domain | `20 - Areas/` | No end date — ongoing work or knowledge domain |
| Direct report | `20 - Areas/Direct Reports/` | Person who reports to the vault owner |
| Vendor partner | `20 - Areas/Vendor Partners/` | Key vendor/supplier worth running context on |
| Key contact | `20 - Areas/Key Contacts/` | Regular external contact worth running context |
| Reference material | `30 - Resources/` | Article, vendor doc, framework, external reference |
| Distilled knowledge | `35 - Techniques/` | Generalizable lesson, process, or framework from experience |
| Meeting capture | `50 - Meeting Notes/` | Time-stamped meeting notes |
| Web clip / captured content | `05 - Clippings/` | Raw capture of a web page or external content, not yet processed into a Resource or Technique |

## Step 1: Determine note type and location

Ask or infer from context:
- Is this actionable with a deadline? → `10 - Projects/`
- Is this ongoing with no end date? → `20 - Areas/`
- Is this a lesson or framework extracted from experience? → `35 - Techniques/`
- Is this reference material being saved? → `30 - Resources/`
- Is this a raw capture of a web page or external content, not yet distilled? → `05 - Clippings/`

## Step 2: Read the relevant template

Templates live in `90 - Templates/`. Read the appropriate template before writing the note — don't rely on a schema written into this skill, since it can drift from the real template. Known templates:
- `90 - Templates/Project Note.md` — for Projects (always use this one; see Step 3)
- `90 - Templates/Technique.md` — for Techniques
- `90 - Templates/Area Note - Direct Report.md` — for direct reports
- `90 - Templates/Area Note - Vendor Partner.md` — for vendor partners
- `90 - Templates/Area Note - Key Contact.md` — for key contacts
- Check `90 - Templates/` for any other note type not listed here

## Step 3: Create the note with proper frontmatter

**Project notes:** Read `90 - Templates/Project Note.md` in full and use its frontmatter and section structure exactly — including its `<% tp... %>` Templater fields (fill `title` and `date-created` yourself; strip the Templater syntax since notes are being created directly, not via the Templater plugin). Do not use a hand-written frontmatter block for projects; the template is the source of truth and this skill should never hold its own copy that can go stale.

**Technique frontmatter:**
```yaml
---
type: technique
title: ""
area: [[]]
date-created: YYYY-MM-DD
last-updated: YYYY-MM-DD
tags: [Technique]
---
```

**Person (direct report) frontmatter:**
```yaml
---
type: person
role: ""
reports-to: "[Your Name]"
tags: [DirectReport]
last-updated: YYYY-MM-DD
---
```

**Vendor partner frontmatter:**
```yaml
---
type: area-vendor
name: ""
company: ""
products: []
account-team: []
renewal-date: [YYYY-MM-DD if known]
tags: [VendorPartner]
last-updated: YYYY-MM-DD
---
```

**Key contact frontmatter:**
```yaml
---
type: area-contact
name: ""
role: ""
org: ""
affiliation: ""   # your org / a partner org / external
tags: [KeyContact]
last-updated: YYYY-MM-DD
---
```

## Step 4: Add cross-links

Two different linking patterns are in play — use the right one, don't default to outbound everywhere:

**Inbound (antifragile) — use this whenever the target note's template has a Dataview query keyed on backlinks.** `90 - Templates/Project Note.md`'s "Related Meeting Notes" and "Open Action Items" sections are both queries like `WHERE contains(file.outlinks, this.file.link)` — they auto-populate from any note that links *to* the project, and need zero maintenance inside the project note itself. This is why every Meeting Note should carry a `[[Project Name]]` link near the top: that single link is what makes the note show up in the project automatically, forever, with no one having to remember to update a list. Do not hand-maintain a manual list of meeting notes or action items inside a project note to substitute for this — it's redundant with the query and will silently go stale the first time someone forgets to update it. If you're creating a note that references an existing Project (a Meeting Note, a new Direct Report note, etc.), your job is to add the inbound link on *that* note, not to go edit the project.

**Outbound (manual) — use this only for relationships Dataview can't auto-discover**, i.e. anything without a backlink-driven query: project-to-project relationships, links to relevant Area notes, or Techniques linking back to their source Project/Meeting Notes. Add a `See Also:` or `Related:` section with `[[wikilinks]]` for these. This is the fragile pattern — it only works if someone remembers to add and update it — so reach for it only when there's no inbound alternative.

## Step 5: Write the note

Follow the template structure. Fill in what's known; mark unknowns explicitly as `[to confirm]` rather than leaving blanks or guessing.

## Rules
- Never create a note without at least one cross-link to an existing note
- Filenames should be plain English, no date prefixes (except Meeting Notes)
- Don't duplicate existing notes — search first with `search_notes` before creating
- For Techniques: name by the generalizable skill, not the specific project (e.g., `Structuring a Multi-Phase Strategy Engagement.md` not `Project X Lessons.md`)
- Always set `last-updated` to today's date
- When creating a Meeting Note, always include a `[[Entity Name]]` wikilink to every Project, direct report, vendor partner, or key contact it concerns — not just people/vendors. Project notes surface their meeting history the same backlink-driven way Direct Report/Vendor/Contact notes do (see the inbound-link pattern in Step 4), so a missing project link means the meeting silently never shows up in that project's "Related Meeting Notes." Put the link near the top (e.g. `Related:` or `**Person:**`/`**Vendor:**`/`**Contact:**`) so it's guaranteed regardless of what else gets filled in.
- Vendor Partner and Key Contact notes: create from `90 - Templates/Area Note - Vendor Partner.md` and `90 - Templates/Area Note - Key Contact.md`
