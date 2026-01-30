# Executive Summary - OpenSpec

## Framework Identity

**OpenSpec** is a TypeScript-based framework for specification-driven
development emphasizing fluid workflows and brownfield development support.

| Attribute | Value |
|-----------|-------|
| Version Analyzed | Commit `3768694` (2025-01-30) |
| Primary Language | TypeScript |
| Core Philosophy | Fluid, iterative, brownfield-first |
| Target Projects | Personal to enterprise, existing codebases |

## Core Differentiators

### Delta Specs for Brownfield

Focus on what's changing, not full specification rewrites:

- `## ADDED Requirements` - New behavior
- `## MODIFIED Requirements` - Changed behavior
- `## REMOVED Requirements` - Deprecated features

### Artifact Graph System

DAG-based dependency management:

- Topological sort for build order
- Filesystem-based state detection
- Dependencies as enablers, not gates
- Parallel artifact creation when possible

### OPSX Workflow

Action-based commands instead of phases:

- `/opsx:explore` - Think without artifact pressure
- `/opsx:new`, `/opsx:continue` - Create artifacts
- `/opsx:ff` - Fast-forward all planning
- `/opsx:apply` - Implement tasks
- `/opsx:verify`, `/opsx:archive` - Complete work

## Key Strengths

| Strength | Description |
|----------|-------------|
| Brownfield-first | Delta specs for existing systems |
| Fluid workflow | No phase gates, work on what makes sense |
| Minimal ceremony | Lightweight setup, easy onboarding |
| Custom schemas | Team-specific workflows |
| Context injection | Project conventions in instructions |

## Artifact Overview

| Artifact | Focus | Output |
|----------|-------|--------|
| Proposal | WHY + Scope | proposal.md |
| Specs | WHAT (requirements) | specs/[domain]/spec.md |
| Design | HOW (approach) | design.md |
| Tasks | Steps | tasks.md |

## Workflow Approach

- **Actions not phases**: Available when dependencies met
- **Fast-forward option**: All artifacts at once
- **Parallel changes**: Isolated folders, independent work
- **Archive preservation**: Full context retained

## Best Fit Scenarios

| Scenario | Fit |
|----------|-----|
| Existing codebases (brownfield) | Excellent |
| Teams preferring flexibility | Excellent |
| Parallel feature development | Excellent |
| Minimal ceremony needs | Excellent |
| Heavy governance requirements | Moderate |

## Quick Start Path

```text
1. Install OpenSpec
2. /opsx:new add-feature
3. /opsx:ff (or /opsx:continue step-by-step)
4. /opsx:apply
5. /opsx:verify
6. /opsx:archive
```

## Sources

- [README.md](../../references/OpenSpec/README.md)
- [Concepts](../../references/OpenSpec/docs/concepts.md)
- [OPSX Reference](../../references/OpenSpec/docs/opsx.md)
