# Cross-Analysis: Core Concepts

## Overview

This analysis compares how spec-kit, BMAD, and OpenSpec conceptualize
spec-driven development. Each framework brings a distinct philosophical
approach to defining and organizing the development process.

## Concept Comparison Matrix

| Concept Area | spec-kit | BMAD | OpenSpec |
|--------------|----------|------|----------|
| Governance | Constitution (9 articles) | Project Context | Config + Schema |
| Requirements | Feature Specification | PRD | Proposal + Delta Specs |
| Design | Implementation Plan | Architecture + ADRs | Design |
| Tasks | Tasks (phased) | Stories (sprint-based) | Tasks (checkbox) |
| Validation | Analyze command | Readiness Check | Verify (3 dimensions) |
| Work Units | Features | Epics/Stories | Changes |
| Process Model | Sequential commands | Four phases | Dependency graph |

## Deep Dives

### Governance Concepts

How each framework handles project-level constraints and principles.

#### spec-kit: Constitution

The Constitution (`.specify/memory/constitution.md`) defines immutable
architectural DNA through 9 formal articles:

- **Article I**: Library-First - Features begin as standalone libraries
- **Article II**: CLI Interface Mandate - Text I/O for all features
- **Article III**: Test-First Imperative - Non-negotiable TDD requirement
- **Article VII**: Simplicity - Maximum 3 projects constraint
- **Article VIII**: Anti-Abstraction - Direct framework usage
- **Article IX**: Integration-First Testing - Real dependencies

Key characteristic: **Prescriptive and immutable** - constitutional principles
cannot be overridden, only documented violations tracked.

#### BMAD: Project Context

BMAD uses `project-context.md` for brownfield development, capturing:

- Existing codebase patterns
- Technology constraints
- Rules all workflows must observe

Key characteristic: **Descriptive and adaptive** - captures existing reality
rather than prescribing behavior.

#### OpenSpec: Config + Schema

OpenSpec governance operates at two levels:

1. **config.yaml**: Project settings, tech stack, conventions
2. **schema.yaml**: Workflow definition, artifact dependencies

Key characteristic: **Configurable and extensible** - multi-level resolution
allows package, user, and project customization.

### Specification Concepts

How each framework captures requirements and intent.

#### spec-kit: Feature Specification

Single document (`spec.md`) per feature containing:

- User scenarios with acceptance criteria
- Numbered functional requirements
- Key entities (data model overview)
- Success criteria and edge cases
- `[NEEDS CLARIFICATION]` markers (max 3)

Focus: **Technology-agnostic WHAT and WHY**, never HOW.

#### BMAD: PRD (Product Requirements Document)

Comprehensive project-level document covering:

- Problem statement and target users
- User personas
- Functional and non-functional requirements
- Success metrics
- Risks and mitigations

Focus: **Full product scope** with business context.

#### OpenSpec: Proposal + Delta Specs

Two-level approach:

1. **Proposal**: Intent, scope, and approach (WHY and boundaries)
2. **Delta Specs**: ADDED/MODIFIED/REMOVED changes (WHAT)

Focus: **Change-oriented**, preserving existing spec integrity.

### Work Unit Concepts

How frameworks organize implementable units.

#### spec-kit: Features

Features are discrete units in `specs/[###-feature-name]/` containing:

- Specification (`spec.md`)
- Plan (`plan.md`)
- Tasks (`tasks.md`)

Lifecycle: **Once per feature**, numbered sequentially.

#### BMAD: Epics and Stories

Hierarchical structure:

- **Epics**: High-level feature groupings
- **Stories**: Implementable units with acceptance criteria

Lifecycle: **Sprint-based**, tracked in `sprint-status.yaml`.

#### OpenSpec: Changes

Isolated folders in `openspec/changes/[name]/` containing all artifacts.

Lifecycle: **Archive on completion**, preserving full context.

### Process Model Concepts

How frameworks structure the development flow.

#### spec-kit: Sequential Commands

Linear command sequence: `constitution` → `specify` → `clarify` → `plan` →
`analyze` → `tasks` → `implement`

