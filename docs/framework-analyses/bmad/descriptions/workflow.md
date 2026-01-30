# Workflow and Prompts - BMAD

## Overview

BMAD organizes development into four sequential phases, each with dedicated
workflows executed by specialized agents. The framework supports both full
methodology and minimum-ceremony Quick Flow tracks.

## Four-Phase Development Lifecycle

### Phase 1: Analysis (Optional)

Discovery and strategic planning phase for new projects.

| Workflow | Agent | Command | Output |
|----------|-------|---------|--------|
| Brainstorm Project | Mary | `/brainstorm` | `brainstorming-report.md` |
| Research | Mary | `/research` | Research findings |
| Create Product Brief | Mary | `/product-brief` | `product-brief.md` |

**Brainstorming Workflow**:

1. Setup: Define topic, goals, constraints
2. Choose Approach: Pick techniques (60+ available)
3. Facilitation: Work through with probing questions
4. Organization: Group ideas into themes
5. Action: Define next steps for top ideas

### Phase 2: Planning

Requirements definition and user experience design.

| Workflow | Agent | Command | Output |
|----------|-------|---------|--------|
| Create PRD | John (PM) | `/create-prd` | `PRD.md` |
| Validate PRD | John | `/validate-prd` | Validation report |
| Edit PRD | John | `/edit-prd` | Updated `PRD.md` |
| Create UX Design | Sally | `/create-ux` | `ux-spec.md` |

**PRD Workflow (Tri-Modal)**:

- **Create Mode (-c)**: New PRD from scratch
- **Validate Mode (-v)**: Check against BMAD standards
- **Edit Mode (-e)**: Improve existing PRD

### Phase 3: Solutioning

Technical architecture and story preparation (multi-epic projects).

| Workflow | Agent | Command | Output |
|----------|-------|---------|--------|
| Create Architecture | Winston | `/create-architecture` | `architecture.md` |
| Create Epics/Stories | John/Bob | `/create-epics` | Epic files |
| Implementation Readiness | Various | `/impl-readiness` | PASS/CONCERNS/FAIL |

**Architecture Workflow**:

- Technical decisions documented as ADRs
- System design with component interactions
- Integration patterns and conventions
- Technology stack decisions with rationale

### Phase 4: Implementation

Sprint execution and code delivery.

| Workflow | Agent | Command | Output |
|----------|-------|---------|--------|
| Sprint Planning | Bob | `/sprint-planning` | `sprint-status.yaml` |
| Create Story | Bob | `/create-story` | `story-[slug].md` |
| Dev Story | Amelia | `/dev-story` | Working code + tests |
| Automate (QA) | Quinn | `/qa` | Test suite |
| Code Review | Various | `/code-review` | Approved/Changes |
| Course Correction | Bob | `/course-correct` | Updated plan |
| Retrospective | Bob | `/retro` | Lessons learned |

## Quick Flow Track

Minimum ceremony for simple changes.

| Workflow | Agent | Command | Output |
|----------|-------|---------|--------|
| Quick Spec | Barry | `/quick-spec` | `tech-spec.md` |
| Quick Dev | Barry | `/quick-dev` | Working code + tests |

**When to use Quick Flow**:

- Bug fixes
- Refactoring
- Small features
- Prototyping

## Step-File Architecture

### Core Principles

1. **Micro-file Design**: Each step is self-contained
2. **Just-In-Time Loading**: Only current step in memory
3. **Sequential Enforcement**: Steps in order, no skipping
4. **State Tracking**: Progress in output file frontmatter
5. **Append-Only Building**: Documents built incrementally

### Critical Rules

- NEVER load multiple step files simultaneously
- ALWAYS read entire step file before execution
- NEVER skip steps or optimize sequence
- ALWAYS update frontmatter when writing output
- ALWAYS halt at menus and wait for input

### Frontmatter Example

```yaml
---
stepsCompleted: ['step-1', 'step-2']
inputDocuments: ['product-brief.md']
workflowType: 'prd'
---
```

## Context Loading

Different workflows load different context:

| Workflow | Context Loaded |
|----------|---------------|
| `create-story` | Epics, PRD, Architecture, UX |
| `dev-story` | Story file |
| `code-review` | Architecture, Story file |
| `quick-spec` | Planning docs (if exist) |
| `quick-dev` | Tech-spec |

## Workflow Templates

### PRD Template Structure

```markdown
# Product Requirements Document - {{project_name}}

**Author:** {{user_name}}
**Date:** {{date}}

## Problem Statement
## Target Users
## User Personas
## Functional Requirements
## Non-Functional Requirements
## Success Metrics
## Risks and Mitigations
```

### Story Template Structure

```markdown
# Story: [Title]

## Acceptance Criteria
## Tasks
## Technical Notes
## Dependencies
## Definition of Done
```

## Recommended Practices

### Fresh Chats

Start fresh conversation for each workflow to:

- Avoid context limitations
- Prevent cross-workflow interference
- Ensure clean state

### Document Project (Brownfield)

For existing codebases, run `document-project` workflow to create
`project-context.md` containing:

- Existing codebase patterns
- Rules all workflows must observe
- Technology constraints

## Sources

- [Workflow Map](../../references/BMAD/BMAD-METHOD/docs/reference/workflow-map.md)
- [Getting Started](../../references/BMAD/BMAD-METHOD/docs/tutorials/getting-started.md)
- [Quick Flow](../../references/BMAD/BMAD-METHOD/docs/explanation/quick-flow.md)
- [Create PRD Workflow](../../references/BMAD/BMAD-METHOD/src/bmm/workflows/2-plan-workflows/create-prd/)
