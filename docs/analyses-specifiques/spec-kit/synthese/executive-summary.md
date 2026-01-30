# Executive Summary - spec-kit

## Framework Identity

**spec-kit** is a Python CLI tool implementing Specification-Driven Development
(SDD), where specifications drive code generation rather than the reverse.

| Attribute | Value |
|-----------|-------|
| Version Analyzed | Commit `9111699` (2025-01-30) |
| Primary Language | Python CLI |
| Core Philosophy | Specifications as primary artifact |
| Target Projects | Greenfield and iterative enhancement |

## Core Differentiators

### Constitutional Governance

9 articles defining immutable architectural DNA:

- **Library-First**: Features as standalone libraries
- **Test-First Imperative**: Non-negotiable TDD
- **CLI Interface Mandate**: Text I/O, JSON support
- **Simplicity**: Maximum 3 projects initially
- **Integration-First Testing**: Real databases over mocks

### Template-Driven Quality Control

Templates constrain LLM behavior:

- Focus on WHAT, not HOW
- `[NEEDS CLARIFICATION]` markers (max 3)
- Pre-implementation gates
- Quality checklists

### 7-Step Sequential Workflow

1. Constitution establishment
2. Specification creation
3. Clarification
4. Plan generation
5. Cross-artifact analysis
6. Task breakdown
7. Implementation

## Key Strengths

| Strength | Description |
|----------|-------------|
| Principled | Constitution enforces standards |
| Quality-focused | Test-first, integration-first |
| Clarification-first | Resolve ambiguity before planning |
| Multi-agent support | Works with 20+ AI agents |
| Cross-platform | Bash and PowerShell scripts |

## Artifact Overview

| Category | Artifacts |
|----------|-----------|
| Governance | Constitution |
| Specification | spec.md, research.md |
| Design | plan.md, data-model.md, contracts/ |
| Execution | tasks.md |

## Workflow Approach

- **Sequential commands**: `/speckit.specify`, `/speckit.plan`, etc.
- **Constitution gates**: Pre-implementation validation
- **Clarification loop**: Max 10 questions, max 5 per round
- **Analysis pass**: 6 detection categories

## Best Fit Scenarios

| Scenario | Fit |
|----------|-----|
| New projects (greenfield) | Excellent |
| Teams valuing TDD | Excellent |
| Projects needing governance | Excellent |
| Quick prototyping | Moderate |
| Brownfield development | Moderate |

## Quick Start Path

```bash
1. uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
2. specify init <PROJECT_NAME>
3. /speckit.constitution
4. /speckit.specify <description>
5. /speckit.clarify
6. /speckit.plan
7. /speckit.tasks
8. /speckit.implement
```

## Sources

- [README.md](../../references/spec-kit/README.md)
- [Spec-Driven Philosophy](../../references/spec-kit/spec-driven.md)
