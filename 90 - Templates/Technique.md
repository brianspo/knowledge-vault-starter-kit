---
type: technique
title: ""
area: [[]]
date-created: <% tp.date.now("YYYY-MM-DD") %>
last-updated: <% tp.date.now("YYYY-MM-DD") %>
tags: [Technique]
---

# <% tp.file.title %>

## What This Is
[One sentence: what this technique enables you to do in your role]

## Context
[Where and when you learned or developed this — the specific situation that surfaced it]

Source: [[]]

## Approach
[The actual framework, process, or mental model. Use numbered steps or named principles.]

1.
2.
3.

## Key Insights
[What's non-obvious or counter-intuitive — the things that took experience to learn]

-
-

## When to Apply
[Conditions or trigger situations where this technique is useful]

-

## Watch-outs
[Common failure modes, or situations where this approach breaks down]

-

## Outputs / Artifacts
[What this technique produces — deliverables, decisions, or documents]

-

## Related
```dataview
LIST
FROM "10 - Projects" OR "20 - Areas" OR "30 - Resources" OR "50 - Meeting Notes"
WHERE contains(file.outlinks, this.file.link)
SORT file.mtime DESC
```
