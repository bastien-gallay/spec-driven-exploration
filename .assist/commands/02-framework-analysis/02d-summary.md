---
name: framework-analysis-summary
description: Write executive summary and conclusions for a framework
arguments:
  - name: framework
    description: Framework name (spec-kit, bmad, openspec)
    required: true
outputs:
  - path: docs/framework-analyses/{framework}/summary/executive-summary.md
  - path: docs/framework-analyses/{framework}/summary/conclusions.md
status_file: .assist/status/framework-analyses/{framework}.yaml
---

# Framework Analysis: Summary

Write the executive summary and conclusions for the framework analysis.

## Prerequisites

- Descriptions step completed (`stages.descriptions.philosophy: completed`)
- All prior analysis steps completed

## Context Loading

1. Read `.assist/status/framework-analyses/{framework}.yaml`
2. Verify descriptions stage is completed
3. Read all prior analysis outputs:
   - `documents/key-sources.md`
   - `documents/reading-notes.md`
   - `glossaries/glossary.yaml`
   - `glossaries/artifact-taxonomy.yaml`
   - `glossaries/concept-mapping.yaml`
   - `descriptions/philosophy.md`
   - `descriptions/workflow.md`
   - `descriptions/context-organization.md`
   - `descriptions/specific-features.md`

## Task 1: Executive Summary (executive-summary.md)

Write a high-level summary of the framework for quick understanding.

### Content Structure

```markdown
# Executive Summary - {framework}

## Overview

2-3 paragraph summary of what this framework is and does.

## Key Characteristics

| Aspect | Description |
|--------|-------------|
| Philosophy | One-liner |
| Primary Workflow | One-liner |
| Key Artifact | One-liner |
| Target User | One-liner |
| Complexity | Low/Medium/High |

## Strengths

- Strength 1: Brief explanation
- Strength 2: Brief explanation
- Strength 3: Brief explanation

## Considerations

- Consideration 1: Brief explanation
- Consideration 2: Brief explanation

## Best Suited For

Describe ideal use cases in 2-3 sentences.

## Quick Start Path

1. First thing to do
2. Second thing to do
3. Third thing to do
```

## Task 2: Conclusions (conclusions.md)

Write analytical conclusions about the framework.

### Content Structure

```markdown
# Conclusions - {framework}

## Analysis Summary

Brief summary of what was analyzed.

## Key Findings

### Finding 1: {Title}

Detailed explanation with evidence from analysis.

### Finding 2: {Title}

...

## Unique Value Proposition

What makes this framework distinctive?

## Limitations

### Limitation 1: {Title}

Explanation and context.

## Comparison Position

Where this framework sits relative to alternatives:

- More structured than: ...
- Less opinionated than: ...
- Similar in scope to: ...

## Recommendations

### Use This Framework When

- Condition 1
- Condition 2

### Consider Alternatives When

- Condition 1
- Condition 2

## Open Questions

Questions that remain after analysis.

## Sources

Key sources that informed these conclusions.
```

## Status Update

After completing both files, update the status:

```yaml
stages:
  summary:
    executive_summary:
      status: completed
      last_updated: {current_datetime}
    conclusions:
      status: completed
      last_updated: {current_datetime}

overall_completion: 100
ready_for_cross_analysis: true
```

## Quality Checklist

- [ ] Executive summary is readable in < 2 minutes
- [ ] Key characteristics table is complete
- [ ] Strengths and considerations are balanced
- [ ] Conclusions are evidence-based
- [ ] Recommendations are actionable
- [ ] No jargon without definition
- [ ] Status file updated with 100% completion
- [ ] `ready_for_cross_analysis: true` set
