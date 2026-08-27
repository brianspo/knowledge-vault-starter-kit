---
name: note-update
description: Update an existing note in the vault — add context from meeting notes, update status, add cross-links, or promote a lesson to a Technique. Use when asked to update a project, direct report, or area note, or when a weekly review surfaces something that should be encoded permanently.
---

# Note Update

Keep existing notes current and well-connected. Notes decay without maintenance — this skill updates status, adds running context, promotes insights to Techniques, and strengthens the knowledge graph by adding missing cross-links.

## Common update scenarios

### 1. Add running context from a meeting
After a significant meeting, update the relevant Project, Direct Report, Vendor Partner, or Key Contact note:
- Add dated context to the "Running Context" or "Recent" section
- Update open questions, decisions, risks, or open items based on what was discussed
- Flag action items that belong to the note's owner
- Ensure the meeting note itself contains a `[[Entity Name]]` wikilink to each person, vendor, and contact it concerns — the context notes pull meeting history via a link-based Dataview query, so a missing link means the meeting won't show up

### 2. Update project status
When a milestone is hit or status changes:
- Update the `status` frontmatter field
- Update the next milestone in the status table
- Archive completed phases under a collapsible section

### 3. Add cross-links
When you notice a note should link to another:
- Add `[[wikilink]]` to the related note in a `See Also:` or `Related:` section
- Update both notes so links are bidirectional where appropriate
- For Techniques: add links from the source Project/Meeting note back to the Technique

### 4. Promote a lesson to a Technique
When a "What I Learned" bullet from a Weekly Review deserves permanent capture:
1. Read `90 - Templates/Technique.md`
2. Create a new note in `35 - Techniques/` using the template
3. Link the Technique back to the Weekly Review and source Project
4. Add a `See Also: [[Technique Name]]` line to the source Project note

### 5. Update direct report, vendor, or contact notes
After a 1:1, vendor meeting, or significant interaction:
- Add dated context under the "Running Context" section
- For direct reports: update "What They Need From Me" if priorities shifted; flag new focus areas or concerns
- For vendors: update contract/renewal details, current engagements, and open items
- For key contacts: update relationship context and open items

## Step 1: Find the note to update

Use `search_notes` or `list_directory` to locate the target note. Read it fully before making changes.

## Step 2: Identify what needs updating

Compare current note content against:
- Recent meeting notes (search `50 - Meeting Notes/` for the past 7 days)
- The explicit request for what to add or change
- Missing cross-links to related notes

## Step 3: Apply updates with `patch_note`

Use `patch_note` with `oldString`/`newString` parameters (NOT `oldContent`/`newContent`).

For dated running context, append to an existing section rather than replacing it:
```
oldString: "## Running Context\n\n"
newString: "## Running Context\n\n**2026-MM-DD** — [what happened]\n\n"
```

Update `last-updated` in frontmatter with today's date.

## Step 4: Check for cross-link opportunities

After updating, search for other notes that should link to this one:
- If you updated a Project, check if related Area or Technique notes should reference it
- If you created a Technique, update the source Project note to link to it
- If a Direct Report note changed, check if the relevant Project notes need updating too

## Rules
- Always read the full note before patching — never patch blind
- Preserve existing structure; add to it, don't replace it
- Dated entries go newest-first within running context sections
- `last-updated` frontmatter must be updated on every edit
- Never delete information without explicit instruction — archive or collapse instead
- For `patch_note`: parameters are `oldString` and `newString`, not `oldContent`/`newContent`
