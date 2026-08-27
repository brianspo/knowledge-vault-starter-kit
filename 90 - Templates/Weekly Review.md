---
type: weekly-review
week: <% tp.date.now("YYYY-[W]WW") %>
date: <% tp.date.now("YYYY-MM-DD") %>
---

# Week of <% tp.date.now("MMMM D, YYYY") %> — Weekly Review

## What Moved This Week
<!-- 3-5 things that actually advanced. Be specific. -->
-
-
-

## What Didn't Move (and Why)
<!-- Honest accounting. Blocked? Deprioritized? Dropped? -->
-

## Open Action Items
<!-- Dataview pulls your unchecked tasks from all notes this week -->
```dataview
TASK
WHERE !completed
AND file.mtime >= date(today) - dur(7 days)
SORT file.name ASC
```

## Program Status Snapshot

| Program | Status | Next Milestone | Owner |
|---|---|---|---|
| [Project A] | 🟡 | | |
| [Project B] | 🟡 | | |
| [Project C] | 🔴 | | |

<!-- 🟢 On track  🟡 Watch  🔴 At risk -->

## Decisions I Made This Week
<!-- Record these — they're easy to forget and important to explain later -->
-

## What I Learned
<!-- One thing — from a meeting, an article, a conversation. Even if small. -->

## Next Week's Top 3 Priorities
1.
2.
3.

## One Thing to Unblock
<!-- Pick one thing that will unstick something for someone else on your team -->

## Personal Pulse
<!-- Brief, honest: energy level, stress, what needs attention -->
