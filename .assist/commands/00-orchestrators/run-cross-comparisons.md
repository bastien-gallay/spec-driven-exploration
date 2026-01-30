---
name: run-cross-comparisons
description: Run complete cross-comparison analysis
arguments: []
outputs:
  - path: docs/cross-analyses/by-theme/
  - path: docs/cross-analyses/pairwise/
status_file: .assist/status/cross-analyses/
---

# Orchestrator: Run Cross-Comparisons

Execute the complete cross-comparison workflow.

## Overview

This orchestrator runs all cross-comparison steps:

1. **03a-by-theme** - Compare frameworks across themes
2. **03b-pairwise** - Compare frameworks in pairs
3. **03v-validate** - Validate the analysis

## Prerequisites

All framework analyses must be complete:

- `.assist/status/framework-analyses/spec-kit.yaml`: `ready_for_cross_analysis: true`
- `.assist/status/framework-analyses/bmad.yaml`: `ready_for_cross_analysis: true`
- `.assist/status/framework-analyses/openspec.yaml`: `ready_for_cross_analysis: true`

## Execution Flow

```text
┌─────────────────────────────────────────────────────────────────┐
│                    Cross-Comparisons                             │
│                                                                  │
│  ┌──────────────────────┐    ┌──────────────────────┐           │
│  │     By-Theme         │    │      Pairwise        │           │
│  │      (03a)           │    │       (03b)          │           │
│  │                      │    │                      │           │
│  │  - concepts.md       │    │  - spec-kit-vs-bmad  │           │
│  │  - workflows.md      │    │  - spec-kit-vs-opnsp │           │
│  │  - artifacts.md      │    │  - bmad-vs-openspec  │           │
│  │  - roles.md          │    │                      │           │
│  │  - tooling.md        │    │                      │           │
│  └──────────────────────┘    └──────────────────────┘           │
│             │                          │                         │
│             └──────────┬───────────────┘                         │
│                        ▼                                         │
│               ┌──────────────┐                                   │
│               │   Validate   │                                   │
│               │    (03v)     │                                   │
│               └──────────────┘                                   │
└─────────────────────────────────────────────────────────────────┘
```

## Process

### Step 1: Verify Prerequisites

Check all three framework status files:

```yaml
# Required state for each framework
ready_for_cross_analysis: true
```

If any framework is not ready, report which ones need completion.

### Step 2: Check Status

Read the status files:

- `.assist/status/cross-analyses/by-theme.yaml`
- `.assist/status/cross-analyses/pairwise.yaml`

Identify what needs to be done.

### Step 3: Execute By-Theme Analysis

Run the by-theme comparison (03a):

- concepts.md
- workflows.md
- artifacts.md
- roles.md
- tooling.md

Update status after each file.

### Step 4: Execute Pairwise Analysis

Run the pairwise comparisons (03b):

- spec-kit-vs-bmad.md
- spec-kit-vs-openspec.md
- bmad-vs-openspec.md

Update status after each file.

### Step 5: Run Validation

Run the validation step (03v) to check completeness.

### Step 6: Report Results

Report final status.

## Resumability

This orchestrator supports resuming:

1. Check which files already exist and are complete
2. Skip completed comparisons
3. Resume from incomplete work

## Usage

```bash
/ca-all
```

## Output

Upon completion:

```markdown
# Cross-Comparisons Complete

## By-Theme Analysis

| Theme | Status |
|-------|--------|
| Concepts | ✓ |
| Workflows | ✓ |
| Artifacts | ✓ |
| Roles | ✓ |
| Tooling | ✓ |

## Pairwise Analysis

| Comparison | Status |
|------------|--------|
| spec-kit vs BMAD | ✓ |
| spec-kit vs OpenSpec | ✓ |
| BMAD vs OpenSpec | ✓ |

## Validation

- Status: Passed
- Errors: 0
- Warnings: 2

## Next Steps

Run synthesis:
- `/synth`
```
