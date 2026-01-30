# Cross-Analysis: Roles

## Overview

This analysis compares how spec-kit, BMAD, and OpenSpec define actors in
the development process. Each framework takes a distinct approach to
representing AI agents and human participants.

## Role Comparison

| Role Type | spec-kit | BMAD | OpenSpec |
|-----------|----------|------|----------|
| AI Agent Model | Single agent | Multiple personas | Single agent |
| Agent Names | None | John, Winston, Amelia, etc. | None |
| Human Role | User | Stakeholder | User |
| Orchestration | Commands | BMad Master | OPSX commands |
| Specialization | Via commands | Via personas | Via artifacts |

## Agent Models

### spec-kit: Single Agent with Commands

spec-kit uses a **unified agent model** where a single AI agent executes
different commands. The agent doesn't have a persona - it's a tool that
responds to slash commands.

```text
┌─────────────────────────────────────────────────────────────────┐
│                        Single AI Agent                          │
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐            │
│  │/speckit.    │  │/speckit.    │  │/speckit.    │  ...        │
│  │ specify     │  │ plan        │  │ implement   │            │
│  └─────────────┘  └─────────────┘  └─────────────┘            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │      User       │
                    │ (provides input,│
                    │ answers Clarify)│
                    └─────────────────┘
```

**Characteristics**:

- No personality or identity
- Behavior determined by command context
- User interacts directly with commands
- Constitution provides governance, not persona

### BMAD: Multiple Specialized Personas

BMAD uses a **multi-agent collaboration model** with named personas, each
having distinct identities, communication styles, and expertise areas.

```text
┌─────────────────────────────────────────────────────────────────┐
│                       BMad Master                               │
│                    (Orchestrator)                               │
│                          │                                      │
│    ┌─────────────────────┼─────────────────────┐               │
│    │                     │                     │               │
│    ▼                     ▼                     ▼               │
│ ┌──────────┐       ┌──────────┐        ┌──────────┐           │
│ │ John     │       │ Winston  │        │ Amelia   │           │
│ │ (PM)     │       │(Architect│        │(Developer│    ...    │
│ │ - PRD    │       │ - ADRs   │        │ - Code   │           │
│ │ - Epics  │       │ - Design │        │ - Stories│           │
│ └──────────┘       └──────────┘        └──────────┘           │
│                                                                 │
│ ┌──────────┐       ┌──────────┐        ┌──────────┐           │
│ │ Mary     │       │ Sally    │        │ Bob      │           │
│ │(Analyst) │       │(UX)      │        │(Scrum    │           │
│ │- Research│       │- Flows   │        │ Master)  │           │
│ │- Brief   │       │- UX Spec │        │- Sprints │           │
│ └──────────┘       └──────────┘        └──────────┘           │
│                                                                 │
│ ┌──────────┐       ┌──────────┐                                │
│ │ Barry    │       │ Quinn    │                                │
│ │(Quick    │       │ (QA)     │                                │
│ │ Flow Dev)│       │- Testing │                                │
│ └──────────┘       └──────────┘                                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │   Stakeholder   │
                    │ (decisions at   │
                    │ HALT points)    │
                    └─────────────────┘
```

**Named Agents**:

| Agent | Role | Responsibilities |
|-------|------|-----------------|
| BMad Master | Orchestrator | Party Mode, `/bmad-help` |
| John | PM | PRD creation, requirements |
| Winston | Architect | System design, ADRs |
| Amelia | Developer | Story implementation |
| Bob | Scrum Master | Sprint management |
| Mary | Analyst | Brainstorming, research |
| Sally | UX Designer | User flows, wireframes |
| Quinn | QA | Test automation |
| Barry | Quick Flow Dev | Minimum ceremony development |

**Characteristics**:

- Named experts with personalities
- Distinct communication styles
- Specialized workflows per agent
- Party Mode enables multi-agent collaboration
- BMad Master orchestrates interactions

### OpenSpec: Single Agent with Commands

OpenSpec uses a **single agent model** similar to spec-kit, but with an
action-based command system (OPSX) rather than sequential commands.

```text
┌─────────────────────────────────────────────────────────────────┐
│                        Single AI Agent                          │
│                                                                 │
│  OPSX Commands (available based on dependencies)               │
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐            │
│  │/opsx:new    │  │/opsx:       │  │/opsx:apply  │            │
│  │             │  │ continue    │  │             │            │
│  └─────────────┘  └─────────────┘  └─────────────┘            │
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐            │
│  │/opsx:ff     │  │/opsx:verify │  │/opsx:       │            │
│  │             │  │             │  │ archive     │            │
│  └─────────────┘  └─────────────┘  └─────────────┘            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │      User       │
                    │ (invokes        │
                    │ commands)       │
                    └─────────────────┘
```

**Characteristics**:

- No personality or identity
- Commands available based on artifact state
- User drives workflow by invoking commands
- Schema defines behavior, not persona

## Human Involvement

### When Humans Participate

