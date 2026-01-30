# Reading Notes - spec-kit

## Metadata

| Field | Value |
|-------|-------|
| Framework | spec-kit |
| Version Analyzed | Commit `9111699` (2025-01-30) |
| Analysis Date | 2025-01-30 |
| Repository | `docs/references/spec-kit/` |

## First Impressions

- Python CLI tool focused on specification-driven development
- 7-step workflow with clear command structure
- Constitution-based governance for project principles
- Strong template-driven approach constraining LLM behavior

## Key Observations

### Architecture

- **Constitution system**: Immutable architectural DNA with 9 articles
- **Template-driven**: Strict templates prevent premature implementation details
- **Memory system**: Persistent context in `.specify/memory/`
- **Feature-based organization**: Each feature in `specs/[###-feature-name]/`

### Philosophy

- "Specifications drive code generation, not the reverse"
- Code becomes "continuously regenerated output"
- Intent-driven development with natural language specifications
- Supports what-if/simulation experiments

### Workflow Design

- Sequential 7-step process with dedicated commands
- `/speckit.clarify` before `/speckit.plan` to reduce rework
- `/speckit.analyze` for cross-artifact consistency validation
- Test-first imperative (Article III - NON-NEGOTIABLE)

### Unique Elements

- **Constitutional Enforcement**: Pre-implementation gates validate principles
- **Library-First Principle**: Features begin as standalone libraries
- **CLI Interface Mandate**: Text input/output, JSON support
- **Quality Markers**: `[NEEDS CLARIFICATION]` for ambiguous areas

## Questions for Further Investigation

1. How are constitution amendments managed in practice?
2. What happens when clarification limit (max 3) is exceeded?
3. How does the framework handle brownfield vs greenfield differently?

## Notes During Analysis

- Clear separation between WHAT (spec) and HOW (plan)
- Supports 20+ AI coding agents
- Scripts available in both bash and PowerShell
- Strong focus on preventing over-engineering through constraints
