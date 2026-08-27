# 30 - Resources

Reference material not tied to a specific active project — articles, vendor docs, frameworks, and research output.

- **`Research Briefs/`** — Decision Briefs produced by the `autoresearch` skill (`YYYY-MM-DD - [Topic].md`).
- **`Research Briefs/Sources/`** — individual source pages `autoresearch` creates while researching, so every claim in a brief traces back to something.

**Resource frontmatter convention:**
```yaml
type: research-brief | source | resource
source: "[domain or publisher]"
tags: [Resource, ResearchBrief | Source]
last-updated: YYYY-MM-DD
```

**Used by:** `autoresearch` (both subfolders), `knowledge-retrieval` (reads). Delete the `Research Briefs/` subfolders specifically if you're not installing `autoresearch` — you can still keep `30 - Resources/` itself for general reference material.
