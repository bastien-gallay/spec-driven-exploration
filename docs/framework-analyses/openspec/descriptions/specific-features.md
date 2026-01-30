# Specific Features - OpenSpec

## Overview

OpenSpec distinguishes itself through its artifact graph system, delta specs
for brownfield development, and fluid workflow architecture. This document
covers features unique to OpenSpec.

## Artifact Graph System

### DAG-Based Dependency Management

The artifact graph is OpenSpec's central innovation:

```typescript
// From src/core/artifact-graph/graph.ts
class ArtifactGraph {
  getBuildOrder(): string[]      // Topological sort
  getNextArtifacts(completed): string[]  // Ready artifacts
  getBlocked(completed): BlockedArtifacts  // Blocked + why
  isComplete(completed): boolean  // All done?
}
```

### Topological Sort

Uses Kahn's algorithm for deterministic ordering:

1. Find artifacts with no dependencies (in-degree 0)
2. Add to build order
3. Remove from graph, update in-degrees
4. Repeat until complete

### Dependencies as Enablers

Philosophy: Dependencies show what's possible, not what's required next.

| Approach | Meaning |
|----------|---------|
| Traditional gates | Must complete A before B |
| OpenSpec enablers | Can work on B once A exists |

### Parallel Creation

When dependencies allow, multiple artifacts can be created:

```text
proposal
    │
    ├─────┬─────┐
    ▼     ▼     ▼
  specs  design  (both available after proposal)
```

## Delta Specs

### Change-Focused Specifications

Instead of rewriting entire specs, delta specs describe changes:

```markdown
## ADDED Requirements

### Requirement: Two-Factor Authentication
The system SHALL support TOTP-based two-factor authentication.

#### Scenario: Enable 2FA
- GIVEN a user with verified email
- WHEN they enable 2FA
- THEN a QR code is displayed for authenticator setup

## MODIFIED Requirements

### Requirement: Login Flow
The system SHALL require 2FA verification after password authentication
when 2FA is enabled.

## REMOVED Requirements

### Requirement: Security Questions
**Reason**: Replaced by 2FA
**Migration**: Users with security questions prompted to enable 2FA
```

### Merge Process

During `/opsx:sync`:

1. ADDED sections appended to main spec
2. MODIFIED sections replace existing requirements
3. REMOVED sections deleted (with reason preserved in archive)

### Conflict Detection

During bulk archive, conflicts detected when:

- Multiple changes modify same requirement
- Changes have incompatible removals
- Order-dependent modifications

## OPSX Workflow Architecture

### Actions Not Phases

| Traditional Phases | OPSX Actions |
|-------------------|--------------|
| PLANNING | `/opsx:explore`, `/opsx:new`, `/opsx:continue` |
| IMPLEMENTING | `/opsx:apply` |
| DONE | `/opsx:verify`, `/opsx:archive` |

Key difference: Actions available anytime based on state.

### Fast-Forward Mode

`/opsx:ff` creates all artifacts at once:

```text
/opsx:new → /opsx:ff
                │
                ├── proposal.md
                ├── specs/**/*.md
                ├── design.md
                └── tasks.md
```

Use case: Clear requirements, experienced teams.

### Exploration as First-Class

`/opsx:explore` legitimizes thinking without artifact pressure:

- No output required
- Free investigation
- Problem understanding
- Approach consideration

## Multi-Level Schema Resolution

### Resolution Order

```text
1. Project-local: <project>/openspec/schemas/<name>/schema.yaml
2. User global:   ~/.local/share/openspec/schemas/<name>/schema.yaml
3. Package:       <package>/schemas/<name>/schema.yaml
```

### Custom Workflows

Teams can define custom schemas:

```yaml
# custom-workflow/schema.yaml
name: research-first
version: 1
description: Research before proposal

artifacts:
  - id: research
    generates: research.md
    requires: []

  - id: proposal
    generates: proposal.md
    requires: [research]  # Research first!

  - id: specs
    generates: specs/**/*.md
    requires: [proposal]

  # ... rest of workflow
```

### Schema Commands

```bash
openspec schema init my-workflow       # Create new
openspec schema fork spec-driven my-flow  # Copy and modify
openspec schema validate my-workflow   # Check validity
```

## Context Injection

### Project Context

Config embedded in instructions:

```yaml
# openspec/config.yaml
context: |
  Tech stack: TypeScript, React, Node.js
  API conventions: RESTful, JSON responses
```

Becomes:

```markdown
<context>
Tech stack: TypeScript, React, Node.js
API conventions: RESTful, JSON responses
</context>

[Artifact instructions...]
```

### Per-Artifact Rules

```yaml
rules:
  proposal:
    - Include rollback plan
  specs:
    - Use Given/When/Then format
  design:
    - Document alternatives
```

Becomes:

```markdown
<rules>
- Include rollback plan
</rules>
```

## Three-Dimensional Verification

### `/opsx:verify` Dimensions

| Dimension | Focus | Questions |
|-----------|-------|-----------|
| Completeness | Coverage | All tasks done? All requirements covered? |
| Correctness | Accuracy | Does implementation match intent? |
| Coherence | Consistency | Are design decisions reflected? |

### Verification Output

Structured report identifying:

- Missing implementations
- Incorrect behaviors
- Design deviations

## Parallel Change Isolation

### Independent Work Streams

Each change in separate folder:

```text
changes/
├── feature-a/    # Team 1
├── feature-b/    # Team 2
└── feature-c/    # Team 3
```

### Context Switching

```bash
/opsx:apply feature-a    # Work on feature-a
/opsx:apply feature-b    # Switch to feature-b
```

### Clean Completion

Each change archived independently:

```text
archive/
├── 2025-01-15-feature-a/
├── 2025-01-20-feature-b/
└── 2025-01-22-feature-c/
```

## RFC 2119 Requirements

### Standard Keywords

| Keyword | Meaning |
|---------|---------|
| MUST / SHALL | Absolute requirement |
| SHOULD | Recommended, may be ignored with reason |
| MAY | Optional feature |

### In Specifications

```markdown
## Requirements

### Requirement: Session Management
The system SHALL invalidate sessions after 30 minutes of inactivity.
The system SHOULD warn users before session expiration.
The system MAY offer "remember me" functionality.
```

## Filesystem-Based State

### No Metadata Tracking

State determined by file existence:

```typescript
// From src/core/artifact-graph/state.ts
function detectCompleted(changePath: string): Set<string> {
  // Scan directory for generated files
  // Match against artifact patterns
  // Return completed artifact IDs
}
```

### Glob Pattern Support

Artifacts can use patterns:

```yaml
- id: specs
  generates: specs/**/*.md   # Matches any specs
```

## Instruction Generation

### Enriched Instructions

`ArtifactInstructions` includes:

| Component | Content |
|-----------|---------|
| Template | Base markdown structure |
| Dependencies | Completion status |
| Unlocks | What completes after this |
| Project context | Tech stack, conventions |
| Rules | Artifact-specific constraints |

### Dynamic Enrichment

Instructions assembled at runtime from:

- Schema templates
- Project config
- Artifact-specific rules
- Current state

## Sources

- [Concepts](../../references/OpenSpec/docs/concepts.md)
- [OPSX Reference](../../references/OpenSpec/docs/opsx.md)
- [Artifact Graph Source](../../references/OpenSpec/src/core/artifact-graph/)
- [Schema Definition](../../references/OpenSpec/schemas/spec-driven/schema.yaml)
