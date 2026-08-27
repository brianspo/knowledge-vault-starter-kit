---
type: project
title: "<% tp.system.prompt('Project name') %>"
status: active
owner: "[Your Name]"
jira: ""
target-date: ""
date-created: <% tp.date.now("YYYY-MM-DD") %>
last-updated: <% tp.date.now("YYYY-MM-DD") %>
---

# <% tp.system.prompt('Project name') %>

## What Success Looks Like
<!-- One paragraph. If you can't write this, the project isn't scoped yet. -->

## Current Status
<!-- Update this in place — it's always the current state, not a log -->

**As of <% tp.date.now("YYYY-MM-DD") %>:**

## Key Stakeholders

| Name | Role | What They Need From This |
|---|---|---|
| | | |

## Decisions Log
<!-- Add decisions as they're made. Date each one. -->

| Date | Decision | Who | Rationale |
|---|---|---|---|
| | | | |

## Open Questions

- [ ]
- [ ]

## Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| | | | |

## Related Meeting Notes
```dataview
LIST
FROM "50 - Meeting Notes"
WHERE contains(file.name, this.title) OR contains(file.outlinks, this.file.link)
SORT file.mtime DESC
```

## Open Action Items Across All Related Notes
```dataview
TASK
WHERE !completed
AND (contains(file.name, this.title) OR contains(file.outlinks, this.file.link))
SORT file.mtime ASC
```

## Resources & Reference Links

-
