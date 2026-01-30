# Pairwise Comparison: spec-kit vs OpenSpec

## Overview

| Aspect | spec-kit | OpenSpec |
|--------|----------|----------|
| Philosophy | Constitution-driven, immutable principles | Fluid, action-based, brownfield-first |
| Complexity | Medium (7 sequential steps) | Low (action commands, no phases) |
| Strictness | High (9 formal articles) | Flexible (dependencies as enablers) |
| Workflow | Sequential commands | DAG-based artifact graph |
| Primary Focus | Greenfield with governance | Brownfield with minimal ceremony |

## Key Similarities

### Similarity 1: Specification as Source of Truth

Both frameworks treat specifications as the primary artifact:

- **spec-kit**: "Specifications drive code generation rather than the reverse"
- **OpenSpec**: "Agreement before implementation" with artifacts defining
  requirements

Neither framework treats code as the source of truth.

### Similarity 2: Implementation Plan/Design Artifact

Both create technical design documents before implementation:

- **spec-kit**: `plan.md` with data models and contracts
- **OpenSpec**: `design.md` with technical approach

Both separate the WHAT (specs) from the HOW (design).

### Similarity 3: Task-Based Execution

Both break implementation into checkable tasks:

- **spec-kit**: `tasks.md` with phase organization
- **OpenSpec**: `tasks.md` with numbered checkboxes

Both track progress through explicit task completion.

### Similarity 4: Validation Step

Both include verification before completion:

- **spec-kit**: `/speckit.analyze` performs consistency checks
- **OpenSpec**: `/opsx:verify` checks completeness, correctness, coherence

Both ensure implementation matches specification intent.

## Key Differences

### Difference 1: Governance Model

**spec-kit**: Formal constitution with 9 immutable articles. Every project
operates under explicit governance defining Library-First design, CLI mandates,
TDD requirements, and more.

**OpenSpec**: Configuration-based context without formal governance. Project
settings define conventions (tech stack, API style, testing framework) but don't
mandate architectural principles.

**Implications**:

- spec-kit enforces architectural consistency across features
- OpenSpec adapts to existing project conventions
- Teams with strict standards prefer spec-kit; brownfield teams prefer OpenSpec

### Difference 2: Workflow Structure

**spec-kit**: Sequential 7-step commands that must be followed in order
(constitution → specify → clarify → plan → analyze → tasks → implement).

**OpenSpec**: Fluid action-based commands available when dependencies are met.
Can update specs during implementation; no artificial phase gates.

**Implications**:

- spec-kit is predictable but inflexible
- OpenSpec allows iteration and course correction
- Unclear requirements suit OpenSpec's iterative approach

### Difference 3: Brownfield Support

**spec-kit**: Primarily designed for greenfield development. Brownfield requires
adapting existing code to constitutional principles.

**OpenSpec**: Explicitly "built for brownfield" with delta specs focusing on
ADDED, MODIFIED, and REMOVED requirements rather than full document rewrites.

**Implications**:

- Existing codebases integrate more naturally with OpenSpec
- spec-kit requires more upfront adaptation for brownfield
- Feature modifications favor OpenSpec's delta approach

### Difference 4: Clarification Handling

**spec-kit**: Dedicated `/speckit.clarify` step with `[NEEDS CLARIFICATION]`
markers, session question limits (max 10), and structured ambiguity detection.

**OpenSpec**: No explicit clarification step. `/opsx:explore` provides thinking
space, but ambiguity resolution happens organically during artifact creation.

**Implications**:

- spec-kit catches ambiguities systematically and early
- OpenSpec relies on iterative refinement to surface issues
- Vague requirements benefit from spec-kit's explicit clarification

### Difference 5: Parallel Work Support

**spec-kit**: Features in isolated folders (`specs/###-feature-name/`), but no
explicit parallel work tooling. Sequential workflow implies single-feature
focus.

**OpenSpec**: Built for parallel changes with isolated folders
(`changes/feature-name/`), explicit `/opsx:apply <change-name>` switching, and
`/opsx:bulk-archive` for completing multiple changes.

**Implications**:

- Multi-stream development favors OpenSpec
- spec-kit suits focused, single-feature work
- Teams working on multiple features simultaneously prefer OpenSpec

### Difference 6: Artifact Management

**spec-kit**: Linear artifact creation following workflow sequence. Artifacts
are outputs of specific commands.

