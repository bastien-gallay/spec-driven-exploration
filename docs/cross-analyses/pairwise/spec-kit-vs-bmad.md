# Pairwise Comparison: spec-kit vs BMAD

## Overview

| Aspect | spec-kit | BMAD |
|--------|----------|------|
| Philosophy | Specification-first, constitution-governed | AI as collaborator, agent-specialized |
| Complexity | Medium (7 sequential commands) | High (21 agents, 50+ workflows) |
| Target | Solo developers, TDD advocates | Teams with multiple roles |
| Strictness | High (9 formal articles) | Moderate (guidelines, not mandates) |
| Workflow | Sequential commands | Four-phase lifecycle |

## Key Similarities

### Similarity 1: Specification Before Implementation

Both frameworks emphasize defining requirements before writing code:

- **spec-kit**: Feature specifications drive all downstream work
- **BMAD**: PRD and architecture documents precede implementation

Both treat documentation as a first-class artifact, not an afterthought.

### Similarity 2: Validation Gates

Both include explicit validation checkpoints:

- **spec-kit**: `/speckit.analyze` performs 6-category consistency validation
- **BMAD**: Readiness checks validate PRD and architecture completeness

Neither framework allows proceeding with incomplete specifications.

### Similarity 3: Task-Based Implementation

Both break implementation into discrete work units:

- **spec-kit**: `tasks.md` with phase organization and parallel markers
- **BMAD**: Stories with acceptance criteria and definition of done

Implementation is guided by explicit, checkable task lists.

### Similarity 4: Quality Focus

Both emphasize code quality through structured practices:

- **spec-kit**: Test-First Imperative (Article III), integration testing
- **BMAD**: Adversarial review, code review workflows

Quality is built into the process, not bolted on afterward.

## Key Differences

### Difference 1: Governance Model

**spec-kit**: Formal constitution with 9 immutable articles defining architectural
DNA (Library-First, CLI Mandate, Test-First, etc.).

**BMAD**: Informal agent personas with guidelines. No formal governance document;
behavior emerges from agent definitions and workflow step files.

**Implications**:

- spec-kit provides stronger architectural consistency but less flexibility
- BMAD adapts to different project needs but may have inconsistent patterns
- Teams valuing strict standards prefer spec-kit; teams preferring guidance
  prefer BMAD

### Difference 2: Agent Model

**spec-kit**: Single AI agent executing sequential commands. Each command
(`/speckit.specify`, `/speckit.plan`) invokes the same agent with different
prompts.

**BMAD**: 21 specialized agents with distinct personas (John the PM, Winston the
Architect, Amelia the Developer). Agents have identities, communication styles,
and specialized expertise.

**Implications**:

- spec-kit is simpler to understand and use
- BMAD provides role-appropriate perspectives but requires learning agent
  capabilities
- spec-kit suits solo work; BMAD simulates team collaboration

### Difference 3: Clarification Workflow

**spec-kit**: Dedicated `/speckit.clarify` command with structured ambiguity
detection, `[NEEDS CLARIFICATION]` markers (max 3), and session question limits.

**BMAD**: No explicit clarification step. Questions arise naturally during PRD
creation or via the brainstorming workflow's probing questions.

**Implications**:

- spec-kit catches ambiguities earlier and more systematically
- BMAD relies on workflow-embedded questioning, which may miss edge cases
- Projects with unclear requirements benefit from spec-kit's explicit
  clarification

### Difference 4: Scale Adaptivity

**spec-kit**: Single workflow track regardless of project size. All projects use
the same 7-step sequence.

**BMAD**: Three distinct tracks (Quick Flow, BMad Method, Enterprise) adapting
to project complexity from bug fixes to multi-tenant platforms.

**Implications**:

- spec-kit overhead is consistent but may be excessive for small changes
- BMAD scales ceremony appropriately but requires track selection decisions
- Small projects favor BMAD's Quick Flow; large projects suit either

### Difference 5: Collaboration Model

