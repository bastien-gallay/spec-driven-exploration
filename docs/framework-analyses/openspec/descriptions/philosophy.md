# Philosophy and Core Concepts - OpenSpec

## Overview

OpenSpec is a specification-driven development framework built for modern
AI-assisted development. It emphasizes fluid workflows, brownfield development
support, and explicit agreement between humans and AI before implementation.

## Foundational Philosophy

### Core Principles

OpenSpec is built on four foundational principles:

| Principle | Meaning |
|-----------|---------|
| Fluid not rigid | No phase gates, work on what makes sense |
| Iterative not waterfall | Learn as you build, refine as you go |
| Easy not complex | Lightweight setup, minimal ceremony |
| Built for brownfield | Works with existing codebases |

### Agreement Before Implementation

The central insight: humans and AI must align on specifications before any code
is written. This brings predictability without ceremony.

> "Specifications bring predictability without ceremony"

### Scalable Approach

OpenSpec scales from personal projects to enterprises without changing the
fundamental approach.

## Key Concepts

### Delta Specs

Unlike full specifications requiring complete system restates, delta specs
focus only on what's changing:

| Section | Purpose |
|---------|---------|
| `## ADDED Requirements` | New behavior |
| `## MODIFIED Requirements` | Changed behavior (full updated content) |
| `## REMOVED Requirements` | Deprecated features (with reason) |

**Benefits**:

- Clarity on what's changing
- Avoids conflicts in parallel work
- Practical for brownfield development
- Clean history of changes

### Artifact Graph

A DAG-based system for managing artifact creation order:

- Topological sorting (Kahn's algorithm)
- State detected from filesystem
- Dependencies as enablers, not gates
- Multiple artifacts can be created in parallel

### Actions Not Phases

Traditional: `PLANNING → IMPLEMENTING → DONE` (can't go back)

OpenSpec: Actions available anytime based on dependency state

- Update specs during implementation
- Iterate on design based on discoveries
- No artificial phase restrictions

## Philosophical Stance

### On Brownfield Development

OpenSpec is explicitly "built for brownfield" because most real development
involves existing codebases. Delta specs enable:

- Change-focused specifications
- Minimal overhead for modifications
- Clean integration with existing systems
- Historical context preservation

### On Ceremony

Minimal ceremony is a design goal:

- Lightweight setup
- Simple directory structure
- No complex configuration
- Quick onboarding

### On Customization

Multi-level schema resolution enables customization without code changes:

1. Package built-in schemas (default)
2. User global overrides
3. Project local customizations

Teams can create domain-specific workflows without modifying the framework.

### On AI Alignment

Context injection ensures AI understands project specifics:

```yaml
context: |
  Tech stack: TypeScript, React, Node.js
  API conventions: RESTful, JSON responses
  Testing: Vitest, Playwright
```

This context is embedded in every artifact instruction.

## Mental Models

### Changes as Isolated Units

Each change lives in its own folder:

```text
changes/
├── add-dark-mode/          # Independent change
├── improve-search/         # Another independent change
└── archive/                # Completed changes
```

This isolation enables:

- Parallel work without conflicts
- Clean context switching
- Independent completion
- Historical preservation

### Specs as Living Documents

Main specs in `openspec/specs/` evolve through archived changes:

```text
Spec v1 + Change A → Spec v2
Spec v2 + Change B → Spec v3
...
```

Each archive adds to the specification history.

### Verification as Three Dimensions

Implementation validation across:

| Dimension | Question |
|-----------|----------|
| Completeness | All tasks done? All requirements implemented? |
| Correctness | Implementation matches spec intent? |
| Coherence | Design decisions reflected in code? |

## Workflow Philosophy

### Exploration as Valid Work

`/opsx:explore` legitimizes thinking and investigation:

- No artifact pressure
- Free investigation
- Problem understanding
- Approach consideration

### Fast-Forward for Experienced Users

`/opsx:ff` creates all planning artifacts at once for:

- Clear requirements
- Experienced teams
- Simple changes
- Time pressure

### Archive as Memory

Completed changes preserve full context:

- All artifacts retained
- Decision history visible
- Learning from past changes
- Audit trail for compliance

## Sources

- [README.md](../../references/OpenSpec/README.md)
- [Concepts](../../references/OpenSpec/docs/concepts.md)
- [Workflows](../../references/OpenSpec/docs/workflows.md)
