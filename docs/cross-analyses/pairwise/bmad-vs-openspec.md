# Pairwise Comparison: BMAD vs OpenSpec

## Overview

| Aspect | BMAD | OpenSpec |
|--------|------|----------|
| Philosophy | Multi-agent collaboration | Fluid, artifact-graph workflow |
| Complexity | High (21 agents, 4 phases) | Low (action commands, no phases) |
| Collaboration | Strong (Party Mode, personas) | Minimal (single conversation) |
| Structure | Phase-based lifecycle | Dependency-based actions |
| Scale | Bug fixes to enterprise | Personal to enterprise |

## Key Similarities

### Similarity 1: Brownfield Support

Both frameworks explicitly support existing codebases:

- **BMAD**: `document-project` workflow creates `project-context.md` with
  existing patterns and rules
- **OpenSpec**: Built for brownfield with delta specs and project config context

Neither framework assumes greenfield development.

### Similarity 2: Artifact-Driven Development

Both produce structured artifacts before implementation:

- **BMAD**: PRD, Architecture, Stories
- **OpenSpec**: Proposal, Specs, Design, Tasks

Both treat documentation as essential input for implementation.

### Similarity 3: Task/Story-Based Implementation

Both break work into implementable units:

- **BMAD**: Stories with acceptance criteria and definition of done
- **OpenSpec**: Tasks with numbered checkboxes

Both track progress through explicit completion markers.

### Similarity 4: Quality Validation

Both include validation before completion:

- **BMAD**: Readiness checks, adversarial code review
- **OpenSpec**: Three-dimensional verification (completeness, correctness,
  coherence)

Both ensure implementation quality through structured review.

### Similarity 5: Workflow Customization

Both allow adapting workflows to project needs:

- **BMAD**: Three tracks (Quick Flow, BMad Method, Enterprise) plus custom agent
  personas
- **OpenSpec**: Multi-level schema resolution (package, user, project)

Neither framework is one-size-fits-all.

## Key Differences

### Difference 1: Agent Model

**BMAD**: 21 specialized agents with distinct personas (John the PM, Winston the
Architect, Amelia the Developer). Each agent has identity, principles, and
specialized workflows. Party Mode enables multi-agent collaboration.

**OpenSpec**: Single conversation model with OPSX commands. No agent personas or
multi-agent collaboration. The AI adapts based on context, not character.

**Implications**:

- BMAD provides role-appropriate perspectives but requires learning agents
- OpenSpec is simpler but lacks perspective diversity
- Teams valuing simulated team dynamics prefer BMAD

### Difference 2: Workflow Structure

**BMAD**: Four sequential phases (Analysis → Planning → Solutioning →
Implementation). Each phase has dedicated workflows and must complete before
the next begins.

**OpenSpec**: Fluid action-based commands with no phases. Artifacts are
available when dependencies are satisfied. Can update specs during
implementation.

**Implications**:

- BMAD provides clear progression but is less flexible
- OpenSpec allows iteration and course correction at any time
- Waterfall-tolerant teams suit BMAD; agile teams suit OpenSpec

### Difference 3: Scale Adaptivity Mechanism

**BMAD**: Three explicit tracks (Quick Flow for bugs, BMad Method for products,
Enterprise for compliance). Track selection determines artifact requirements.

**OpenSpec**: Implicit scaling through command choice. `/opsx:ff` for simple
changes; step-by-step `/opsx:continue` for complex work. No explicit track
selection.

**Implications**:

- BMAD makes scale decisions explicit but requires upfront choice
- OpenSpec adapts naturally but may under- or over-engineer
- Teams preferring explicit guidance prefer BMAD's tracks

### Difference 4: Collaboration Model

**BMAD**: Multi-agent collaboration through Party Mode. Agents discuss, agree,
disagree, and build on each other's ideas. BMad Master orchestrates
conversations.

**OpenSpec**: Single conversation without collaboration simulation. No
brainstorming or multi-perspective features built in.

**Implications**:

- Complex decisions benefit from BMAD's Party Mode
- Simple features need no collaboration overhead
- Strategic planning and retrospectives favor BMAD

### Difference 5: Parallel Change Support

**BMAD**: Sprint-based approach with stories. Multiple stories can be in
progress, but no explicit parallel feature workflow or isolation mechanism.

**OpenSpec**: Explicit change isolation with folders (`changes/feature-name/`),
switching between changes (`/opsx:apply <change>`), and bulk archive for
completing multiple changes.

**Implications**:

- Multiple independent features favor OpenSpec
- BMAD suits sprint-focused delivery
- Parallel development streams prefer OpenSpec

### Difference 6: Delta Specification

**BMAD**: Full PRD and architecture documents. Updates require modifying
existing documents with tri-modal workflows (create, validate, edit).

