# Cross-Analysis: Workflows

## Overview

This analysis compares how spec-kit, BMAD, and OpenSpec structure the
development process. Each framework takes a distinct approach to organizing
work from initial concept to completed implementation.

## Workflow Comparison

### High-Level Stages

| Stage | spec-kit | BMAD | OpenSpec |
|-------|----------|------|----------|
| 1 | Constitution | Analysis (optional) | Explore (optional) |
| 2 | Specify | Planning (PRD) | New (create change) |
| 3 | Clarify | Solutioning (Architecture) | Continue (artifacts) |
| 4 | Plan | Implementation (Stories) | Apply (implement) |
| 5 | Analyze | - | Verify |
| 6 | Tasks | - | Sync + Archive |
| 7 | Implement | - | - |

### Workflow Diagrams

#### spec-kit

```text
                    ┌──────────────────┐
                    │   Constitution   │
                    │ (project setup)  │
                    └────────┬─────────┘
                             │
                    ┌────────▼─────────┐
        ┌──────────►│     Specify      │
        │           │ (create spec)    │
        │           └────────┬─────────┘
        │                    │
        │           ┌────────▼─────────┐
        │           │     Clarify      │◄────┐
        │           │ (resolve gaps)   │     │ iterate
        │           └────────┬─────────┘     │
        │                    │───────────────┘
        │           ┌────────▼─────────┐
        │           │      Plan        │
        │           │ (tech design)    │
        │           └────────┬─────────┘
        │                    │
        │           ┌────────▼─────────┐
        └───────────┤     Analyze      │
          rework    │ (validate)       │
                    └────────┬─────────┘
                             │
                    ┌────────▼─────────┐
                    │      Tasks       │
                    │ (breakdown)      │
                    └────────┬─────────┘
                             │
                    ┌────────▼─────────┘
                    │    Implement     │
                    │ (execute)        │
                    └──────────────────┘
```

#### BMAD

```text
     Phase 1 (Optional)          Phase 2              Phase 3              Phase 4
     ┌──────────────┐        ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
     │  Brainstorm  │        │  Create PRD  │     │  Create      │     │   Sprint     │
     │    (Mary)    │───────►│   (John)     │────►│ Architecture │────►│  Planning    │
     └──────────────┘        └──────────────┘     │  (Winston)   │     │   (Bob)      │
            │                       │             └──────────────┘     └──────────────┘
            ▼                       │                    │                    │
     ┌──────────────┐              │                    ▼                    ▼
     │   Research   │              │             ┌──────────────┐     ┌──────────────┐
     │    (Mary)    │              │             │ Create Epics │     │ Create Story │
     └──────────────┘              │             │  (John/Bob)  │     │    (Bob)     │
            │                       │             └──────────────┘     └──────────────┘
            ▼                       │                    │                    │
     ┌──────────────┐              │                    ▼                    ▼
     │   Product    │              │             ┌──────────────┐     ┌──────────────┐
     │    Brief     │◄─────────────┘             │  Readiness   │     │  Dev Story   │
     │    (Mary)    │                            │    Check     │     │  (Amelia)    │
     └──────────────┘                            └──────────────┘     └──────────────┘
                                                        │                    │
                                   PASS ◄───────────────┘                    ▼
                                                                      ┌──────────────┐
                                                                      │ Code Review  │
                                                                      │  (Various)   │
                                                                      └──────────────┘

     ┌─────────────────────────────────────────────────────────────────────────────────┐
     │ Quick Flow Alternative: /quick-spec (Barry) ─► /quick-dev (Barry)               │
     └─────────────────────────────────────────────────────────────────────────────────┘
```

#### OpenSpec

```text
                    ┌──────────────────┐
                    │  /opsx:explore   │ (optional)
                    │ (think/debug)    │
                    └────────┬─────────┘
                             │
                    ┌────────▼─────────┐
                    │   /opsx:new      │
                    │ (create change)  │
                    └────────┬─────────┘
                             │
     ┌───────────────────────┼───────────────────────┐
     │                       │                       │
     │  Dependency-based artifact creation           │
     │                       │                       │
     │  ┌────────────────────▼────────────────────┐  │
     │  │            /opsx:continue               │  │
     │  │                                         │  │
     │  │  proposal ────┬────► specs              │  │
     │  │               │                         │  │
     │  │               └────► design             │  │
     │  │                          │              │  │
     │  │  specs ───────┴────► tasks              │  │
     │  │                                         │  │
     │  └─────────────────────────────────────────┘  │
     │                                               │
     │  Alternative: /opsx:ff (all at once)          │
     │                                               │
     └───────────────────────────────────────────────┘
                             │
                    ┌────────▼─────────┐
                    │   /opsx:apply    │◄────┐
                    │ (implement)      │     │ iterate
                    └────────┬─────────┘     │
                             │───────────────┘
                    ┌────────▼─────────┐
                    │   /opsx:verify   │
                    │ (validate)       │
                    └────────┬─────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼                             ▼
     ┌────────────────┐           ┌────────────────┐
     │  /opsx:sync    │──────────►│ /opsx:archive  │
     │ (merge specs)  │           │ (complete)     │
     └────────────────┘           └────────────────┘
```

