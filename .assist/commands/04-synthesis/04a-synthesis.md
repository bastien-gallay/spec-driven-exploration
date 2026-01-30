---
name: synthesis
description: Write cross-cutting conclusions and recommendations
arguments: []
outputs:
  - path: docs/cross-analyses/summary/synthesis.md
  - path: docs/cross-analyses/summary/recommendations.md
status_file: .assist/status/cross-analyses/synthesis.yaml
---

# Synthesis

Write cross-cutting conclusions and recommendations based on all analyses.

## Prerequisites

All cross-comparison analyses must be complete:

- By-theme analysis: `overall_completion: 100` in by-theme.yaml
- Pairwise analysis: `overall_completion: 100` in pairwise.yaml

## Context Loading

1. Read all status files to verify prerequisites
2. Load all cross-analysis files:
   - `docs/cross-analyses/by-theme/*.md`
   - `docs/cross-analyses/pairwise/*.md`
3. Load executive summaries from all three frameworks
4. Load conclusions from all three frameworks

## Task 1: Synthesis (synthesis.md)

Write the overarching synthesis of all findings.

### Content Structure

```markdown
# Synthesis: Spec-Driven Development Frameworks

## Executive Overview

High-level summary of the entire analysis effort.

### Scope

What was analyzed and why.

### Methodology

How the analysis was conducted.

## Cross-Cutting Themes

### Theme 1: The Spectrum of Structure

How frameworks balance structure vs flexibility...

- spec-kit: High structure (constitution, articles)
- BMAD: Medium structure (personas, checklists)
- OpenSpec: Low structure (flexible proposals)

### Theme 2: Agent Models

How frameworks conceptualize AI agents...

### Theme 3: Human-AI Collaboration

How frameworks handle the human role...

### Theme 4: Artifact Strategy

How frameworks organize deliverables...

## Key Insights

### Insight 1: {Title}

Detailed explanation supported by evidence from the analysis.

### Insight 2: {Title}

...

### Insight 3: {Title}

...

## The SDD Landscape

### Positioning Map

```text
                    Structured
                        │
                        │  spec-kit
                        │
    Solo ────────────────┼──────────────── Team
                        │
              OpenSpec  │    BMAD
                        │
                    Flexible
```

### Evolution Trends

Where the field is heading based on these frameworks.

## Open Questions

Questions that emerged from the analysis.

1. Question 1
2. Question 2

## Limitations of This Analysis

What this analysis does and doesn't cover.

## Sources

Key sources across all frameworks.
```

## Task 2: Recommendations (recommendations.md)

Write actionable recommendations for practitioners.

### Content Structure

```markdown
# Recommendations

## How to Use This Guide

Instructions for readers.

## Framework Selection Guide

### Decision Tree

```text
Start
  │
  ├─ Solo developer?
  │   ├─ Yes → Need strict governance?
  │   │         ├─ Yes → spec-kit
  │   │         └─ No → OpenSpec
  │   └─ No → Team size?
  │           ├─ Small (2-5) → BMAD lite or spec-kit
  │           └─ Large (5+) → BMAD
  │
  └─ ...
```

### Quick Reference

| If You Need... | Consider | Because |
|----------------|----------|---------|
| Strict TDD | spec-kit | Constitution enforces it |
| Team roles | BMAD | Personas define roles |
| Flexibility | OpenSpec | Minimal constraints |
| ... | ... | ... |

## Getting Started Paths

### For Solo Developers

1. Recommendation
2. Recommendation

### For Small Teams

1. Recommendation
2. Recommendation

### For Large Organizations

1. Recommendation
2. Recommendation

## Adoption Strategies

### Starting Fresh

How to adopt a framework for a new project.

### Migrating

How to migrate from one approach to another.

### Hybrid Approaches

How to combine elements from multiple frameworks.

## Best Practices

### Universal Best Practices

Practices that apply regardless of framework choice.

1. Best practice 1
2. Best practice 2

### Framework-Specific Tips

#### spec-kit

- Tip 1
- Tip 2

#### BMAD

- Tip 1
- Tip 2

#### OpenSpec

- Tip 1
- Tip 2

## Anti-Patterns

### Anti-Pattern 1: {Name}

Description and how to avoid.

### Anti-Pattern 2: {Name}

...

## Future Considerations

What to watch for as the field evolves.
```

## Status Update

After completing both files, update the status:

```yaml
stages:
  synthesis:
    cross_cutting_conclusions:
      status: completed
    recommendations:
      status: completed

overall_completion: 100
```

## Quality Checklist

- [ ] Synthesis draws from all prior analyses
- [ ] Insights are novel (not just repetition)
- [ ] Recommendations are actionable
- [ ] Decision tree is practical
- [ ] Anti-patterns are useful
- [ ] No framework unfairly favored
- [ ] Status file updated
