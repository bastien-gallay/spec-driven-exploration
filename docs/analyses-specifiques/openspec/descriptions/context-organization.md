# Context Organization - OpenSpec

## Overview

OpenSpec organizes specification documentation through two main areas: `specs/`
for the source of truth and `changes/` for work in progress. This separation
enables parallel work and clean history.

## Directory Structure

### Project Layout

```text
project/
├── openspec/
│   ├── specs/                   # Source of truth (current system)
│   │   └── [domain]/
│   │       └── spec.md
│   ├── changes/                 # Work in progress
│   │   ├── [change-name]/
│   │   │   ├── .openspec.yaml   # Change metadata
│   │   │   ├── proposal.md
│   │   │   ├── specs/
│   │   │   │   └── [domain]/
│   │   │   │       └── spec.md  # Delta spec
│   │   │   ├── design.md
│   │   │   └── tasks.md
│   │   └── archive/
│   │       └── [date]-[name]/   # Completed changes
│   ├── schemas/                 # Custom workflow schemas
│   └── config.yaml              # Project configuration
└── [project source code]
```

### Specs Directory

Source of truth describing current system behavior:

```text
specs/
├── auth/
│   └── spec.md                  # Authentication requirements
├── payments/
│   └── spec.md                  # Payment processing
├── notifications/
│   └── spec.md                  # Notification system
└── ui/
    └── spec.md                  # UI components
```

**Organization**: By domain (logical groupings)

### Changes Directory

Work in progress area:

```text
changes/
├── add-2fa/                     # Active change
│   ├── .openspec.yaml
│   ├── proposal.md
│   ├── specs/
│   │   └── auth/
│   │       └── spec.md          # Delta spec
│   ├── design.md
│   └── tasks.md
├── improve-search/              # Another active change
│   └── ...
└── archive/                     # Completed changes
    ├── 2025-01-15-add-oauth/
    └── 2025-01-20-fix-session/
```

## Configuration

### Project Config (`config.yaml`)

```yaml
schema: spec-driven              # Workflow schema
context: |
  Tech stack: TypeScript, React, Node.js
  API conventions: RESTful, JSON responses
  Testing: Vitest, Playwright

rules:
  proposal:
    - Include rollback plan
    - Identify affected teams
  specs:
    - Use Given/When/Then format
  design:
    - Document alternatives considered
  tasks:
    - Maximum 2 hours per task
```

### Context Precedence

1. CLI flag (`--schema <name>`)
2. Change metadata (`.openspec.yaml`)
3. Project config (`openspec/config.yaml`)
4. Default (`spec-driven`)

### Change Metadata (`.openspec.yaml`)

```yaml
schema: spec-driven
created: 2025-01-30
```

## Schema Organization

### Multi-Level Resolution

```text
Resolution Order (highest to lowest):
1. Project-local: <project>/openspec/schemas/<name>/schema.yaml
2. User global:   ~/.local/share/openspec/schemas/<name>/schema.yaml
3. Package:       <package>/schemas/<name>/schema.yaml
```

### Schema Structure

```text
schemas/spec-driven/
├── schema.yaml                  # Workflow definition
├── templates/
│   ├── proposal.md
│   ├── spec.md
│   ├── design.md
│   └── tasks.md
└── instructions/
    ├── proposal.md
    ├── specs.md
    ├── design.md
    └── tasks.md
```

### Custom Schemas

Teams can create custom workflows:

```bash
openspec schema init my-workflow
openspec schema fork spec-driven research-first
openspec schema validate my-workflow
```

## Context Injection

### How It Works

Project config embedded in artifact instructions as `<context>` tags:

```markdown
<context>
Tech stack: TypeScript, React, Node.js
API conventions: RESTful, JSON responses
Testing: Vitest, Playwright
</context>

[Artifact-specific instructions...]
```

### Rules Injection

Per-artifact rules as `<rules>` tags:

```markdown
<rules>
- Include rollback plan
- Identify affected teams
</rules>
```

## Artifact State Detection

### Filesystem-Based

State determined by file existence, not metadata:

| Artifact | Detection |
|----------|-----------|
| Proposal | `proposal.md` exists |
| Specs | Files matching `specs/**/*.md` |
| Design | `design.md` exists |
| Tasks | `tasks.md` exists |

### Completion Check

All dependencies satisfied when required files exist.

### Blocked Detection

Missing required artifacts identified by graph traversal.

## Archive Process

### Before Archive

```text
openspec/
├── specs/
│   └── auth/spec.md            # Current state
└── changes/
    └── add-2fa/
        ├── proposal.md
        ├── specs/
        │   └── auth/spec.md    # Delta: ADDED requirements
        └── tasks.md
```

### After Archive

```text
openspec/
├── specs/
│   └── auth/spec.md            # Now includes 2FA requirements
└── changes/
    └── archive/
        └── 2025-01-24-add-2fa/ # Full change preserved
            ├── proposal.md
            ├── specs/
            │   └── auth/spec.md
            └── tasks.md
```

### Archive Benefits

| Benefit | Description |
|---------|-------------|
| Clean state | Only active changes in `changes/` |
| Audit trail | Why changes were made visible |
| Spec evolution | Each archive builds up specs |
| Context preservation | Full artifacts retained |

## Domain Organization

### Logical Groupings

Domains organize specs by functional area:

| Domain | Focus |
|--------|-------|
| `auth/` | Authentication, authorization |
| `payments/` | Payment processing |
| `notifications/` | Alerts, emails, messages |
| `ui/` | Interface components |

### Cross-Domain Changes

Changes can affect multiple domains:

```text
changes/add-payment-notifications/
├── specs/
│   ├── payments/
│   │   └── spec.md             # Payment hooks
│   └── notifications/
│       └── spec.md             # New notification types
└── ...
```

## Sources

- [Concepts](../../references/OpenSpec/docs/concepts.md)
- [Schema Definition](../../references/OpenSpec/schemas/spec-driven/schema.yaml)
- [Resolver Source](../../references/OpenSpec/src/core/artifact-graph/resolver.ts)
