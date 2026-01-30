---
name: framework-analysis-descriptions
description: Document philosophy, workflow, context organization, and specific features
arguments:
  - name: framework
    description: Framework name (spec-kit, bmad, openspec)
    required: true
outputs:
  - path: docs/framework-analyses/{framework}/descriptions/philosophy.md
  - path: docs/framework-analyses/{framework}/descriptions/workflow.md
  - path: docs/framework-analyses/{framework}/descriptions/context-organization.md
  - path: docs/framework-analyses/{framework}/descriptions/specific-features.md
status_file: .assist/status/framework-analyses/{framework}.yaml
---

# Framework Analysis: Descriptions

Write detailed descriptions of the framework's philosophy, workflow, and features.

## Prerequisites

- Glossaries step completed (`stages.glossaries.glossary: completed`)
- Read the glossary and artifact taxonomy for terminology

## Context Loading

1. Read `.assist/status/framework-analyses/{framework}.yaml`
2. Verify glossaries stage is completed
3. Load glossary from `docs/framework-analyses/{framework}/glossaries/glossary.yaml`
4. Load taxonomy from `docs/framework-analyses/{framework}/glossaries/artifact-taxonomy.yaml`

## Task 1: Philosophy (philosophy.md)

Document the framework's core philosophy and principles.

### Content Structure

```markdown
# Philosophy - {framework}

## Core Principles

What fundamental beliefs drive this framework?

### Principle 1: {Name}

- Description
- How it manifests in the framework
- Implications for users

## Design Goals

What problems does this framework solve?

- Goal 1
- Goal 2

## Target Audience

Who is this framework for?

## Trade-offs

What trade-offs does this framework make?

| Optimizes For | At the Cost Of |
|---------------|----------------|
| X | Y |

## Sources

- [Source 1](path)
```

## Task 2: Workflow (workflow.md)

Document the framework's workflow and process.

### Content Structure

```markdown
# Workflow - {framework}

## Overview

High-level description of the workflow.

## Stages

### Stage 1: {Name}

- **Input**: What you need to start
- **Process**: What happens
- **Output**: What you produce
- **Command/Action**: How to invoke

### Stage 2: {Name}

...

## Workflow Diagram

```text
[Stage 1] → [Stage 2] → [Stage 3]
    ↓           ↓
[Artifact]  [Artifact]
```

## Decision Points

Where does the user make choices?

## Iteration Patterns

How does work loop back?

## Sources

- [Source 1](path)
```

## Task 3: Context Organization (context-organization.md)

Document how the framework organizes project context.

### Content Structure

```markdown
# Context Organization - {framework}

## Directory Structure

```text
project-root/
├── directory/
│   └── file
```

## File Naming Conventions

| Pattern | Purpose |
|---------|---------|
| pattern | purpose |

## Context Persistence

How does the framework maintain context across sessions?

## Memory/State Management

What persists vs what is ephemeral?

## Context Loading Strategy

How does the framework load context at start of session?

## Sources

- [Source 1](path)
```

## Task 4: Specific Features (specific-features.md)

Document unique or notable features of the framework.

### Content Structure

```markdown
# Specific Features - {framework}

## Feature 1: {Name}

### Description

What is this feature?

### How It Works

Technical explanation.

### Benefits

Why this feature matters.

### Example Usage

```
Example code or command
```

## Feature 2: {Name}

...

## Comparison Notes

How these features compare to alternatives.

## Sources

- [Source 1](path)
```

## Status Update

After completing all four files, update the status:

```yaml
stages:
  descriptions:
    philosophy:
      status: completed
      last_updated: {current_datetime}
    workflow:
      status: completed
      last_updated: {current_datetime}
    context_organization:
      status: completed
      last_updated: {current_datetime}
    specific_features:
      status: completed
      last_updated: {current_datetime}
```

## Quality Checklist

- [ ] Philosophy captures core beliefs
- [ ] Workflow covers all stages end-to-end
- [ ] Directory structure is accurate
- [ ] Features are specific and concrete
- [ ] Terminology matches glossary
- [ ] Sources cited for all claims
- [ ] Status file updated
