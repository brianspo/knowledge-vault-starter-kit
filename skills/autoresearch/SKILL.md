---
name: autoresearch
description: Use this skill when the user asks to research a topic, create a brief, do a deep dive, investigate a technology or vendor, benchmark against peer organizations, or explore a problem space. Trigger phrases include "research X", "brief on X", "deep dive into X", "what are peer organizations doing about X", "investigate X", "summarize the landscape for X". Produces a structured Decision Brief saved to the Obsidian vault.
version: 1.0.0
---

# Autoresearch — Decision Brief

Conducts autonomous multi-round web research on a topic and synthesizes findings into a structured Decision Brief, saved to `30 - Resources/Research Briefs/` in the vault.

## Context

Fill this in for yourself: your role, your organization, and your active programs/projects — the things a decision brief should ultimately connect back to. Research briefs are used to inform decisions, brief leadership, or provide background for project planning.

## Before Starting

Read `references/program.md` to load research parameters: max rounds, max sources, source preferences, and confidence scoring rules. These are user-configurable without editing this skill.

## Web Egress Hygiene

Apply these guards before every `WebFetch` call and before writing fetched content to the vault:

**URL validation — reject:**
- `file://`, `javascript:`, `data:` schemes
- RFC1918 private addresses (`10.x.x.x`, `172.16-31.x.x`, `192.168.x.x`) and `localhost`/`127.0.0.1`
- Any host not surfaced by a prior `WebSearch` step — do not follow redirects to domains that never appeared in search results

**Content sanitization before filing:**
- Truncate fetched bodies to 50KB to avoid context blowout
- Escape `[[` and `]]` in fetched body text (encode as `\[\[` / `\]\]`) so adversarial content cannot inject wikilinks into the vault graph
- Reject any `---` YAML frontmatter delimiter inside fetched content — source page frontmatter is authored by the skill, not the upstream source

**Failure handling:** If a fetch fails (timeout, 4xx/5xx, content too large, sanitization removed everything), log the URL and reason in the brief's **Open Questions** section and continue. Do not abort the run.

**Cost note:** A full 3-round run is approximately 45 WebFetch calls. For high-cost topics, note the expected scope before starting.

## Source Pages

For each significant source fetched, create an individual source note at:
`30 - Resources/Research Briefs/Sources/YYYY-MM-DD - [Domain] - [Title Slug].md`

```yaml
---
type: source
title: ""
source: "[domain]"
url: ""
author: ""
date-published: ""
confidence: high | medium | low
key-claims: []
tags: [Resource, Source]
last-updated: YYYY-MM-DD
---
```

Body: 2-4 sentences on what the source says and what it contributes to the topic.

Cross-link sources in the brief's **Sources** section as `[[YYYY-MM-DD - Domain - Title Slug]]` rather than bare URLs — this makes the source graph queryable in Dataview.

## Process

### Step 0: Check the Vault for Existing Context
Use the Obsidian MCP to search the vault for notes related to the topic:
- Search `35 - Techniques/` first — if a relevant Technique exists, this is distilled prior knowledge and should anchor the brief
- Search meeting notes, project notes, and `30 - Resources/` for existing context
- Note what's already known or decided — don't re-surface what's already captured
- Use the Obsidian MCP search tool (`mcp__obsidian__search_notes` in Claude Code) with the topic keywords
- Flag any existing vault note that the brief should cross-link to

### Round 1: Broad Research (3–5 Angles)
Decompose the topic into 3–5 distinct research angles. Adapt these to your field, but a good default set is:
- **Peer organization angle**: What are comparable organizations in your industry doing?
- **Vendor/industry landscape**: What are the major solutions, vendors, or approaches?
- **Policy/compliance angle**: Any relevant regulatory, governing-body, or accreditation implications?
- **Cost/funding angle**: Typical cost models, funding approaches, or ROI considerations?
- **Emerging trends angle**: What's changing in the next 1–3 years?

