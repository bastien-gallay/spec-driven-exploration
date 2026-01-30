# Context Organization - spec-kit

## Overview

spec-kit organizes specification documentation through a hierarchical directory
structure centered on the `.specify/` directory, with feature-based isolation
and persistent memory for project-level context.

## Directory Structure

### Root Layout

```text
project/
├── .specify/
│   ├── memory/
│   │   └── constitution.md      # Project governing principles
│   ├── scripts/
│   │   ├── bash/                # Bash automation scripts
│   │   └── powershell/          # PowerShell automation scripts
│   ├── specs/
│   │   └── [###-feature-name]/  # Feature specifications
│   └── templates/               # Document templates
└── [project source code]
```

### Feature Directory Structure

Each feature in `specs/[###-feature-name]/`:

```text
specs/001-photo-organizer/
├── spec.md                      # Feature specification
├── plan.md                      # Implementation plan
├── research.md                  # Technology investigation
├── data-model.md                # Entity schemas
├── quickstart.md                # Validation scenarios
├── contracts/                   # API specifications
│   ├── api-spec.json
│   └── [service]-spec.md
└── tasks.md                     # Implementation checklist
```

## Feature Naming Convention

### Format

`[###]-[feature-name]`

**Examples**:

- `001-create-taskify`
- `002-user-authentication`
- `003-photo-gallery`

### Automatic Numbering

spec-kit auto-generates feature numbers by checking:

1. Remote branches
2. Local branches
3. Existing specs directories

## Memory System

### Constitution Location

`.specify/memory/constitution.md`

**Purpose**: Persistent project-level principles

**Persistence**: Across all feature development

**Access**: Always available to AI agents

### Constitution Structure

```markdown
# Project Constitution

## Article I: Library-First Principle
Every feature must begin as a standalone library...

## Article II: CLI Interface Mandate
All CLI interfaces must accept text input...

## Article III: Test-First Imperative
Strict Test-Driven Development required...

[Articles IV-IX]

## Section 4: Amendment Process
[Amendment procedures]
```

## Template Organization

### Template Files

```text
.specify/templates/
├── spec-template.md             # Feature specification
├── plan-template.md             # Implementation plan
├── tasks-template.md            # Task breakdown
└── commands/
    ├── constitution.md
    ├── specify.md
    ├── clarify.md
    ├── plan.md
    ├── analyze.md
    ├── tasks.md
    ├── implement.md
    ├── checklist.md
    └── taskstoissues.md
```

### Template Sections

#### Specification Template

| Section | Required | Purpose |
|---------|----------|---------|
| User Scenarios & Testing | Yes | Prioritized user stories |
| Functional Requirements | Yes | Testable requirements |
| Key Entities | Yes | Data model overview |
| Success Criteria | Yes | Measurable outcomes |
| Edge Cases | Yes | Boundary conditions |

#### Plan Template

| Section | Required | Purpose |
|---------|----------|---------|
| Technical Context | Yes | Tech stack decisions |
| Constitution Check | Yes | Gate validation |
| Project Structure | Yes | Architecture pattern |
| Complexity Tracking | Optional | Justified violations |

#### Tasks Template

| Section | Required | Purpose |
|---------|----------|---------|
| Phase 1: Setup | Yes | Initialization |
| Phase 2: Foundational | Yes | Prerequisites |
| Phase 3+: User Stories | Yes | Feature implementation |
| Final Phase: Polish | Yes | Cross-cutting |

## Script Organization

### Bash Scripts

```text
.specify/scripts/bash/
├── check-prerequisites.sh       # Environment validation
├── common.sh                    # Shared utilities
├── create-new-feature.sh        # Feature scaffolding
├── setup-plan.sh                # Plan initialization
└── update-agent-context.sh      # Context synchronization
```

### PowerShell Scripts

```text
.specify/scripts/powershell/
├── check-prerequisites.ps1
├── common.ps1
├── create-new-feature.ps1
├── setup-plan.ps1
└── update-agent-context.ps1
```

## Context Flow

### Specification Phase

```text
constitution.md ─────────────────────────────────┐
        │                                        │
        ▼                                        │
user description ──► spec.md                     │
                                                 │
                        │                        │
                        ▼                        │
                    clarify                      │
                        │                        │
                        ▼                        │
              updated spec.md                    │
                                                 ▼
```

### Planning Phase

```text
spec.md ─────────────────────────────────────────┐
   │                                             │
   ├──► research.md                              │
   │                                             │
   ├──► data-model.md                            │
   │                                             │
   ├──► contracts/                               │
   │                                             │
   ├──► quickstart.md                            │
   │                                             │
   └──► plan.md ◄────────── constitution gates   │
                                                 │
```

### Implementation Phase

```text
plan.md + data-model.md + contracts/ ────────────┐
                                                 │
                        │                        │
                        ▼                        │
                    tasks.md                     │
                        │                        │
                        ▼                        │
                   implement                     │
                                                 │
```

## Agent Context Management

### Context Update Script

`update-agent-context.sh` synchronizes:

- Technology stack
- Project conventions
- Current feature context

### Context Injection Points

| Artifact | Context Source |
|----------|---------------|
| Specification | Constitution, templates |
| Plan | Spec, constitution, tech decisions |
| Tasks | Plan, data-model, contracts |
| Implementation | Tasks, plan, constitution |

## Branch-Based Context

### Feature Detection

- Git checkout determines active feature
- `SPECIFY_FEATURE` environment variable for non-Git repos

### Branch Naming

Branches follow feature naming:

- `001-create-taskify`
- `002-user-authentication`

## Sources

- [README.md](../../references/spec-kit/README.md)
- [Templates](../../references/spec-kit/templates/)
- [Scripts](../../references/spec-kit/.specify/scripts/)
