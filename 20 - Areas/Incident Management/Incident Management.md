---
type: area
title: Incident Management
owner: [Your Name]
date-created: YYYY-MM-DD
last-updated: YYYY-MM-DD
---

# Incident Management

## Purpose
Leadership-level notes on significant incidents, post-incident reviews, and lessons learned. This is not a ticket tracker — your ITSM system handles that. This area captures your observations, patterns across incidents, and decisions made at the leadership level that aren't captured elsewhere.

## Notable Incidents

| Date | Ticket | Summary | Note |
|---|---|---|---|
| YYYY-MM-DD | [Ticket #] | [One-line description] | [[Ticket # - Short Title]] |

## Recurring Patterns
<!-- Themes that surface across multiple incidents — update as patterns emerge -->

-

## Open Leadership Questions

- [ ] What is the right escalation threshold for your direct involvement in an active incident vs. delegation to the team?
- [ ] Does your organization have a documented pre-term or pre-event infrastructure readiness checklist?

## Related Meeting Notes
```dataview
LIST
FROM "50 - Meeting Notes"
WHERE contains(file.name, "Incident") OR contains(file.name, "ITS-") OR contains(file.outlinks, this.file.link)
SORT file.mtime DESC
```