**OpenSpec**: DAG-based artifact graph with topological sorting. Dependencies
determine creation order; multiple artifacts can be created in parallel when
dependencies are satisfied.

**Implications**:

- spec-kit is simpler to understand
- OpenSpec optimizes for minimal blocking
- Fast-forward (`/opsx:ff`) creates all artifacts at once for clear requirements

## Concept Mapping

| spec-kit | OpenSpec | Match Level | Notes |
|----------|----------|-------------|-------|
| Constitution | Config | Partial | Both set project constraints; constitution is formal |
| Feature Specification | Proposal + Specs | Partial | OpenSpec separates WHY (proposal) from WHAT (specs) |
| Implementation Plan | Design | Exact | Both describe HOW to implement |
| Tasks | Tasks | Exact | Identical concept |
| Clarify | (none) | None | No explicit clarification in OpenSpec |
| Analyze | Verify | Partial | Different timing: analyze is pre-task, verify is post-impl |
| (none) | Delta Spec | None | No change-focused spec format in spec-kit |
| (none) | Fast-Forward | None | No artifact batch creation in spec-kit |
| (none) | Archive | None | No formal completion/preservation workflow in spec-kit |
| (none) | Explore | None | No thinking-without-artifacts command in spec-kit |

## Use Case Comparison

| Use Case | Better Choice | Why |
|----------|---------------|-----|
| Greenfield project | spec-kit | Constitution establishes solid foundation |
| Existing codebase (brownfield) | OpenSpec | Delta specs and brownfield-first design |
| TDD-required projects | spec-kit | Test-First Imperative mandated |
| Parallel feature development | OpenSpec | Change isolation and bulk archive |
| Strict governance needs | spec-kit | Formal constitutional articles |
| Minimal ceremony | OpenSpec | Lightweight setup, fluid workflow |
| Unclear requirements | Either | spec-kit clarifies early; OpenSpec iterates |
| Fast prototyping | OpenSpec | Fast-forward creates all artifacts at once |
| Teams preferring flexibility | OpenSpec | No phase gates, action-based workflow |
| Teams preferring structure | spec-kit | Sequential commands, clear progression |

## Migration Considerations

### spec-kit to OpenSpec

**What to expect**:

1. **Lose formal governance**: Constitutional articles become project config
   context. No mandated principles; teams must self-enforce.
2. **Gain workflow flexibility**: Can iterate on specs during implementation,
   work on multiple changes simultaneously.
3. **Simpler brownfield integration**: Delta specs focus on changes, not full
   rewrites.
4. **Archive for preservation**: Completed changes retain full context.

**Migration steps**:

1. Extract constitution principles into OpenSpec config context:

   ```yaml
   context: |
     Architecture: Library-first design
     Testing: TDD required, integration-first
     Interface: CLI with JSON support
   ```

2. Convert feature specifications to proposal + specs format:
   - WHY and scope → `proposal.md`
   - Requirements → `specs/[domain]/spec.md`
3. Adapt to fluid workflow: use `/opsx:explore` before committing to artifacts
4. Leverage `/opsx:ff` for clear requirements to speed iteration

### OpenSpec to spec-kit

**What to expect**:

1. **Lose workflow fluidity**: Sequential steps replace action-based commands.
   Cannot update specs during implementation.
2. **Gain governance formality**: Clear, mandated architectural principles.
3. **Required TDD**: Test-First Imperative is non-negotiable.
4. **Single-feature focus**: Parallel change workflow not supported.

**Migration steps**:

1. Create constitution from project conventions:
   - Identify architectural decisions, elevate to articles
   - Add TDD mandate if not already practiced
2. Convert proposal + specs to unified feature specification
3. Introduce `/speckit.clarify` practice for ambiguity detection
4. Add `[NEEDS CLARIFICATION]` markers (max 3) for unresolved questions
5. Adapt to single-feature workflow: complete changes sequentially

## Conclusions

**Choose spec-kit when**:

- Starting new projects (greenfield)
- Architectural governance is critical
- TDD is a core practice
- Clear sequential workflow is preferred
- Projects have well-defined scope upfront

**Choose OpenSpec when**:

- Working with existing codebases (brownfield)
- Parallel feature development is common
- Minimal ceremony is desired
- Requirements evolve during development
- Team prefers flexibility over structure
