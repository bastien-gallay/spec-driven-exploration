# Status Tracking

This directory tracks progress of the spec-driven development analysis workflow.

## Structure

```text
status/
├── framework-analyses/     # Per-framework analysis progress
│   ├── spec-kit.yaml
│   ├── bmad.yaml
│   └── openspec.yaml
└── cross-analyses/         # Cross-framework analysis progress
    ├── by-theme.yaml
    ├── pairwise.yaml
    └── synthesis.yaml
```

## Status Values

| Status | Meaning |
|--------|---------|
| `pending` | Not started |
| `in-progress` | Currently being worked on |
| `completed` | Finished and validated |
| `skipped` | Intentionally skipped |

## Validation Status

| Status | Meaning |
|--------|---------|
| `not-started` | Validation never run |
| `passed` | All checks passed |
| `passed-with-warnings` | Passed with minor issues |
| `failed` | Critical issues found |

## Updating Status

Status files are updated by the analysis prompts in `.assist/commands/`.
Each prompt updates its corresponding section when work completes.

## Schema

See `.assist/schemas/status.schema.yaml` for the full schema definition.