**OpenSpec**: Delta specs with ADDED, MODIFIED, REMOVED sections. Focus on
what's changing rather than restating everything.

**Implications**:

- Frequent small changes favor OpenSpec's delta approach
- Full product planning suits BMAD's comprehensive documents
- Brownfield modifications prefer OpenSpec

## Concept Mapping

| BMAD | OpenSpec | Match Level | Notes |
|------|----------|-------------|-------|
| Product Brief | Proposal | Partial | Product-level vs change-level scope |
| PRD | Specs | Partial | PRD is broader; specs are delta-focused |
| Architecture | Design | Exact | Both capture technical decisions |
| Story | Tasks | Exact | Both represent implementation units |
| Phase | (none) | None | OpenSpec has no phases |
| Agent | (none) | None | OpenSpec has no agent personas |
| Party Mode | (none) | None | No multi-agent collaboration in OpenSpec |
| Quick Flow | Fast-Forward | Low | Different mechanisms for minimum ceremony |
| Readiness Check | (none) | None | OpenSpec has no pre-implementation gate |
| (none) | Delta Spec | None | BMAD uses full documents |
| (none) | Archive | None | BMAD doesn't preserve change context |
| (none) | Artifact Graph | None | BMAD uses phase sequence |
| Sprint Status | (none) | None | OpenSpec has no sprint tracking |

## Use Case Comparison

| Use Case | Better Choice | Why |
|----------|---------------|-----|
| Team with multiple roles | BMAD | Agent personas match team roles |
| Solo developer | OpenSpec | Simpler model, no agent complexity |
| Complex strategic decisions | BMAD | Party Mode provides perspectives |
| Quick bug fixes | Either | BMAD Quick Flow or OpenSpec minimal |
| Parallel features | OpenSpec | Change isolation and bulk archive |
| Full product planning | BMAD | Comprehensive PRD and architecture |
| Incremental improvements | OpenSpec | Delta specs for focused changes |
| Enterprise compliance | BMAD | Extended track with compliance artifacts |
| Brownfield modifications | OpenSpec | Delta specs, brownfield-first |
| Sprint-based delivery | BMAD | Sprint status tracking, stories |
| Retrospectives | BMAD | Party Mode for team reflection |
| Flexible iteration | OpenSpec | No phase gates, any-time updates |

## Migration Considerations

### BMAD to OpenSpec

**What to expect**:

1. **Lose agent perspectives**: No more role-based personas or Party Mode.
   Single AI conversation replaces multi-agent collaboration.
2. **Gain workflow flexibility**: Can iterate on any artifact at any time;
   no phase gates.
3. **Simplified model**: Fewer concepts to learn; action commands replace
   agent workflows.
4. **Delta-focused changes**: Focus on what's changing, not full rewrites.

**Migration steps**:

1. Convert PRD to proposal + specs format:
   - Problem statement, goals → `proposal.md`
   - Requirements → delta specs with ADDED sections
2. Convert architecture to design format:
   - ADRs become inline design decisions
   - Technical approach documented in `design.md`
3. Convert stories to task format:
   - Acceptance criteria inform task descriptions
   - Definition of done embedded in task completion criteria
4. Adapt to fluid workflow: use `/opsx:explore` for thinking, `/opsx:ff` for
   clear requirements

### OpenSpec to BMAD

**What to expect**:

1. **Lose workflow fluidity**: Four phases replace action commands. Must
   complete Planning before Solutioning.
2. **Gain agent perspectives**: 21 personas provide role-appropriate guidance.
   Party Mode enables collaborative decisions.
3. **More comprehensive documentation**: Full PRD and architecture instead of
   delta specs.
4. **Sprint-based delivery**: Stories and sprint status for tracking.

**Migration steps**:

1. Convert proposal to product brief format:
   - Add strategic context (vision, market, users)
   - Expand scope beyond single change
2. Convert delta specs to full PRD:
   - Document all requirements, not just changes
   - Add user personas and success metrics
3. Convert design to architecture format:
   - Structure decisions as ADRs
   - Add system diagrams and integration patterns
4. Convert tasks to stories:
   - Add acceptance criteria for each story
   - Include definition of done
5. Learn agent model: understand when to invoke John (PM), Winston (Architect),
   Amelia (Developer)

## Conclusions

**Choose BMAD when**:

- Team has multiple roles needing representation
- Complex decisions benefit from multi-perspective discussion
- Full product planning is needed (not just incremental changes)
- Sprint-based delivery aligns with team cadence
- Enterprise compliance requirements exist

**Choose OpenSpec when**:

- Working solo or with small team
- Parallel feature development is common
- Changes are incremental improvements to existing systems
- Minimal ceremony and flexibility are priorities
- Brownfield development is the norm
