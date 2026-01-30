# Artifact Taxonomy - OpenSpec

## Core Artifacts

| Artifact | File | Focus | Purpose |
|----------|------|-------|---------|
| Proposal | `proposal.md` | WHY + Scope | Intent, scope, approach |
| Specs | `specs/[domain]/spec.md` | WHAT | Requirements and scenarios |
| Design | `design.md` | HOW | Technical approach |
| Tasks | `tasks.md` | Steps | Implementation checklist |

## Classification by Lifecycle Stage

### Active Change Artifacts

Located in `openspec/changes/[change-name]/`:

| Artifact | Created By | Updated By |
|----------|------------|------------|
| Proposal | `/opsx:new` or `/opsx:continue` | Scope changes |
| Delta Specs | `/opsx:continue` | Requirement refinement |
| Design | `/opsx:continue` | Technical decisions |
| Tasks | `/opsx:continue` | Implementation progress |

### Main Specs

Located in `openspec/specs/[domain]/`:

| Artifact | Updated By | Trigger |
|----------|------------|---------|
| Domain Spec | `/opsx:sync` | Change archive |

### Archived Artifacts

Located in `openspec/changes/archive/[date]-[name]/`:

| Content | Preservation |
|---------|--------------|
| All change artifacts | Complete snapshot |
| Delta specs | Before merge |
| Implementation context | Full history |

## Delta Spec Sections

| Section | Prefix | Purpose |
|---------|--------|---------|
| Added Requirements | `## ADDED` | New behavior |
| Modified Requirements | `## MODIFIED` | Changed behavior (full content) |
| Removed Requirements | `## REMOVED` | Deprecated features (with reason) |

## Specification Structure

### Proposal Sections

| Section | Required | Content |
|---------|----------|---------|
| Why | Yes | Problem and motivation |
| Scope | Yes | In-scope and out-of-scope |
| Approach | Yes | High-level strategy |
| Capabilities | Optional | New and modified capabilities |
| Impact | Optional | Affected systems |

### Spec Sections

| Section | Required | Content |
|---------|----------|---------|
| Purpose | Yes | Domain description |
| Requirements | Yes | Numbered requirements (RFC 2119) |
| Scenarios | Yes | Given/When/Then format |

### Design Sections

| Section | Required | Content |
|---------|----------|---------|
| Context | Yes | Background and constraints |
| Goals/Non-Goals | Yes | Explicit boundaries |
| Decisions | Yes | Technical choices with rationale |
| Risks/Trade-offs | Optional | Known limitations |
| Migration Plan | Optional | Deployment strategy |
| Open Questions | Optional | Unresolved decisions |

### Tasks Structure

| Element | Format | Purpose |
|---------|--------|---------|
| Phase | `## N. Phase Name` | Grouping |
| Task | `- [ ] N.M Description` | Checkbox item |
| Subtask | Indented checkbox | Nested work |

## Artifact Dependencies (Default Schema)

```text
proposal
    │
    ├───────────┐
    ▼           ▼
  specs       design
    │           │
    └─────┬─────┘
          ▼
        tasks
          │
          ▼
       (apply)
```

## Configuration Artifacts

| File | Location | Purpose |
|------|----------|---------|
| Project Config | `openspec/config.yaml` | Schema, context, rules |
| Change Metadata | `.openspec.yaml` | Per-change schema override |
| Schema Definition | `schemas/[name]/schema.yaml` | Workflow definition |

## Schema Artifact Definition

From `schemas/spec-driven/schema.yaml`:

```yaml
artifacts:
  - id: proposal
    generates: proposal.md
    requires: []

  - id: specs
    generates: specs/**/*.md
    requires: [proposal]

  - id: design
    generates: design.md
    requires: [proposal]

  - id: tasks
    generates: tasks.md
    requires: [specs, design]
```

## Artifact State Detection

| Method | Implementation |
|--------|----------------|
| File existence | Filesystem scan of change directory |
| Glob patterns | Support for `specs/**/*.md` |
| Completion check | All dependencies satisfied |
| Blocked detection | Missing required artifacts |

## Sources

- [Concepts](../../references/OpenSpec/docs/concepts.md)
- [Schema Definition](../../references/OpenSpec/schemas/spec-driven/schema.yaml)
- [Artifact Graph Source](../../references/OpenSpec/src/core/artifact-graph/)