**spec-kit**: Human + single AI interaction. No multi-agent collaboration
concept.

**BMAD**: Party Mode enables multi-agent discussions for complex decisions,
brainstorming, and retrospectives. Agents respond in character, agree, and
disagree.

**Implications**:

- spec-kit is predictable but lacks perspective diversity
- BMAD provides richer ideation through simulated team dynamics
- Teams needing diverse viewpoints benefit from BMAD's Party Mode

## Concept Mapping

| spec-kit | BMAD | Match Level | Notes |
|----------|------|-------------|-------|
| Constitution | Product Brief | Low | Constitution is governance; brief is strategic vision |
| Feature Specification | PRD | Partial | PRD is broader, covering full product scope |
| Implementation Plan | Architecture | Partial | spec-kit is feature-level; BMAD is system-level |
| Tasks | Story | Exact | Both represent implementable work units |
| Clarify | (none) | None | No explicit clarification workflow in BMAD |
| Analyze | Readiness Check | Exact | Both are validation gates |
| Constitutional Articles | (none) | None | No formal principle articles in BMAD |
| (none) | Party Mode | None | No multi-agent collaboration in spec-kit |
| (none) | Agent Personas | None | spec-kit uses commands, not characterized agents |
| (none) | Quick Flow | None | spec-kit has no minimum-ceremony track |

## Use Case Comparison

| Use Case | Better Choice | Why |
|----------|---------------|-----|
| Solo project | spec-kit | Simpler model, no agent complexity |
| Team with multiple roles | BMAD | Role-appropriate agent perspectives |
| Greenfield with TDD focus | spec-kit | Test-First Imperative mandated |
| Bug fixes / quick changes | BMAD | Quick Flow minimizes ceremony |
| Project with strict standards | spec-kit | Constitutional governance enforces consistency |
| Complex strategic decisions | BMAD | Party Mode provides diverse perspectives |
| Brownfield development | BMAD | Project context workflow, agent adaptation |
| Small to medium features | Either | Both handle this scale well |
| Enterprise compliance | BMAD | Extended artifact track for compliance |
| Rapid prototyping | BMAD | Quick Flow enables fast iteration |

## Migration Considerations

### spec-kit to BMAD

**What to expect**:

1. **Lose governance formality**: Constitutional articles become guidelines, not
   mandates. Teams must self-enforce architectural standards.
2. **Gain flexibility**: Can choose appropriate ceremony level (Quick Flow vs
   full method).
3. **Learn agent model**: Understanding 21 agent personas and when to invoke
   each.
4. **Adapt documentation**: Feature specs become PRDs; clarification happens
   within workflows.

**Migration steps**:

1. Review existing constitution, extract key principles for architecture ADRs
2. Map feature specifications to PRD format
3. Convert tasks to story format with acceptance criteria
4. Use Quick Flow for ongoing changes while learning full method

### BMAD to spec-kit

**What to expect**:

1. **Lose scale adaptivity**: All projects follow the same 7-step workflow,
   regardless of size.
2. **Gain governance clarity**: Explicit articles define non-negotiable
   standards.
3. **Simpler mental model**: Single agent, sequential commands.
4. **Mandatory TDD**: Test-First Imperative is non-negotiable.

**Migration steps**:

1. Create constitution from architecture ADRs and project conventions
2. Convert PRDs to feature specification format
3. Add `[NEEDS CLARIFICATION]` markers for ambiguous requirements
4. Establish `/speckit.clarify` practice before planning
5. Adapt to integration-first testing if not already practiced

## Conclusions

**Choose spec-kit when**:

- Working solo or with small teams
- TDD is a core practice
- Consistent architectural standards are paramount
- Projects are greenfield with well-defined scope
- Governance and formal principles are valued

**Choose BMAD when**:

- Multiple team roles need representation
- Project complexity varies (bugs to enterprise systems)
- Party Mode collaboration adds value
- Brownfield development is common
- Flexible ceremony levels are desired
