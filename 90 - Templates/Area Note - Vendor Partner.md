---
type: area-vendor
name: ""
company: ""
products: []
account-team: []
renewal-date: null
date-created: <% tp.date.now("YYYY-MM-DD") %>
last-updated: <% tp.date.now("YYYY-MM-DD") %>
---

# [Company] — Vendor Partner Context

## Overview
**Company:**
**Products / Services:**
**Relationship since:**

## Contract & Commercials
**Contract vehicle:**
**Annual spend:**
**Renewal date:**
**Notes:**

## Account Team & Key Contacts
<!-- Who I actually deal with — reps, SEs, execs. Add [[Key Contact]] links where they have their own note. -->
-

## Current Engagements
<!-- Active work, deployments, escalations, roadmap items that matter -->
1.
2.
3.

## Running Context
<!-- History, preferences, promises made, sensitivities, how the relationship really runs -->

## Open Items

- [ ]

## Related Projects
<!-- [[wikilinks]] to Projects this vendor touches -->
-

## Meeting History
```dataview
TABLE without id file.link AS "Meeting", date AS "Date"
FROM "50 - Meeting Notes"
WHERE contains(file.outlinks, this.file.link)
SORT date DESC
```
