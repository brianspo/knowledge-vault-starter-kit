---
type: dashboard
---

# Dashboard

## Needs Your Review
```dataview
TABLE status, date AS "Staged"
FROM "00 - Inbox"
WHERE type = "staging" AND status = "pending-review"
SORT date DESC
```

## Risks & Flags
<!-- AGENT:daily-update:risks:start -->
_Not yet run._
<!-- AGENT:daily-update:risks:end -->

## Direct-Report Follow-ups Getting Old
<!-- AGENT:daily-update:followups:start -->
_Not yet run._
<!-- AGENT:daily-update:followups:end -->

## Latest Outputs
- News Brief: <!-- AGENT:news-brief -->not yet run<!-- /AGENT -->
- Weekly Review: <!-- AGENT:weekly-review -->not yet run<!-- /AGENT -->
- Accomplishments: <!-- AGENT:accomplishments -->not yet run<!-- /AGENT -->

## Active Projects
```dataview
TABLE status, last-updated AS "Last Updated", target-date AS "Target Date", (date(today) - last-updated).days AS "Days Since Update"
FROM "10 - Projects"
WHERE status = "active"
SORT last-updated ASC
```

## Upcoming Target Dates (next 60 days)
```dataview
TABLE target-date AS "Target Date"
FROM "10 - Projects"
WHERE status = "active" AND target-date AND date(target-date) <= date(today) + dur(60 days)
SORT target-date ASC
```

## Open Commitments — All Direct Reports
```dataview
TABLE WITHOUT ID
  file.link AS "Direct Report",
  T.text AS "Commitment"
FROM "20 - Areas/Direct Reports"
FLATTEN file.tasks AS T
WHERE !T.completed
SORT file.link ASC
```
