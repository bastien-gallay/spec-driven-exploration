---
name: cross-comparisons-pairwise
description: Compare frameworks in pairs for detailed analysis
arguments: []
outputs:
  - path: docs/cross-analyses/pairwise/spec-kit-vs-bmad.md
  - path: docs/cross-analyses/pairwise/spec-kit-vs-openspec.md
  - path: docs/cross-analyses/pairwise/bmad-vs-openspec.md
status_file: .assist/status/cross-analyses/pairwise.yaml
---

# Cross-Comparisons: Pairwise

Compare frameworks in pairs for detailed side-by-side analysis.

## Prerequisites

All framework analyses must be complete:

- `ready_for_cross_analysis: true` in each framework status file

## Context Loading

1. Read all three framework status files
2. Verify all are ready for cross-analysis
3. Load executive summaries from all three frameworks
4. Load concept mappings from all three frameworks

## Comparison 1: spec-kit vs BMAD (spec-kit-vs-bmad.md)

### Content Structure

```markdown
# Pairwise Comparison: spec-kit vs BMAD

## Overview

| Aspect | spec-kit | BMAD |
|--------|----------|------|
| Philosophy | Specification-first | Agent collaboration |
| Complexity | Medium | High |
| Target | Solo developers | Teams |

## Key Similarities

### Similarity 1: {Title}

Both frameworks...

## Key Differences

### Difference 1: Agent Model

**spec-kit**: Single agent with commands
**BMAD**: Multiple specialized personas

Implications:
- ...

### Difference 2: Governance

**spec-kit**: Formal constitution with articles
**BMAD**: Informal personas and checklists

Implications:
- ...

### Difference 3: {Title}

...

## Concept Mapping

| spec-kit | BMAD | Match Level |
|----------|------|-------------|
| Constitution | Personas | Low |
| Feature Spec | PRD | Partial |
| ... | ... | ... |

## Use Case Comparison

| Use Case | Better Choice | Why |
|----------|---------------|-----|
| Solo project | spec-kit | Simpler, less overhead |
| Team project | BMAD | Role clarity |
| ... | ... | ... |

## Migration Considerations

### spec-kit → BMAD

What to expect when migrating...

### BMAD → spec-kit

What to expect when migrating...

## Conclusions

Summary of when to choose each.
```

## Comparison 2: spec-kit vs OpenSpec (spec-kit-vs-openspec.md)

### Content Structure

```markdown
# Pairwise Comparison: spec-kit vs OpenSpec

## Overview

| Aspect | spec-kit | OpenSpec |
|--------|----------|----------|
| Philosophy | Constitution-driven | Proposal-driven |
| Complexity | Medium | Low |
| Strictness | High (articles) | Flexible |

## Key Similarities

...

## Key Differences

...

## Concept Mapping

...

## Use Case Comparison

...

## Migration Considerations

...

## Conclusions

...
```

## Comparison 3: BMAD vs OpenSpec (bmad-vs-openspec.md)

### Content Structure

```markdown
# Pairwise Comparison: BMAD vs OpenSpec

## Overview

| Aspect | BMAD | OpenSpec |
|--------|------|----------|
| Philosophy | Multi-agent | Incremental |
| Complexity | High | Low |
| Collaboration | Strong | Minimal |

## Key Similarities

...

## Key Differences

...

## Concept Mapping

...

## Use Case Comparison

...

## Migration Considerations

...

## Conclusions

...
```

## Status Update

After completing all pairwise comparisons, update the status:

```yaml
stages:
  comparisons:
    spec-kit_vs_bmad:
      status: completed
    spec-kit_vs_openspec:
      status: completed
    bmad_vs_openspec:
      status: completed

overall_completion: 100
```

## Quality Checklist

- [ ] Each comparison is balanced (not favoring one)
- [ ] Similarities acknowledged before differences
- [ ] Differences explained with implications
- [ ] Concept mapping references glossaries
- [ ] Use cases are practical
- [ ] Migration guidance is actionable
- [ ] Status file updated
