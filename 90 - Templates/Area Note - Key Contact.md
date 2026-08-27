---
type: area-contact
name: ""
role: ""
org: ""
affiliation: ""
date-created: <% tp.date.now("YYYY-MM-DD") %>
last-updated: <% tp.date.now("YYYY-MM-DD") %>
---

# [Name] — Key Contact Context

## Who They Are
**Role / Title:**
**Organization:**
**Affiliation:** <!-- your org / a partner org / external -->
**How we connect:**

## Why They Matter
<!-- Their role in my world — what they influence, control, or unblock -->

## Running Context
<!-- History, preferences, ongoing situations, things I need to remember about working with them -->

## What I Need From Them / What They Need From Me

## Open Items

- [ ]

## Related Projects & Areas
<!-- [[wikilinks]] to related notes -->
-

## Meeting History
```dataview
TABLE without id file.link AS "Meeting", date AS "Date"
FROM "50 - Meeting Notes"
WHERE contains(file.outlinks, this.file.link)
SORT date DESC
```