| Framework | Trigger | Interaction Style |
|-----------|---------|-------------------|
| spec-kit | Clarify questions | Multiple-choice or short-phrase answers |
| BMAD | HALT at menus | Decision selection |
| OpenSpec | Command invocation | User initiates all actions |

### Decision Authority

| Decision Type | spec-kit | BMAD | OpenSpec |
|--------------|----------|------|----------|
| Requirement decisions | User via Clarify | Stakeholder at HALTs | User (any time) |
| Technical decisions | AI follows constitution | Relevant agent (Winston) | User + Design doc |
| Process decisions | Linear flow | Agent workflows | User via commands |
| Quality validation | AI via Analyze | Readiness Check agents | User invokes Verify |

## Unique Role Patterns

### spec-kit: Constitution-Governed Agent

The agent's behavior is constrained by the constitution's 9 articles. This
creates an implicit "governance role" that shapes all interactions:

- Library-First principle limits architectural choices
- Test-First Imperative mandates TDD
- Simplicity Gate caps project complexity

### BMAD: Party Mode Collaboration

Unique multi-agent feature where multiple personas participate in one
conversation:

```text
User: Let's discuss the authentication approach

BMad Master: Activating Party Mode with John (PM), Winston (Architect),
             and Amelia (Developer)

John: From a product perspective, we need OAuth2 for enterprise clients...

Winston: Architecturally, I recommend a token service pattern with...

Amelia: Implementation-wise, I'd use passport.js with custom strategies...
```

Use cases: Big decisions, brainstorming, retrospectives

### OpenSpec: Artifact-Driven Authority

Instead of personas, OpenSpec delegates authority to artifacts:

- **Proposal** defines scope authority
- **Specs** define requirement authority
- **Design** defines technical authority
- **Tasks** define implementation authority

## Command/Agent Mapping

### spec-kit Commands → No Agent

| Command | Purpose | Agent? |
|---------|---------|--------|
| `/speckit.constitution` | Create principles | No |
| `/speckit.specify` | Create specification | No |
| `/speckit.clarify` | Resolve ambiguities | No |
| `/speckit.plan` | Create design | No |
| `/speckit.analyze` | Validate | No |
| `/speckit.tasks` | Create breakdown | No |
| `/speckit.implement` | Execute | No |

### BMAD Commands → Named Agents

| Command | Agent | Role |
|---------|-------|------|
| `/brainstorm` | Mary | Analyst |
| `/product-brief` | Mary | Analyst |
| `/create-prd` | John | PM |
| `/create-ux` | Sally | UX Designer |
| `/create-architecture` | Winston | Architect |
| `/create-epics` | John/Bob | PM/SM |
| `/create-story` | Bob | Scrum Master |
| `/dev-story` | Amelia | Developer |
| `/qa` | Quinn | QA |
| `/quick-spec` | Barry | Quick Flow Dev |
| `/quick-dev` | Barry | Quick Flow Dev |

### OpenSpec Commands → No Agent

| Command | Purpose | Agent? |
|---------|---------|--------|
| `/opsx:explore` | Investigation | No |
| `/opsx:new` | Create change | No |
| `/opsx:continue` | Next artifact | No |
| `/opsx:ff` | All artifacts | No |
| `/opsx:apply` | Implement | No |
| `/opsx:verify` | Validate | No |
| `/opsx:sync` | Merge specs | No |
| `/opsx:archive` | Complete | No |

## Conclusions

### Role Design Philosophy

1. **spec-kit**: Tool-centric
   - Agent is a utility responding to commands
   - Governance via constitution, not persona
   - User maintains control through command invocation

2. **BMAD**: Team-centric
   - Agents simulate specialized team members
   - Collaboration mirrors human team dynamics
   - Orchestrator (BMad Master) coordinates

3. **OpenSpec**: Artifact-centric
   - Agent is invisible; artifacts carry authority
   - Dependencies drive workflow, not roles
   - User orchestrates via command selection

### Trade-offs

| Aspect | Single Agent | Multi-Persona |
|--------|--------------|---------------|
| Simplicity | Higher | Lower |
| Context switching | None | Between agents |
| Expertise simulation | Generic | Specialized |
| Learning curve | Lower | Higher |
| Collaboration feel | Tool use | Team interaction |

### Recommendations

- **Choose spec-kit roles** when: Simplicity valued, clear governance needed,
  single-agent model sufficient
- **Choose BMAD roles** when: Team simulation valuable, specialized expertise
  matters, collaborative feel desired
- **Choose OpenSpec roles** when: Minimal role overhead preferred, artifact
  authority sufficient, flexible workflow needed

## Sources

- [spec-kit Glossary](../../framework-analyses/spec-kit/glossaries/glossary.yaml)
- [BMAD Glossary](../../framework-analyses/bmad/glossaries/glossary.yaml)
- [OpenSpec Glossary](../../framework-analyses/openspec/glossaries/glossary.yaml)
- [BMAD Context Organization](../../framework-analyses/bmad/descriptions/context-organization.md)
