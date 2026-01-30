# Workflow and Prompts - spec-kit

## Overview

spec-kit implements a 7-step sequential workflow with dedicated commands for
each phase. The workflow emphasizes clarification before planning and
validation before implementation.

## Workflow Steps

### Step 1: Establish Constitution

**Command**: `/speckit.constitution`

**Purpose**: Create project's governing principles.

**Input**: Project-specific principles (code quality, testing standards, UX
consistency, performance requirements)

**Output**: `.specify/memory/constitution.md`

**Example prompt**:

```text
/speckit.constitution Create principles focused on code quality, testing
standards, user experience consistency, and performance requirements
```

### Step 2: Create Specification

**Command**: `/speckit.specify`

**Purpose**: Transform natural language into structured specification.

**Execution flow**:

1. Generate 2-4 word branch short name
2. Determine next feature number
3. Run setup script
4. Parse user description for key concepts
5. Mark ambiguities with `[NEEDS CLARIFICATION]` (max 3)
6. Generate specification sections
7. Create quality checklist
8. Validate against checklist (max 3 iterations)
9. Present clarification questions

**Output**: `specs/[###-feature-name]/spec.md`

**Example prompt**:

```text
/speckit.specify Build an application that can help me organize my photos
by date, location, and custom tags with a clean gallery interface
```

### Step 3: Clarify Specification

**Command**: `/speckit.clarify`

**Purpose**: Identify and resolve ambiguities BEFORE planning.

**Execution flow**:

1. Structured ambiguity & coverage scan (8 categories)
2. Generate prioritized questions (max 5, max 10 across session)
3. Sequential questioning (one at a time)
4. Incremental spec updates after each answer
5. Coverage summary
6. Recommendations for proceeding

**Question constraints**:

- Multiple-choice (2-5 options) or short-phrase (≤5 words)
- Prioritized by impact
- Session limit of 10 questions

### Step 4: Generate Implementation Plan

**Command**: `/speckit.plan`

**Purpose**: Create technical architecture and supporting documents.

**Execution phases**:

- **Phase 0: Research** - Investigate unknowns, resolve NEEDS CLARIFICATION
- **Phase 1: Design** - Generate data models, contracts, quickstart
- **Agent context update** - Update AI-specific context files

**Outputs**:

- `plan.md` - Implementation plan
- `research.md` - Technology investigation
- `data-model.md` - Entity schemas
- `contracts/` - API specifications
- `quickstart.md` - Validation scenarios

### Step 5: Analyze Plan

**Command**: `/speckit.analyze`

**Purpose**: Cross-artifact consistency validation before implementation.

**Operating mode**: Read-only analysis (no file modifications)

**Detection passes**:

| Pass | Detection |
|------|-----------|
| A | Duplication |
| B | Ambiguity (vague adjectives, unresolved placeholders) |
| C | Underspecification (missing objects, outcomes) |
| D | Constitution Alignment (MUST principle conflicts) |
| E | Coverage Gaps (requirements without tasks) |
| F | Inconsistency (terminology drift, contradictions) |

**Severity levels**: CRITICAL, HIGH, MEDIUM, LOW

**Output**: Structured markdown report

### Step 6: Generate Task Breakdown

**Command**: `/speckit.tasks`

**Purpose**: Create executable task list from implementation plan.

**Inputs**:

- `plan.md` (required)
- `data-model.md` (if present)
- `contracts/` (if present)
- `research.md` (if present)

**Output**: `tasks.md` with phase organization and parallel markers

**Task organization**:

| Phase | Purpose |
|-------|---------|
| Phase 1: Setup | Project initialization |
| Phase 2: Foundational | Blocking prerequisites |
| Phase 3+: User Stories | Feature implementation |
| Final Phase: Polish | Cross-cutting concerns |

### Step 7: Execute Implementation

**Command**: `/speckit.implement`

**Purpose**: Execute all tasks following the implementation plan.

**Execution sequence**:

1. Check checklist status
2. Load implementation context
3. Verify project setup (create/verify ignore files)
4. Parse `tasks.md` structure
5. Phase-by-phase execution
6. Progress tracking with checkpoint validation
7. Completion validation

## Workflow Best Practices

### Recommended Sequence

```text
/speckit.constitution
        │
        ▼
/speckit.specify ◄──┐
        │           │
        ▼           │
/speckit.clarify ───┘ (iterate until clear)
        │
        ▼
/speckit.plan
        │
        ▼
/speckit.analyze
        │
        ▼
/speckit.tasks
        │
        ▼
/speckit.implement
```

### Key Insights

1. **Focus on WHAT and WHY** during specification
2. **Iterate and refine** specifications before implementation
3. **Use `/speckit.clarify` BEFORE `/speckit.plan`** to reduce rework
4. **Run `/speckit.analyze` after `/speckit.tasks`** for consistency validation
5. **Let AI agent handle implementation details**

## Task Markers

| Marker | Meaning |
|--------|---------|
| `[P]` | Parallel execution possible |
| `[Story]` | User story association (US1, US2, US3) |
| `[ ]` | Pending task |
| `[x]` | Completed task |

## Pre-Implementation Gates

Constitution-based checkpoints in implementation plan:

| Gate | Article | Validation |
|------|---------|------------|
| Simplicity | VII | Maximum 3 projects |
| Anti-Abstraction | VIII | Direct framework usage |
| Integration-First | IX | Real dependencies |

## Checklist Workflow

**Command**: `/speckit.checklist`

**Purpose**: Validate specification completeness.

**Sections**:

- Requirement completeness
- Feature readiness
- Quality markers

## Sources

- [README.md](../../references/spec-kit/README.md)
- [Quick Start](../../references/spec-kit/docs/quickstart.md)
- [Command Workflows](../../references/spec-kit/templates/commands/)
