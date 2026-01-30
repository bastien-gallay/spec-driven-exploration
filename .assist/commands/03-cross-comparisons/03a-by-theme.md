---
name: cross-comparisons-by-theme
description: Compare frameworks across common themes (concepts, workflows, artifacts, roles, tooling)
arguments: []
outputs:
  - path: docs/cross-analyses/by-theme/concepts.md
  - path: docs/cross-analyses/by-theme/workflows.md
  - path: docs/cross-analyses/by-theme/artifacts.md
  - path: docs/cross-analyses/by-theme/roles.md
  - path: docs/cross-analyses/by-theme/tooling.md
status_file: .assist/status/cross-analyses/by-theme.yaml
---

# Cross-Comparisons: By Theme

Compare all three frameworks across common themes.

## Prerequisites

All framework analyses must be complete:

- `ready_for_cross_analysis: true` in each framework status file

## Context Loading

1. Read all three framework status files
2. Verify all are ready for cross-analysis
3. Load glossaries from all three frameworks:
   - `docs/framework-analyses/spec-kit/glossaries/glossary.yaml`
   - `docs/framework-analyses/bmad/glossaries/glossary.yaml`
   - `docs/framework-analyses/openspec/glossaries/glossary.yaml`
4. Load artifact taxonomies from all three
5. Load concept mappings from all three

## Theme 1: Concepts (concepts.md)

Compare core concepts across frameworks.

### Content Structure

```markdown
# Cross-Analysis: Core Concepts

## Overview

How do the frameworks conceptualize spec-driven development?

## Concept Comparison Matrix

| Concept Area | spec-kit | BMAD | OpenSpec |
|--------------|----------|------|----------|
| Governance | Constitution | Personas/Checklists | Config |
| Requirements | Feature Spec | PRD | Proposal + Spec |
| Design | Plan | Architecture | Design |
| ... | ... | ... | ... |

## Deep Dives

### Governance Concepts

How each framework handles project governance...

#### spec-kit
...

#### BMAD
...

#### OpenSpec
...

### Specification Concepts

...

## Terminology Alignment

| Common Term | spec-kit | BMAD | OpenSpec |
|-------------|----------|------|----------|
| Requirement | Feature Spec | PRD | Proposal |
| ... | ... | ... | ... |

## Unique Concepts

### Only in spec-kit
- Concept: explanation

### Only in BMAD
- Concept: explanation

### Only in OpenSpec
- Concept: explanation

## Conclusions

Key insights about conceptual differences.
```

## Theme 2: Workflows (workflows.md)

Compare development workflows.

### Content Structure

```markdown
# Cross-Analysis: Workflows

## Overview

How do the frameworks structure the development process?

## Workflow Comparison

### High-Level Stages

| Stage | spec-kit | BMAD | OpenSpec |
|-------|----------|------|----------|
| 1 | Constitution | Project Brief | Setup |
| 2 | Specify | PRD | Propose |
| ... | ... | ... | ... |

### Workflow Diagrams

#### spec-kit
```text
[diagram]
```

#### BMAD
```text
[diagram]
```

#### OpenSpec
```text
[diagram]
```

## Process Differences

### Linearity vs Iteration
...

### Validation Points
...

### Human Checkpoints
...

## Recommendations

When to use which workflow pattern.
```

## Theme 3: Artifacts (artifacts.md)

Compare produced artifacts.

### Content Structure

```markdown
# Cross-Analysis: Artifacts

## Overview

What documents/files do the frameworks produce?

## Artifact Mapping

| Purpose | spec-kit | BMAD | OpenSpec |
|---------|----------|------|----------|
| Governance | constitution.md | personas/, checklists/ | config |
| Requirements | spec.md | prd.md | proposal.md |
| Design | plan.md | architecture.md | design.md |
| Tasks | tasks.md | stories/ | tasks.md |
| ... | ... | ... | ... |

## Artifact Lifecycle

How artifacts evolve over time in each framework.

## Template Comparison

Comparing what sections each artifact type contains.

## File Organization

How each framework organizes files in the project.

## Conclusions

Insights about artifact strategies.
```

## Theme 4: Roles (roles.md)

Compare agents, personas, and roles.

### Content Structure

```markdown
# Cross-Analysis: Roles

## Overview

How do frameworks define actors in the process?

## Role Comparison

| Role Type | spec-kit | BMAD | OpenSpec |
|-----------|----------|------|----------|
| AI Agent | Single agent | Multiple personas | Single agent |
| Human | User | Stakeholder | User |
| ... | ... | ... | ... |

## Agent Models

### spec-kit
Single-agent model with commands...

### BMAD
Multi-persona model with specialized agents...

### OpenSpec
Single-agent with modes...

## Human Involvement

When and how humans participate.

## Conclusions

Insights about role design.
```

## Theme 5: Tooling (tooling.md)

Compare tooling and integration.

### Content Structure

```markdown
# Cross-Analysis: Tooling

## Overview

How do frameworks integrate with development tools?

## Tooling Comparison

| Aspect | spec-kit | BMAD | OpenSpec |
|--------|----------|------|----------|
| IDE Integration | VS Code | Cursor/VS Code | Cursor |
| Commands | Slash commands | Slash commands | Slash commands |
| Config Format | YAML | Markdown | YAML |
| ... | ... | ... | ... |

## Command Comparison

How commands are invoked and what they do.

## Configuration

How each framework is configured.

## Extensibility

How each framework can be extended.

## Conclusions

Insights about tooling approaches.
```

## Status Update

After completing all theme files, update the status:

```yaml
stages:
  themes:
    concepts:
      status: completed
    workflows:
      status: completed
    artifacts:
      status: completed
    roles:
      status: completed
    tooling:
      status: completed

overall_completion: 100
```

## Quality Checklist

- [ ] All three frameworks covered in each theme
- [ ] Comparison tables are accurate
- [ ] Unique aspects highlighted
- [ ] Conclusions are actionable
- [ ] Cross-references to framework analyses
- [ ] Status file updated
