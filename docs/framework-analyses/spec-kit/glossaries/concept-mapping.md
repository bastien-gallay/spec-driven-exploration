# Concept Mapping - spec-kit

## Mapping to Common SDD Vocabulary

| spec-kit Term | Common SDD Term | Notes |
|---------------|-----------------|-------|
| Constitution | Governance/Principles | Project-level constraints |
| Feature Specification | Requirements Spec | WHAT and WHY document |
| Implementation Plan | Design Document | HOW document |
| Tasks | Work Items/Checklist | Implementation steps |
| Clarify | Requirements Refinement | Ambiguity resolution |
| Analyze | Validation/Review | Cross-artifact check |
| Research | Technical Investigation | Technology decisions |
| Contracts | API Specification | Interface definitions |

## Comparison with Other Frameworks

### spec-kit vs BMAD

| spec-kit | BMAD | Semantic Match |
|----------|------|----------------|
| Constitution | Product Brief | Low - different purpose |
| Feature Specification | PRD | Partial - spec-kit narrower |
| Implementation Plan | Architecture | Partial - different focus |
| Tasks | Story | High - implementation unit |
| `/speckit.specify` | Create PRD workflow | Partial - scope differs |
| `/speckit.analyze` | Readiness Check | High - validation gate |
| N/A | Agents | N/A - no agent concept |
| N/A | Party Mode | N/A - single-agent model |

### spec-kit vs OpenSpec

| spec-kit | OpenSpec | Semantic Match |
|----------|----------|----------------|
| Constitution | Config rules | Partial - more formal |
| Feature Specification | Proposal + Specs | High - combined scope |
| Implementation Plan | Design | High - technical approach |
| Tasks | Tasks | High - same concept |
| Clarify | N/A | spec-kit-specific |
| Analyze | Verify | Partial - different timing |
| `/speckit.implement` | `/opsx:apply` | High - same purpose |

## Unique spec-kit Concepts

### No Direct Equivalent

| Concept | Description | Why Unique |
|---------|-------------|------------|
| Constitution | Immutable architectural DNA | Formal governance |
| 9 Articles | Specific development principles | Prescriptive constraints |
| Test-First Imperative | Non-negotiable TDD requirement | Strict enforcement |
| Library-First Principle | Features as standalone libraries | Architectural pattern |
| CLI Interface Mandate | Text I/O requirement | Interface constraint |

### Partially Mapped

| Concept | Closest Match | Gap |
|---------|---------------|-----|
| Clarify workflow | Requirements refinement | Structured ambiguity detection |
| Quickstart document | Test scenarios | Focused validation scenarios |
| Constitution Gates | Quality gates | Principle-based validation |

## Concept Relationships

### Hierarchical Structure

```text
spec-kit Framework
├── Constitution (1)
│   └── 9 Articles
├── Commands (7)
│   ├── constitution
│   ├── specify
│   ├── clarify
│   ├── plan
│   ├── analyze
│   ├── tasks
│   └── implement
├── Artifacts
│   ├── Governance (constitution)
│   ├── Specification (spec.md)
│   ├── Design (plan.md + supporting)
│   └── Execution (tasks.md)
└── Templates
    ├── Document templates
    └── Command workflows
```

### Workflow Sequence

```text
/speckit.constitution
        │
        ▼
/speckit.specify
        │
        ▼
/speckit.clarify (iterate)
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

## Cross-Cutting Concerns

| Concern | How spec-kit Addresses |
|---------|------------------------|
| Quality | Test-First Imperative, Integration-First |
| Governance | Constitution with 9 articles |
| Simplicity | Articles VII and VIII constraints |
| Ambiguity | NEEDS CLARIFICATION markers, max 3 |
| Consistency | Analyze workflow, templates |
| Traceability | User story markers in tasks |

## Sources

- [README.md](../../references/spec-kit/README.md)
- [Spec-Driven Philosophy](../../references/spec-kit/spec-driven.md)
- [Quick Start](../../references/spec-kit/docs/quickstart.md)
