# Cross-Analysis: Artifacts

## Overview

This analysis compares the documents and files produced by spec-kit, BMAD,
and OpenSpec. Each framework has distinct artifact strategies reflecting
their philosophical approaches to spec-driven development.

## Artifact Mapping

| Purpose | spec-kit | BMAD | OpenSpec |
|---------|----------|------|----------|
| Governance | `constitution.md` | `project-context.md` | `config.yaml`, `schema.yaml` |
| Vision/Strategy | - | `product-brief.md` | - |
| Requirements | `spec.md` | `PRD.md` | `proposal.md` + `specs/*.md` |
| UX Design | - | `ux-spec.md` | - |
| Technical Design | `plan.md` | `architecture.md` | `design.md` |
| Decision Records | (in plan) | ADRs (in architecture) | (in design) |
| Research | `research.md` | (in brainstorm) | - |
| Data Model | `data-model.md` | (in architecture) | - |
| API Contracts | `contracts/*.yaml` | (in architecture) | - |
| Test Scenarios | `quickstart.md` | - | (in specs) |
| Feature Groups | - | `epics/*.md` | - |
| Work Items | `tasks.md` | `stories/*.md` | `tasks.md` |
| Progress Tracking | (checkboxes) | `sprint-status.yaml` | (checkboxes) |
| Validation Report | (console output) | `readiness-check.md` | (console output) |
| Code Review | - | `reviews/*.md` | - |

## Artifact Lifecycle

### spec-kit Lifecycle

```text
                                 Feature Folder
                          specs/[###-feature-name]/
                          ┌─────────────────────────┐
    Constitution          │                         │
         │                │   spec.md (Specify)     │
         ▼                │         │               │
  .specify/memory/        │   [clarify loop]        │
  constitution.md         │         │               │
         │                │   plan.md (Plan)        │
         │                │   research.md           │
         │                │   data-model.md         │
         │                │   contracts/            │
         │                │   quickstart.md         │
         │                │         │               │
         └────────────────┤   tasks.md (Tasks)      │
                          │                         │
                          └─────────────────────────┘

Lifecycle: once_per_project (constitution)
          once_per_feature (spec, plan, tasks)
          per_session (research, analysis)
```

### BMAD Lifecycle

```text
    Phase 1           Phase 2           Phase 3           Phase 4
    (Optional)

    brainstorm.md     PRD.md            architecture.md   sprint-status.yaml
         │               │                   │                   │
         ▼               ▼                   ▼                   ▼
    product-brief.md  ux-spec.md         epics/*.md        stories/*.md
                                              │                   │
                                              ▼                   ▼
                                         readiness-         reviews/*.md
                                         check.md

    ┌─────────────────────────────────────────────────────────────────────┐
    │ Brownfield: project-context.md (continuous, all phases)             │
    └─────────────────────────────────────────────────────────────────────┘

    ┌─────────────────────────────────────────────────────────────────────┐
    │ Quick Flow: tech-spec.md → implementation (bypasses phases)         │
    └─────────────────────────────────────────────────────────────────────┘

Lifecycle: once_per_project (brief, PRD, architecture)
          once_per_feature (epic, story)
          continuous (sprint-status, project-context)
          per_session (reviews)
```

### OpenSpec Lifecycle

```text
    Main Specs                    Active Change                   Archive
    (Source of Truth)             changes/[name]/                 changes/archive/

    openspec/specs/               ┌─────────────────┐             ┌─────────────────┐
    ├── auth/                     │ .openspec.yaml  │             │ [date]-[name]/  │
    │   └── spec.md               │                 │             │                 │
    ├── payments/                 │ proposal.md     │────────────►│ (all artifacts) │
    │   └── spec.md               │                 │   archive   │                 │
    └── ...                       │ specs/          │             │                 │
         ▲                        │   └── spec.md   │             └─────────────────┘
         │                        │ design.md       │
         │         sync           │ tasks.md        │
         └────────────────────────┤                 │
                                  └─────────────────┘

    Configuration
    openspec/
    ├── config.yaml (project settings)
    └── schemas/ (workflow definitions)

Lifecycle: continuous (main specs, config)
          once_per_feature (change artifacts)
          archive (completed changes)
```

## Template Comparison

### Requirements Document

| Section | spec-kit (spec.md) | BMAD (PRD.md) | OpenSpec (proposal.md) |
|---------|-------------------|---------------|----------------------|
| Problem/Why | (in scenarios) | Problem Statement | Why |
| Users | User Scenarios | Target Users, Personas | (in context) |
| Scope | (implicit) | (implicit) | Scope (In/Out) |
| Approach | (none - HOW forbidden) | (none) | Approach |
| Requirements | Functional Requirements | Functional + Non-Functional | (in specs/) |
| Success | Success Criteria | Success Metrics | (in specs/) |
| Risks | Edge Cases | Risks and Mitigations | (none) |
| Entities | Key Entities | (in architecture) | (none) |

### Design Document

