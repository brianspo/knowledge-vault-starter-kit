---
name: knowledge-retrieval
description: Search and retrieve knowledge from the vault (Projects, Areas, Techniques, Resources) before doing external research. Use when asked about a technology, vendor, concept, process, or domain — or when vault context is needed to support another task.
---

# Knowledge Retrieval

Search and synthesize what's already known before going external. Check the vault first — it contains distilled leadership knowledge, active project context, direct report notes, and curated resources. This avoids re-deriving context that's already been captured.

## Vault Structure (PARA + numbered folders)

- **`05 - Clippings/`** — raw web clips and captured content, not yet distilled into a Resource or Technique. Lower-confidence source; check here for recently captured material that hasn't been processed yet.
- **`10 - Projects/`** — active programs with goals, deadlines, decisions, open questions, risks.
- **`20 - Areas/`** — ongoing responsibilities. `20 - Areas/Direct Reports/` has one note per direct report. `20 - Areas/Vendor Partners/` holds running context on key vendors. `20 - Areas/Key Contacts/` holds running context on regular external contacts.
- **`30 - Resources/`** — reference material: articles, vendor docs, frameworks.
- **`35 - Techniques/`** — distilled, generalizable knowledge extracted from experience. Check here for frameworks and lessons learned.
- **`50 - Meeting Notes/`** — transcribed meeting notes, organized by date.
- **`70 - Weekly Reviews/`** — weekly synthesis notes (format: YYYY-WWW.md).

## Step 1: Search the vault

Run targeted searches based on the query:

1. `search_notes` for the key term(s) — project name, person, technology, vendor, concept
2. Check `35 - Techniques/` directly for any relevant distilled knowledge
3. If the query relates to an active project, read the full project note from `10 - Projects/`
4. If the query relates to a direct report, read their note from `20 - Areas/Direct Reports/`; if it relates to a vendor, read `20 - Areas/Vendor Partners/`; if it relates to an external contact, read `20 - Areas/Key Contacts/`
5. Check recent `70 - Weekly Reviews/` for recent context on the topic

## Step 2: Synthesize what's known

Summarize:
- **What's already known** — key facts, decisions, context from vault notes
- **What's actively in motion** — open action items, pending decisions, risks
- **What's missing or stale** — gaps where the vault has nothing or the information is old

## Step 3: Flag for external research

If vault coverage is thin or the question requires current/external information, note:
- What the vault doesn't cover
- Suggested search angles for external research (hand off to a research/autoresearch skill if needed)

## Output format

```
## What I found in your vault

### [Topic]
[2-3 sentences synthesizing what the vault says]

Source notes: [[Note Name]], [[Note Name]]

### Gaps
- [What's missing or would benefit from external research]
```

## Rules
- Always check the vault before external research — never go external first
- Quote vault content accurately; don't interpolate or fill gaps with assumptions
- If the vault has nothing relevant, say so clearly and suggest next steps
- Cross-link related notes when synthesizing — surface connections that may not have been noticed
