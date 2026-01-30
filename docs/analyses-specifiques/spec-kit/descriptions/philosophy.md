# Philosophy and Core Concepts - spec-kit

## Overview

spec-kit implements Specification-Driven Development (SDD), a methodology that
inverts traditional software development by treating specifications as the
primary executable artifact rather than code.

## Foundational Philosophy

### The Power Inversion

Traditional development treats code as primary and documentation as secondary.
SDD inverts this relationship:

| Traditional | SDD |
|-------------|-----|
| Code drives documentation | Specifications drive code |
| Code is source of truth | Specification is source of truth |
| Documentation lags behind | Code follows specification |
| Manual implementation | Code is generated output |

### Intent-Driven Development

Natural language specifications define behavior before implementation. The
focus is on WHAT and WHY, never HOW:

- **WHAT**: Functional requirements, user scenarios
- **WHY**: Problem being solved, success criteria
- **HOW**: Left to implementation phase

### Code as Continuously Regenerated Output

In SDD, code becomes a derived artifact that can be regenerated from
specifications. This enables:

- Rapid pivots through systematic regeneration
- What-if/simulation experiments
- Consistent implementation across changes
- Reduced gap between intent and implementation

## Core Principles

### Constitutional Governance

Every project operates under a constitution with 9 articles defining
immutable architectural DNA:

| Article | Principle | Impact |
|---------|-----------|--------|
| I | Library-First | Features as standalone libraries |
| II | CLI Interface Mandate | Text I/O, JSON support |
| III | Test-First Imperative | TDD required (NON-NEGOTIABLE) |
| VII | Simplicity | Maximum 3 projects initially |
| VIII | Anti-Abstraction | Use frameworks directly |
| IX | Integration-First Testing | Real databases over mocks |

### Template-Driven Quality Control

Templates constrain LLM behavior to prevent common issues:

| Constraint | Prevention |
|------------|------------|
| Focus on WHAT, avoid HOW | Premature implementation details |
| `[NEEDS CLARIFICATION]` markers | Incorrect assumptions |
| Quality checklists | Incomplete specifications |
| Pre-implementation gates | Over-engineering |
| Test-first file creation | Untestable implementations |

### Explicit Uncertainty Marking

The `[NEEDS CLARIFICATION]` marker system (maximum 3 per specification)
prevents AI from making plausible but potentially incorrect assumptions.
Ambiguities must be resolved before planning.

## Why SDD Matters

### AI Capability Threshold

AI capabilities have reached a point where reliable code generation from
specifications is possible. SDD leverages this capability systematically.

### Complexity Alignment

Modern software complexity demands systematic alignment between intent and
implementation. Specification-driven generation provides this alignment.

### Product Velocity

Rapid iteration through specification changes enables:

- Pivots as systematic regenerations
- Quick experimentation
- Consistent implementation
- Reduced rework

## Philosophical Stance

### On Abstraction

The Anti-Abstraction principle (Article VIII) directly counters over-
engineering:

- Use framework features directly
- Avoid wrapping libraries
- Combat unnecessary complexity
- Justify deviations explicitly

### On Testing

Test-First Imperative (Article III) is non-negotiable:

- Tests written BEFORE implementation
- Red-Green-Refactor cycle enforced
- Tests validated and approved by user
- No implementation without tests

### On Simplicity

Simplicity principle (Article VII) constrains initial scope:

- Maximum 3 projects for initial implementation
- Additional projects require documented justification
- Combat scope creep through principled constraints

### On Integration

Integration-First Testing (Article IX) ensures practical validation:

- Prefer real databases over mocks
- Use actual service instances
- Contract tests mandatory before implementation
- Generated code verified in practice

## Mental Models

### Specification as Unit Test for Intent

The specification quality checklist acts as "unit tests" for the specification
itself. Requirements must be:

- Complete
- Unambiguous
- Testable
- Traceable

### Constitution as Architectural DNA

The constitution provides genetic-level constraints that shape all
development. Like DNA, it:

- Is immutable (except through formal amendment)
- Shapes every artifact
- Provides consistency across features
- Prevents architectural drift

### Features as Libraries

The Library-First principle treats every feature as a potentially reusable
component:

- Enforces modular design
- Enables composition
- Supports testing in isolation
- Facilitates future extraction

## Sources

- [README.md](../../references/spec-kit/README.md)
- [Spec-Driven Philosophy](../../references/spec-kit/spec-driven.md)
- [Constitution](../../references/spec-kit/memory/constitution.md)