## Process Differences

### Linearity vs Iteration

| Framework | Process Type | Iteration Pattern |
|-----------|--------------|-------------------|
| spec-kit | Sequential with loops | Clarify ↔ Specify until clear |
| BMAD | Phase-gated | Within phase; rework requires backtrack |
| OpenSpec | Dependency-driven | Any satisfied dependency available |

**spec-kit** enforces a mostly linear progression but explicitly encourages
iteration between the Specify and Clarify steps. The Analyze command can
also trigger rework.

**BMAD** uses strict phase gates (Readiness Check) that must pass before
implementation. However, Quick Flow bypasses full phases for simple changes.

**OpenSpec** has no inherent linearity - any command is available when its
dependencies are satisfied. This enables parallel work and flexible ordering.

### Validation Points

| Framework | Validation Step | Timing | Outcome |
|-----------|-----------------|--------|---------|
| spec-kit | Analyze | Pre-implementation | Issues report (CRITICAL/HIGH/MEDIUM/LOW) |
| BMAD | Readiness Check | Pre-implementation | PASS / CONCERNS / FAIL |
| OpenSpec | Verify | Post-implementation | Completeness, Correctness, Coherence |

**Key Difference**: spec-kit and BMAD validate before implementation;
OpenSpec validates after. This reflects OpenSpec's iterative apply model.

### Human Checkpoints

| Framework | Human Involvement | Trigger |
|-----------|-------------------|---------|
| spec-kit | Clarification answers | During `/speckit.clarify` workflow |
| BMAD | Step menus, decisions | During step execution (HALT at menus) |
| OpenSpec | Change decisions | Any time (no forced pauses) |

**spec-kit** uses structured questioning (max 5 questions per session, 10 total)
with multiple-choice or short-phrase answers.

**BMAD** step-file architecture includes explicit HALT points where agents
wait for human input on menus or decisions.

**OpenSpec** has minimal forced human checkpoints - users drive by invoking
commands rather than responding to prompts.

## Context Management

### What Gets Loaded

| Framework | Context Loading Strategy |
|-----------|--------------------------|
| spec-kit | Constitution + current feature artifacts |
| BMAD | Workflow-specific (PRD, Architecture, Stories) |
| OpenSpec | Change folder contents + config context injection |

### Context Size Concerns

| Framework | Strategy |
|-----------|----------|
| spec-kit | Feature isolation (one feature at a time) |
| BMAD | Fresh chats recommended per workflow |
| OpenSpec | Change isolation + archived history |

## Workflow Speed Comparison

| Use Case | spec-kit | BMAD | OpenSpec |
|----------|----------|------|----------|
| New project setup | Constitution + Specify | Product Brief + PRD | Config + New |
| Simple bug fix | Full flow (no shortcut) | Quick Flow | Fast-Forward |
| Complex feature | Full 7-step flow | Full 4-phase flow | Continue chain |
| Multiple parallel | Not supported | Multi-sprint | Native (change folders) |

## Error Handling

### When Things Go Wrong

| Framework | Recovery Approach |
|-----------|-------------------|
| spec-kit | Re-run Analyze, iterate Clarify |
| BMAD | Course Correction workflow, Retrospective |
| OpenSpec | Update specs, re-apply tasks |

### Explicit Recovery Workflows

- **spec-kit**: No dedicated recovery workflow; iteration handles corrections
- **BMAD**: `/course-correct` (Bob), `/retro` for lessons learned
- **OpenSpec**: Delta spec updates can modify earlier artifacts

## Recommendations

### When to Use Each Workflow Model

**Sequential (spec-kit)** works best when:

- Requirements are uncertain and need clarification
- Strong governance principles must be enforced
- Single-feature focus is acceptable

**Phase-gated (BMAD)** works best when:

- Team simulation with specialized roles is valuable
- Comprehensive documentation is required
- Clear phase transitions help manage complexity

**Dependency-driven (OpenSpec)** works best when:

- Parallel work on multiple changes is needed
- Workflow flexibility is valued
- Brownfield codebases need change isolation

## Sources

- [spec-kit Workflow](../../framework-analyses/spec-kit/descriptions/workflow.md)
- [BMAD Workflow](../../framework-analyses/bmad/descriptions/workflow.md)
- [OpenSpec Workflow](../../framework-analyses/openspec/descriptions/workflow.md)
