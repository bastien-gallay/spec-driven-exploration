# Concept Mapping - OpenSpec

## Mapping to Common SDD Vocabulary

| OpenSpec Term | Common SDD Term | Notes |
|---------------|-----------------|-------|
| Proposal | Project Brief/Charter | Intent and scope |
| Specs | Requirements Specification | RFC 2119 format |
| Design | Design Document | Technical approach |
| Tasks | Work Items/Checklist | Implementation steps |
| Change | Feature/Work Package | Isolated unit of work |
| Archive | Completed/Closed | Historical record |
| Schema | Workflow Definition | Process template |
| Domain | Module/Component | Logical grouping |

## Comparison with Other Frameworks

### OpenSpec vs BMAD

| OpenSpec | BMAD | Semantic Match |
|----------|------|----------------|
| Proposal | Product Brief | Partial - different scope |
| Specs | PRD | Partial - OpenSpec narrower |
| Design | Architecture | High - technical decisions |
| Tasks | Story | High - implementation unit |
| Change | Epic | Partial - isolation model |
| `/opsx:verify` | Readiness Check | High - validation gate |
| Schema | Module | Partial - configuration |
| N/A | Agents | N/A - no agent concept |
| N/A | Party Mode | N/A - single-agent model |
| Delta Specs | N/A | OpenSpec-specific |

### OpenSpec vs spec-kit

| OpenSpec | spec-kit | Semantic Match |
|----------|----------|----------------|
| Proposal | Feature Specification | Partial - proposal is lighter |
| Specs | Feature Specification | High - requirements focus |
| Design | Implementation Plan | High - technical approach |
| Tasks | Tasks | High - same concept |
| Change | Feature folder | High - isolation model |
| Config rules | Constitution | Partial - less formal |
| `/opsx:apply` | `/speckit.implement` | High - same purpose |
| `/opsx:verify` | `/speckit.analyze` | Partial - different timing |
| Delta Specs | N/A | OpenSpec-specific |

## Unique OpenSpec Concepts

### No Direct Equivalent

| Concept | Description | Why Unique |
|---------|-------------|------------|
| Delta Specs | ADDED/MODIFIED/REMOVED sections | Change-focused specification |
| Artifact Graph | DAG-based dependency management | Algorithmic approach |
| Fluid Workflow | Actions not phases | Non-linear progression |
| Multi-Level Resolution | Package → User → Project | Schema override system |
| Fast-Forward | Create all artifacts at once | Speed optimization |

### Partially Mapped

| Concept | Closest Match | Gap |
|---------|---------------|-----|
| Archive | Completed status | OpenSpec preserves full context |
| Domain organization | Module structure | OpenSpec by logical grouping |
| Context injection | Context loading | OpenSpec via config tags |
| Verification dimensions | Quality checks | Three-dimensional validation |

## Concept Relationships

### Hierarchical Structure

```text
OpenSpec Framework
├── Schemas
│   └── spec-driven (default)
│       ├── Artifacts (4)
│       └── Templates
├── Project Structure
│   ├── specs/ (source of truth)
│   │   └── [domains]
│   ├── changes/ (work in progress)
│   │   ├── [active changes]
│   │   └── archive/
│   └── config.yaml
├── OPSX Commands (9)
│   ├── Exploration (explore)
│   ├── Creation (new, continue, ff)
│   ├── Implementation (apply)
│   ├── Validation (verify)
│   └── Completion (sync, archive, bulk-archive)
└── Artifact Graph
    ├── Dependency management
    ├── State detection
    └── Instruction generation
```

### Workflow Patterns

```text
Quick Feature:
  /opsx:new → /opsx:ff → /opsx:apply → /opsx:verify → /opsx:archive

Exploratory:
  /opsx:explore → /opsx:new → /opsx:continue → /opsx:apply

Parallel Changes:
  Multiple changes in separate folders, switch via /opsx:apply <name>
```

## Cross-Cutting Concerns

| Concern | How OpenSpec Addresses |
|---------|------------------------|
| Quality | Three-dimensional verification |
| Flexibility | Fluid actions, no phase gates |
| Brownfield | Delta specs for change focus |
| Customization | Multi-level schema resolution |
| Consistency | Context injection, rules per artifact |
| Traceability | Archive preserves full context |
| Parallel Work | Isolated change folders |

## Architectural Principles

| Principle | Implementation |
|-----------|----------------|
| Fluid not rigid | Action-based commands |
| Iterative not waterfall | Update specs during implementation |
| Easy not complex | Lightweight setup, minimal ceremony |
| Built for brownfield | Delta specs, change isolation |
| Scalable | Schema customization per project |

## Sources

- [README.md](../../references/OpenSpec/README.md)
- [Concepts](../../references/OpenSpec/docs/concepts.md)
- [Workflows](../../references/OpenSpec/docs/workflows.md)
- [OPSX Reference](../../references/OpenSpec/docs/opsx.md)
