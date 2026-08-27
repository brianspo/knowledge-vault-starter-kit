# autoresearch — Program Configuration

User-configurable parameters for the autoresearch skill. Edit this file to tune research behavior without modifying the skill itself.

## Research Depth

```
max_rounds: 3          # Maximum research rounds (1=fast, 3=thorough)
max_sources: 15        # Maximum sources to fetch per session
max_source_size: 50KB  # Truncate fetched pages beyond this size
```

## Source Preferences

Replace this list with the source hierarchy that matters in your field. A generic starting point:

1. `.edu` / `.gov` domains (research institutions, government sources) where relevant to your sector
2. Your sector's governing body or association publications
3. Recognized analyst firms (Gartner, Forrester, or your field's equivalent)
4. Government/regulatory/policy sources relevant to your jurisdiction
5. Major vendor documentation
6. News/trade press specific to your industry

Deprioritize:
- Anonymous blogs or forums without institutional affiliation
- Vendor marketing pages without technical substance
- Sources older than 3 years (unless foundational/policy)

## Confidence Scoring

Rate each source:
- **High**: Peer-reviewed, official policy, named organization case study
- **Medium**: Trade press with named sources, vendor white paper with methodology
- **Low**: Blog, opinion piece, undated content

Flag Low-confidence claims with `(low confidence)` in Key Findings.

## Domain Constraints

Replace with your own required angle, e.g. "Always include a [your sector/region] angle. If no sources specific to that are found, note the gap explicitly in Open Questions rather than extrapolating."

## Source Filing

Save individual source pages to: `30 - Resources/Research Briefs/Sources/`
Format: `YYYY-MM-DD - [Domain] - [Title Slug].md`
