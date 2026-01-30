# Artifact Taxonomy - BMAD

## Classification by Phase

### Phase 1: Analysis (Optional)

| Artifact | File | Creator | Purpose |
|----------|------|---------|---------|
| Brainstorming Report | `brainstorming-report.md` | Analyst | Session results, ideation outcomes |
| Research Findings | Various | Analyst | Market, domain, technical research |
| Product Brief | `product-brief.md` | Analyst | Strategic vision, product strategy |

### Phase 2: Planning

| Artifact | File | Creator | Purpose |
|----------|------|---------|---------|
| PRD | `PRD.md` | PM | Requirements, personas, metrics |
| UX Spec | `ux-spec.md` | UX Designer | User experience design |

### Phase 3: Solutioning

| Artifact | File | Creator | Purpose |
|----------|------|---------|---------|
| Architecture | `architecture.md` | Architect | Technical decisions (ADRs) |
| Epic Files | `epic-[name].md` | SM/PM | Feature groupings |
| Story Backlog | Various | SM | Individual stories |
| Readiness Check | Report | Various | Implementation gate |

### Phase 4: Implementation

| Artifact | File | Creator | Purpose |
|----------|------|---------|---------|
| Sprint Status | `sprint-status.yaml` | SM | Sprint tracking |
| Story Files | `story-[slug].md` | SM | Implementation details |
| Project Context | `project-context.md` | Analyst | Brownfield rules |
| Test Suites | Various | Dev/QA | Automated tests |
| Code Review | Report | Various | Quality validation |

### Quick Flow

| Artifact | File | Creator | Purpose |
|----------|------|---------|---------|
| Tech Spec | `tech-spec.md` | Barry | Focused change spec |
| Implementation | Code | Barry | Working code + tests |

## Classification by Type

### Strategic Documents

Documents defining vision, goals, and high-level requirements.

- Product Brief
- PRD
- Epic definitions

### Technical Documents

Documents defining architecture, design, and implementation approach.

- Architecture (with ADRs)
- UX Spec
- Tech Spec (Quick Flow)

### Execution Documents

Documents guiding implementation work.

- Story files (tasks, acceptance criteria)
- Sprint Status (tracking)
- Project Context (brownfield rules)

### Validation Documents

Documents ensuring quality and alignment.

- Readiness Check reports
- Code Review findings
- Test results

## Classification by Lifecycle

### Created Once

- Product Brief
- PRD (with edits)
- Architecture

### Created Per Feature

- Epic files
- Story files
- UX Spec (when needed)

### Updated Continuously

- Sprint Status
- Project Context
- Test Suites

## Artifact Dependencies

```text
Product Brief
     │
     ▼
   PRD ─────────────────┐
     │                  │
     ▼                  ▼
Architecture        UX Spec
     │
     ▼
   Epics
     │
     ▼
  Stories
     │
     ▼
Implementation
```

## Storage Locations

| Artifact Type | Location |
|---------------|----------|
| Planning Artifacts | `{{planning_artifacts}}/` |
| Implementation Artifacts | `{{implementation_artifacts}}/` |
| Project Knowledge | `{{project_knowledge}}/` |

## Sources

- [Module Config](../../references/BMAD/BMAD-METHOD/src/bmm/module.yaml)
- [Workflow Map](../../references/BMAD/BMAD-METHOD/docs/reference/workflow-map.md)