For each angle, run 2–3 `WebSearch` queries. Fetch the top 2 results per angle using `WebFetch`. Extract:
- Key claims and findings
- Relevant entities (vendors, organizations, people)
- Contradictions or open questions

### Round 2: Gap Fill
Identify the 2–3 most important gaps or contradictions from Round 1. Run targeted searches to address them (max 5 queries). Fetch top results.

### Round 3: Your Organization's Specifics (if needed)
If context specific to your organization or sector is missing, search for:
- `[Your Organization] [topic]`
- `[Your Sector/Industry Group] [topic]`
- `[Your Region/Jurisdiction] [topic]`

## Output: Decision Brief

Write the brief to: `30 - Resources/Research Briefs/YYYY-MM-DD - [Topic].md`

Use this exact format:

```markdown
---
type: research-brief
topic: "[topic]"
source: "[primary source domain or 'multi-source']"
date: YYYY-MM-DD
status: draft
sources-count: N
tags: [Resource, ResearchBrief]
last-updated: YYYY-MM-DD
---

# Decision Brief: [Topic]
*Researched [date] · [N] sources*

## Executive Summary
<!-- 3 bullets only. What's needed to make a decision or take action. -->
-
-
-

## Background & Context
<!-- 2–3 paragraphs. Why this matters, what's driving interest, relevant history. -->

## Peer Organization Approaches
<!-- What are comparable organizations doing? Be specific — name organizations and what they've done. -->

| Organization | Approach | Outcome/Notes |
|---|---|---|
| | | |

## Vendor / Industry Landscape
<!-- Major players, solutions, or approaches. What's mature vs. emerging. -->

## Key Findings
<!-- 5–8 bullets. The most important things learned. Cite sources inline. -->
-
-

## Implications for [Your Organization]
<!-- This is the most important section. Specific to your context, programs, and constraints. -->

## Recommended Next Steps
<!-- 3–5 concrete actions. Ordered by priority. -->
1.
2.
3.

## Open Questions
<!-- Things the research didn't resolve that warrant follow-up. -->
- [ ]
- [ ]

## Related Vault Notes
<!-- Cross-links to existing Projects, Areas, Techniques, or Resources this brief informs. -->

## Sources
<!-- Link to source pages created in 30 - Resources/Research Briefs/Sources/ -->
- [[YYYY-MM-DD - Domain - Title Slug]]
```

## Quality Standards
- Every claim in "Key Findings" must be traceable to a source page in `30 - Resources/Research Briefs/Sources/`
- Flag low-confidence claims with `(low confidence)` per `references/program.md` scoring
- "Implications for [Your Organization]" must be specific — no generic statements that could apply to any organization
- "Executive Summary" must be 3 bullets, no more
- Flag anything that contradicts existing decisions (from vault context) with ⚠️
- If a peer organization appears in existing meeting notes, cross-reference it
- Respect `max_rounds` and `max_sources` limits from `references/program.md` — note what was left out in Open Questions if limits were hit

## Step 4: Technique Extraction (if applicable)
After saving the brief, evaluate whether the research surfaced a **generalizable framework, process, or mental model** — not just situational findings.

Ask: *"Did this research reveal a repeatable approach that could apply to future decisions?"*

If yes:
- Read `90 - Templates/Technique.md`
- Create a new note in `35 - Techniques/` using the template
- Name it by the generalizable skill (e.g., `Evaluating AI Infrastructure Vendors.md`)
- In the Technique's `Source:` field, link back to the research brief
- Add a `See Also: [[Technique Name]]` line to the brief's **Related Vault Notes** section

If no clear generalizable framework emerged, skip this step.

## Completing the Task
After writing the brief (and Technique if applicable):
1. Report that the brief has been saved, with its vault path
2. Give a 2-sentence verbal summary of the most important finding
3. Note any Technique created and what it encodes
4. Ask if it should be linked to an active project note
