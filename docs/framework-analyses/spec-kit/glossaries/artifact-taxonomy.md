# Artifact Taxonomy - spec-kit

## Classification by Purpose

### Governance Artifacts

| Artifact | File | Purpose |
|----------|------|---------|
| Constitution | `.specify/memory/constitution.md` | Project principles and constraints |

### Specification Artifacts

| Artifact | File | Purpose |
|----------|------|---------|
| Feature Spec | `specs/[###-feature-name]/spec.md` | WHAT and WHY |
| Research | `specs/[###-feature-name]/research.md` | Technology investigation |

### Design Artifacts

| Artifact | File | Purpose |
|----------|------|---------|
| Implementation Plan | `specs/[###-feature-name]/plan.md` | HOW (technical approach) |
| Data Model | `specs/[###-feature-name]/data-model.md` | Entity schemas |
| Contracts | `specs/[###-feature-name]/contracts/` | API specifications |
| Quickstart | `specs/[###-feature-name]/quickstart.md` | Validation scenarios |

### Execution Artifacts

| Artifact | File | Purpose |
|----------|------|---------|
| Tasks | `specs/[###-feature-name]/tasks.md` | Implementation checklist |

## Classification by Workflow Step

| Step | Command | Output Artifact(s) |
|------|---------|-------------------|
| 1 | `/speckit.constitution` | `constitution.md` |
| 2 | `/speckit.specify` | `spec.md` |
| 3 | `/speckit.clarify` | Updated `spec.md` |
| 4 | `/speckit.plan` | `plan.md`, `research.md`, `data-model.md`, `contracts/`, `quickstart.md` |
| 5 | `/speckit.analyze` | Analysis report (not persisted) |
| 6 | `/speckit.tasks` | `tasks.md` |
| 7 | `/speckit.implement` | Code implementation |

## Classification by Lifecycle

### Created Once Per Project

| Artifact | Triggers Update |
|----------|-----------------|
| Constitution | Explicit amendment process |

### Created Once Per Feature

| Artifact | Triggers Update |
|----------|-----------------|
| Feature Spec | Clarification, scope change |
| Implementation Plan | Technical pivot |
| Data Model | Schema changes |
| Contracts | API changes |
| Quickstart | New validation scenarios |
| Tasks | Re-planning |

### Created Per Session

| Artifact | Persistence |
|----------|-------------|
| Research | Optional, kept for reference |
| Analysis Report | Not persisted |

## Artifact Dependencies

```text
Constitution (global)
       │
       ▼
Feature Specification
       │
       ├──────────┐
       ▼          ▼
   Research   Clarification
       │          │
       └────┬─────┘
            ▼
   Implementation Plan
       │
       ├──────────┬──────────┬──────────┐
       ▼          ▼          ▼          ▼
 Data Model   Contracts  Quickstart  Research
       │          │          │          │
       └──────────┴──────────┴──────────┘
                  │
                  ▼
               Tasks
                  │
                  ▼
          Implementation
```

## Artifact Sections

### Feature Specification Sections

| Section | Required | Purpose |
|---------|----------|---------|
| User Scenarios | Yes | Prioritized user stories with acceptance |
| Functional Requirements | Yes | Testable, numbered requirements |
| Key Entities | Yes | Data model overview |
| Success Criteria | Yes | Measurable outcomes |
| Edge Cases | Yes | Boundary conditions |

### Implementation Plan Sections

| Section | Required | Purpose |
|---------|----------|---------|
| Technical Context | Yes | Language, dependencies, storage |
| Constitution Check | Yes | Gate validation |
| Project Structure | Yes | Architecture pattern |
| Complexity Tracking | Optional | Justified principle violations |

### Tasks Sections

| Section | Required | Purpose |
|---------|----------|---------|
| Phase 1: Setup | Yes | Project initialization |
| Phase 2: Foundational | Yes | Blocking prerequisites |
| Phase 3+: User Stories | Yes | Feature implementation |
| Final Phase: Polish | Yes | Cross-cutting concerns |

## Task Markers

| Marker | Meaning |
|--------|---------|
| `[P]` | Parallel execution possible |
| `[Story]` | User story association (US1, US2) |
| `[ ]` | Pending task |
| `[x]` | Completed task |

## Sources

- [Spec Template](../../references/spec-kit/templates/spec-template.md)
- [Plan Template](../../references/spec-kit/templates/plan-template.md)
- [Tasks Template](../../references/spec-kit/templates/tasks-template.md)