Key insight: **Iteration encouraged** between specify and clarify.

#### BMAD: Four Phases

Sequential phases with specialized agents:

1. **Analysis** (optional): Discovery, brainstorming
2. **Planning**: PRD, UX design
3. **Solutioning**: Architecture, ADRs
4. **Implementation**: Sprints, stories

Key insight: **Phase gates** (readiness checks) control progression.

#### OpenSpec: Dependency Graph

Non-linear, action-based workflow:

- Commands available when dependencies satisfied
- Artifact graph determines creation order
- Topological sort (Kahn's algorithm) for ordering

Key insight: **Fluid progression** based on state, not phases.

## Terminology Alignment

| Common Term | spec-kit | BMAD | OpenSpec |
|-------------|----------|------|----------|
| Requirement | Feature Specification | PRD | Proposal + Specs |
| Design | Implementation Plan | Architecture | Design |
| Work Item | Task | Story | Task |
| Feature Group | Feature | Epic | Change |
| Validation | Analyze | Readiness Check | Verify |
| Governance | Constitution | Project Context | Config |
| Fast Track | N/A | Quick Flow | Fast-Forward |

## Unique Concepts

### Only in spec-kit

- **Constitution with 9 Articles**: Formal governance with specific principles
  (Library-First, CLI Mandate, Test-First Imperative)
- **Clarify Workflow**: Dedicated ambiguity detection and resolution step
- **NEEDS CLARIFICATION Marker**: Quantified ambiguity tracking (max 3 per spec)
- **Pre-Implementation Gates**: Constitutional checkpoints (Simplicity,
  Anti-Abstraction, Integration-First)

### Only in BMAD

- **Party Mode**: Multi-agent collaboration in single conversation
- **Agent Personas**: Named experts (John, Winston, Amelia) with personalities
- **Adversarial Review**: Forced problem-finding technique
- **Step-File Architecture**: Micro-file workflow design with JIT loading
- **Solutioning Phase**: Dedicated conflict prevention through ADRs
- **BMad Master**: Meta-agent orchestrating other agents

### Only in OpenSpec

- **Delta Specs**: ADDED/MODIFIED/REMOVED format for change-focused specs
- **Artifact Graph**: DAG-based dependency management with topological sort
- **Fluid Workflow**: Action-based commands without phase constraints
- **Multi-Level Resolution**: Package → User → Project schema customization
- **Fast-Forward Mode**: Create all artifacts at once
- **Three-Dimensional Verification**: Completeness, Correctness, Coherence

## Conclusions

### Philosophical Differences

1. **Governance Approach**:
   - spec-kit: Prescriptive constitution with immutable principles
   - BMAD: Descriptive context capturing existing patterns
   - OpenSpec: Configurable schemas with override hierarchy

2. **Specification Scope**:
   - spec-kit: Feature-level, technology-agnostic
   - BMAD: Product-level, comprehensive business context
   - OpenSpec: Change-level, delta-focused for brownfield

3. **Process Structure**:
   - spec-kit: Linear but iterative commands
   - BMAD: Phase-gated with specialized agents
   - OpenSpec: Dependency-driven, non-linear

### Recommendations

- **Choose spec-kit** when: Building greenfield projects needing strong
  architectural governance and test-first discipline
- **Choose BMAD** when: Working in teams needing specialized expertise
  simulation and comprehensive documentation
- **Choose OpenSpec** when: Maintaining brownfield codebases needing
  change isolation and flexible workflow

## Sources

- [spec-kit Glossary](../../framework-analyses/spec-kit/glossaries/glossary.yaml)
- [BMAD Glossary](../../framework-analyses/bmad/glossaries/glossary.yaml)
- [OpenSpec Glossary](../../framework-analyses/openspec/glossaries/glossary.yaml)
- [spec-kit Concept Mapping](../../framework-analyses/spec-kit/glossaries/concept-mapping.yaml)
- [BMAD Concept Mapping](../../framework-analyses/bmad/glossaries/concept-mapping.yaml)
- [OpenSpec Concept Mapping](../../framework-analyses/openspec/glossaries/concept-mapping.yaml)
