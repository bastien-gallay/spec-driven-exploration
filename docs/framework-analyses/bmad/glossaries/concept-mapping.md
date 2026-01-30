# Concept Mapping - BMAD

## Mapping to Common SDD Vocabulary

| BMAD Term | Common SDD Term | Notes |
|-----------|-----------------|-------|
| PRD | Specification | Primary requirements document |
| Architecture | Design Document | Technical decisions via ADRs |
| Story | Task/Work Item | Implementable unit with acceptance criteria |
| Epic | Feature Group | Collection of related stories |
| Phase | Stage/Phase | Sequential development stage |
| Agent | Persona/Role | Specialized AI actor |
| Workflow | Process/Procedure | Guided sequence of steps |
| Party Mode | Multi-agent Session | Collaborative agent discussion |
| Quick Flow | Fast Track | Minimum ceremony path |
| Solutioning | Design Phase | Architecture and conflict prevention |

## Comparison with Other Frameworks

### BMAD vs spec-kit

| BMAD | spec-kit | Semantic Match |
|------|----------|----------------|
| PRD | Feature Specification | Partial - PRD is broader |
| Architecture | Implementation Plan | Partial - different focus |
| Story | Task | High - implementation unit |
| Agent | Command | Low - different concept |
| Product Brief | Constitution | Low - strategic vs governance |
| Readiness Check | Analyze | Partial - validation step |

### BMAD vs OpenSpec

| BMAD | OpenSpec | Semantic Match |
|------|----------|----------------|
| PRD | Proposal + Specs | High - combined scope |
| Architecture | Design | High - technical decisions |
| Story | Tasks | High - implementation steps |
| Phase | N/A | Low - OpenSpec is fluid |
| Agent | N/A | N/A - no agent concept |
| Workflow | OPSX commands | Partial - structured vs fluid |

## Unique BMAD Concepts

### No Direct Equivalent

| BMAD Concept | Description | Why Unique |
|--------------|-------------|------------|
| Party Mode | Multi-agent collaboration | Agent-centric approach |
| Adversarial Review | Forced problem-finding | Quality technique |
| Agent Personas | Named experts with identity | Human-like collaboration |
| Step-File Architecture | Micro-file workflow design | Implementation detail |
| Tri-Modal Workflows | Create/Validate/Edit modes | Workflow flexibility |

### Partially Mapped

| BMAD Concept | Closest Match | Gap |
|--------------|---------------|-----|
| Solutioning | Design Phase | BMAD focuses on conflict prevention |
| Brownfield Support | Delta Specs (OpenSpec) | Different mechanism |
| Context Loading | Context Injection | BMAD is per-workflow |

## Concept Relationships

### Hierarchical Structure

```text
BMAD Method
├── Phases (4)
│   ├── Analysis
│   ├── Planning
│   ├── Solutioning
│   └── Implementation
├── Agents (21)
│   ├── Core Domain (8)
│   ├── Quick Flow (1)
│   └── Master (1)
├── Workflows (50+)
│   ├── Per Phase
│   └── Quick Flow
└── Artifacts
    ├── Planning
    ├── Execution
    └── Validation
```

### Cross-Cutting Concerns

| Concern | How BMAD Addresses |
|---------|-------------------|
| Quality | Adversarial review, readiness checks |
| Context | Progressive building, per-workflow loading |
| Flexibility | Tri-modal workflows, Quick Flow track |
| Collaboration | Party Mode, agent personas |
| Consistency | Solutioning phase, ADRs |

## Sources

- [README.md](../../references/BMAD/BMAD-METHOD/README.md)
- [Workflow Map](../../references/BMAD/BMAD-METHOD/docs/reference/workflow-map.md)
- [Party Mode](../../references/BMAD/BMAD-METHOD/docs/explanation/party-mode.md)
