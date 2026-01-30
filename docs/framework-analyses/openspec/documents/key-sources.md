# Key Sources - OpenSpec

## Primary Documentation

| Document | Path | Description |
|----------|------|-------------|
| README | [README.md](../../references/OpenSpec/README.md) | Main overview and quick start |
| Concepts | [docs/concepts.md](../../references/OpenSpec/docs/concepts.md) | Core concepts and terminology |
| Workflows | [docs/workflows.md](../../references/OpenSpec/docs/workflows.md) | Practical workflow patterns |
| OPSX Reference | [docs/opsx.md](../../references/OpenSpec/docs/opsx.md) | OPSX architecture and commands |

## Schema Definition

| File | Path | Description |
|------|------|-------------|
| Schema YAML | [schemas/spec-driven/schema.yaml](../../references/OpenSpec/schemas/spec-driven/schema.yaml) | Default workflow definition |

## Templates

| Template | Path | Purpose |
|----------|------|---------|
| Proposal | [schemas/spec-driven/templates/proposal.md](../../references/OpenSpec/schemas/spec-driven/templates/proposal.md) | Change proposal |
| Specification | [schemas/spec-driven/templates/spec.md](../../references/OpenSpec/schemas/spec-driven/templates/spec.md) | Requirements and scenarios |
| Design | [schemas/spec-driven/templates/design.md](../../references/OpenSpec/schemas/spec-driven/templates/design.md) | Technical approach |
| Tasks | [schemas/spec-driven/templates/tasks.md](../../references/OpenSpec/schemas/spec-driven/templates/tasks.md) | Implementation checklist |

## Artifact Graph Source Code

| File | Path | Purpose |
|------|------|---------|
| Types | [src/core/artifact-graph/types.ts](../../references/OpenSpec/src/core/artifact-graph/types.ts) | Type definitions and schemas |
| Graph | [src/core/artifact-graph/graph.ts](../../references/OpenSpec/src/core/artifact-graph/graph.ts) | DAG with topological sort |
| State | [src/core/artifact-graph/state.ts](../../references/OpenSpec/src/core/artifact-graph/state.ts) | Filesystem-based detection |
| Instruction Loader | [src/core/artifact-graph/instruction-loader.ts](../../references/OpenSpec/src/core/artifact-graph/instruction-loader.ts) | Enriched instructions |
| Schema | [src/core/artifact-graph/schema.ts](../../references/OpenSpec/src/core/artifact-graph/schema.ts) | Validation and parsing |
| Resolver | [src/core/artifact-graph/resolver.ts](../../references/OpenSpec/src/core/artifact-graph/resolver.ts) | Multi-level resolution |

## Directory Structure Reference

```text
openspec/
├── specs/                       # Source of truth (current system)
│   └── [domain]/
│       └── spec.md              # Domain specification
├── changes/                     # Work in progress
│   ├── [change-name]/           # Active change
│   │   ├── proposal.md          # Why and scope
│   │   ├── specs/               # Delta specifications
│   │   │   └── [domain]/
│   │   │       └── spec.md      # Delta spec
│   │   ├── design.md            # Technical approach
│   │   └── tasks.md             # Implementation tasks
│   └── archive/                 # Completed changes
│       └── [date]-[name]/
├── schemas/                     # Custom workflow schemas
│   └── [schema-name]/
│       └── schema.yaml
└── config.yaml                  # Project configuration
```

## OPSX Commands Reference

| Command | Purpose | Key Artifacts |
|---------|---------|---------------|
| `/opsx:explore` | Think through ideas | None |
| `/opsx:new` | Start new change | Creates change folder |
| `/opsx:continue` | Create next artifact | Based on dependencies |
| `/opsx:ff` | Fast-forward planning | All artifacts at once |
| `/opsx:apply` | Implement tasks | Code changes |
| `/opsx:verify` | Validate implementation | Verification report |
| `/opsx:sync` | Merge delta specs | Updated main specs |
| `/opsx:archive` | Complete change | Archived folder |
