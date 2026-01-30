# Reading Notes - OpenSpec

## Metadata

| Field | Value |
|-------|-------|
| Framework | OpenSpec |
| Version Analyzed | Commit `3768694` (2025-01-30) |
| Analysis Date | 2025-01-30 |
| Repository | `docs/references/OpenSpec/` |

## First Impressions

- TypeScript-based framework with fluid, iterative approach
- Built specifically for brownfield development
- Artifact graph system for dependency management
- OPSX workflow with action-based commands (not phase-based)

## Key Observations

### Architecture

- **Artifact graph**: DAG-based system for managing artifact dependencies
- **Delta specs**: Focus on changes rather than full specification rewrites
- **Schema-driven workflows**: Customizable artifact definitions
- **Multi-level resolution**: Package → User → Project schema overrides

### Philosophy

- "Fluid not rigid" - no phase gates, work on what makes sense
- "Iterative not waterfall" - learn as you build
- "Easy not complex" - lightweight setup, minimal ceremony
- "Built for brownfield" - works with existing codebases

### Workflow Design

- Action-based commands (`/opsx:explore`, `/opsx:new`, `/opsx:continue`)
- Fast-forward option (`/opsx:ff`) for quick planning
- Verification before archive across completeness, correctness, coherence
- Changes isolated in folders, archived when complete

### Unique Elements

- **Delta Specs**: ADDED/MODIFIED/REMOVED sections for changes
- **Artifact Graph**: Topological sort with Kahn's algorithm
- **RFC 2119 Keywords**: MUST/SHALL/SHOULD/MAY for requirements
- **Context Injection**: Project config embedded in AI instructions

## Questions for Further Investigation

1. How are spec conflicts resolved during bulk archive?
2. What is the overhead of maintaining separate change folders?
3. How does the framework handle large-scale refactoring?

## Notes During Analysis

- Clean separation between `openspec/specs/` (source of truth) and
  `openspec/changes/` (work in progress)
- State detected from filesystem, not metadata
- Templates use structured markdown with clear sections
- Verification validates three dimensions: completeness, correctness, coherence