| Section | spec-kit (plan.md) | BMAD (architecture.md) | OpenSpec (design.md) |
|---------|-------------------|----------------------|---------------------|
| Context | Technical Context | System Overview | Context |
| Decisions | Constitution Check | ADRs | Decisions |
| Structure | Project Structure | Components | (in decisions) |
| Integration | (in contracts) | Integration Patterns | (in decisions) |
| Stack | Language, Dependencies | Technology Stack | (in context) |
| Trade-offs | Complexity Tracking | (in ADRs) | Risks/Trade-offs |
| Migration | (none) | (in ADRs) | Migration Plan |
| Open Items | (none) | (none) | Open Questions |

### Task Document

| Section | spec-kit (tasks.md) | BMAD (story.md) | OpenSpec (tasks.md) |
|---------|---------------------|-----------------|---------------------|
| Format | Markdown checkboxes | Markdown sections | Markdown checkboxes |
| Grouping | Phases (1, 2, 3...) | Single story | Phases (1, 2, 3...) |
| Markers | `[P]` parallel, `[Story]` | Acceptance Criteria | Numbered (1.1, 1.2) |
| Dependencies | (ordering implies) | Dependencies section | (ordering implies) |
| Technical | (in plan) | Technical Notes | (in design) |

## File Organization

### Directory Structure

#### spec-kit

```text
.specify/
├── memory/
│   └── constitution.md
├── templates/
│   ├── spec-template.md
│   ├── plan-template.md
│   └── tasks-template.md
└── specs/
    └── ###-feature-name/
        ├── spec.md
        ├── plan.md
        ├── tasks.md
        ├── research.md
        ├── data-model.md
        ├── quickstart.md
        └── contracts/
            └── *.yaml
```

#### BMAD

```text
{{planning_artifacts}}/              # Configurable path
├── product-brief.md
├── brainstorming-report.md
├── PRD.md
├── ux-spec.md
├── architecture.md
├── tech-spec.md                     # Quick Flow
├── readiness-check.md
└── epics/
    └── epic-*.md

{{implementation_artifacts}}/        # Configurable path
├── sprint-status.yaml
├── project-context.md
├── stories/
│   └── story-*.md
└── reviews/
    └── review-*.md
```

#### OpenSpec

```text
openspec/
├── config.yaml
├── schemas/
│   └── {schema-name}/
│       ├── schema.yaml
│       └── templates/
│           ├── proposal.md
│           ├── spec.md
│           ├── design.md
│           └── tasks.md
├── specs/
│   └── {domain}/
│       └── spec.md
└── changes/
    ├── {change-name}/
    │   ├── .openspec.yaml
    │   ├── proposal.md
    │   ├── specs/
    │   │   └── {domain}/
    │   │       └── spec.md
    │   ├── design.md
    │   └── tasks.md
    └── archive/
        └── {date}-{name}/
            └── (complete snapshot)
```

## Artifact Counts

| Framework | Governance | Specification | Design | Execution | Validation |
|-----------|------------|---------------|--------|-----------|------------|
| spec-kit | 1 | 2-3 | 4-5 | 1 | 1 (session) |
| BMAD | 1-2 | 2-3 | 1-2 | 2+ per feature | 2 |
| OpenSpec | 2-3 | 2+ | 1 | 1 | 1 (session) |

## Unique Artifact Patterns

### spec-kit: Constitution as DNA

The constitution is unique in treating governance as immutable law with
formal articles. No other framework has such rigid principles.

### BMAD: Sprint Tracking

Only BMAD has explicit sprint management artifacts (`sprint-status.yaml`)
for Agile-style tracking across multiple stories and epics.

### OpenSpec: Archive Preservation

Only OpenSpec has a formal archive mechanism that preserves complete change
context including all artifacts for historical record and audit.

## Conclusions

### Artifact Strategy Differences

1. **Scope per Artifact**:
   - spec-kit: Feature-level (one spec = one feature)
   - BMAD: Project-level (one PRD = whole product)
   - OpenSpec: Change-level (one change = one proposal)

2. **Persistence Model**:
   - spec-kit: Permanent (no archive concept)
   - BMAD: Continuous updates (stories accumulate)
   - OpenSpec: Archive completed, sync to source of truth

3. **Template Rigidity**:
   - spec-kit: Strict templates with required sections
   - BMAD: Flexible templates with frontmatter tracking
   - OpenSpec: Configurable via schema templates

### Recommendations

- **Choose spec-kit artifacts** when: Strong structure needed, feature isolation
  important, research documentation valued
- **Choose BMAD artifacts** when: Full product documentation needed, sprint
  tracking required, code review records important
- **Choose OpenSpec artifacts** when: Change history matters, brownfield with
  existing specs, minimal artifact footprint preferred

## Sources

- [spec-kit Artifact Taxonomy](../../framework-analyses/spec-kit/glossaries/artifact-taxonomy.yaml)
- [BMAD Artifact Taxonomy](../../framework-analyses/bmad/glossaries/artifact-taxonomy.yaml)
- [OpenSpec Artifact Taxonomy](../../framework-analyses/openspec/glossaries/artifact-taxonomy.yaml)
