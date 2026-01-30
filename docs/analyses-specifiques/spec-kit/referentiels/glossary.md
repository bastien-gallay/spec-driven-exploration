# Glossary - spec-kit

## Core Concepts

### Constitution

Project's governing principles and development guidelines stored in
`.specify/memory/constitution.md`. Contains 9 articles defining architectural
DNA: Library-First, CLI Mandate, Test-First Imperative, etc.

### Specification-Driven Development (SDD)

Development approach where specifications drive code generation, treating specs
as the primary executable artifact rather than code.

### Feature

A discrete unit of functionality with its own specification, plan, and tasks.
Organized in `specs/[###-feature-name]/` directories.

### Intent-Driven Development

Natural language specifications define behavior before implementation.
Focus on WHAT and WHY, never HOW.

## Workflow Terms

### Command

A slash command invoking a specific workflow step. Examples: `/speckit.specify`,
`/speckit.plan`, `/speckit.implement`.

### Clarify

Workflow step (`/speckit.clarify`) for identifying and resolving specification
ambiguities before planning.

### Analyze

Workflow step (`/speckit.analyze`) for cross-artifact consistency validation.
Detects duplications, ambiguities, and coverage gaps.

### Pre-Implementation Gates

Constitution-based checkpoints (Simplicity Gate, Anti-Abstraction Gate,
Integration-First Gate) validated before implementation begins.

## Artifact Terms

### Spec (Feature Specification)

Technology-agnostic description of what to build and why (`spec.md`).
Contains user scenarios, functional requirements, entities, and success
criteria.

### Plan (Implementation Plan)

Technical architecture translating specifications into technical decisions
(`plan.md`). Maps requirements to technology choices with rationale.

### Tasks

Executable task list derived from the plan (`tasks.md`). Organized in phases
with parallel markers (`[P]`) and story associations (`[Story]`).

### Research

Investigation of technology choices and unknowns (`research.md`). Created
during planning when decisions require research.

### Data Model

Entity schemas and relationships (`data-model.md`). Defines the data
structures for the feature.

### Contracts

API specifications in `contracts/` directory. Includes OpenAPI/GraphQL
definitions for service interfaces.

### Quickstart

Key validation scenarios (`quickstart.md`). Describes critical paths for
testing the implementation.

## Quality Terms

### Needs Clarification Marker

Tag `[NEEDS CLARIFICATION]` indicating ambiguous areas in specification.
Maximum 3 per specification to prevent assumption-making.

### Specification Quality Checklist

Validation checklist ensuring specification completeness and feature readiness.
Acts as "unit tests" for the specification.

### Complexity Tracking

Section in implementation plan documenting justified violations of constitution
principles.

## Constitutional Articles

| Article | Name | Principle |
|---------|------|-----------|
| I | Library-First | Features begin as standalone libraries |
| II | CLI Interface Mandate | Text I/O, JSON support |
| III | Test-First Imperative | TDD required (NON-NEGOTIABLE) |
| VII | Simplicity | Maximum 3 projects initially |
| VIII | Anti-Abstraction | Use frameworks directly |
| IX | Integration-First Testing | Real databases over mocks |

## Directory Terms

### `.specify/`

Root directory containing all spec-kit files: memory, scripts, specs,
and templates.

### Memory

Persistent context directory (`.specify/memory/`) containing constitution
and other project-level context.

### Templates

Document templates (`.specify/templates/`) for specifications, plans,
and tasks.

## Sources

- [README.md](../../references/spec-kit/README.md)
- [Spec-Driven Philosophy](../../references/spec-kit/spec-driven.md)
- [Constitution](../../references/spec-kit/memory/constitution.md)
