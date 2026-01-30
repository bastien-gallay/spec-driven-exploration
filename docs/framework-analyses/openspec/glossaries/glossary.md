# Glossary - OpenSpec

## Core Concepts

### Artifact

A document produced during the specification process. OpenSpec defines four
core artifacts: Proposal, Specs, Design, and Tasks.

### Artifact Graph

DAG-based system managing artifact creation order and dependencies. Uses
topological sorting (Kahn's algorithm) for deterministic ordering.

### Delta Spec

Specification format focusing only on changes rather than full document
rewrites. Uses ADDED, MODIFIED, and REMOVED sections.

### OPSX

OpenSpec's workflow architecture with action-based commands rather than
phase-based progression.

### Schema

YAML definition of a workflow, specifying artifacts, their dependencies,
templates, and instructions.

## Workflow Terms

### Change

A proposed modification to the system, isolated in its own folder under
`openspec/changes/`. Contains all artifacts for that change.

### Archive

Completed changes moved to `openspec/changes/archive/` with timestamp prefix.
Preserves full context for history.

### Fast-Forward (ff)

OPSX command (`/opsx:ff`) creating all planning artifacts at once instead
of step-by-step progression.

### Verify

OPSX command (`/opsx:verify`) validating implementation against artifacts
across completeness, correctness, and coherence dimensions.

### Sync

OPSX command (`/opsx:sync`) merging delta specs into main specs before
archiving.

## Artifact Terms

### Proposal

Document capturing intent, scope, and approach (`proposal.md`). Contains WHY,
scope boundaries, and high-level strategy.

### Specs (Specifications)

Requirements and scenarios defining WHAT the system should do. Stored in
`specs/[domain]/spec.md` using RFC 2119 keywords.

### Design

Technical approach document (`design.md`) explaining HOW to implement the
change. Contains decisions, rationale, and trade-offs.

### Tasks

Implementation checklist (`tasks.md`) with checkbox format for tracking
progress. Small, completable steps ordered by dependency.

## Technical Terms

### RFC 2119 Keywords

Standard requirement level indicators:

- **MUST/SHALL**: Absolute requirement
- **SHOULD**: Recommended but may be ignored with reason
- **MAY**: Optional feature

### Topological Sort

Algorithm (Kahn's) used by artifact graph to determine correct build order
based on dependencies.

### Multi-Level Resolution

Schema resolution order: Package built-in → User global → Project local.
Enables customization without modifying package code.

### Context Injection

Project configuration embedded as `<context>` tags in artifact instructions.
Includes tech stack, conventions, and style guidelines.

## Directory Terms

### `openspec/specs/`

Source of truth describing current system behavior. Organized by domain
(logical groupings).

### `openspec/changes/`

Work in progress area. Each change in separate folder with its artifacts.

### `openspec/config.yaml`

Project configuration defining schema, context, and per-artifact rules.

### Domain

Logical grouping of related specifications (e.g., `auth/`, `payments/`,
`notifications/`).

## OPSX Commands

| Command | Purpose |
|---------|---------|
| `/opsx:explore` | Think through ideas |
| `/opsx:new` | Start new change |
| `/opsx:continue` | Create next artifact |
| `/opsx:ff` | Fast-forward planning |
| `/opsx:apply` | Implement tasks |
| `/opsx:verify` | Validate implementation |
| `/opsx:sync` | Merge delta specs |
| `/opsx:archive` | Complete change |
| `/opsx:bulk-archive` | Archive multiple changes |

## Verification Dimensions

| Dimension | Question |
|-----------|----------|
| Completeness | All tasks done? All requirements implemented? |
| Correctness | Implementation matches spec intent? |
| Coherence | Design decisions reflected in code? |

## Sources

- [README.md](../../references/OpenSpec/README.md)
- [Concepts](../../references/OpenSpec/docs/concepts.md)
- [OPSX Reference](../../references/OpenSpec/docs/opsx.md)
