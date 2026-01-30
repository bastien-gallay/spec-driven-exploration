---
name: run-full-pipeline
description: Run the complete analysis pipeline end-to-end
arguments: []
outputs:
  - path: docs/framework-analyses/
  - path: docs/cross-analyses/
status_file: .assist/status/
---

# Orchestrator: Run Full Pipeline

Execute the complete spec-driven development analysis pipeline.

## Overview

This orchestrator runs the entire 4-stage workflow:

1. **Stage 1: References** - Pull latest source repos
2. **Stage 2: Framework Analysis** - Analyze each framework
3. **Stage 3: Cross-Comparisons** - Compare frameworks
4. **Stage 4: Synthesis** - Write conclusions

## Execution Flow

```text
┌─────────────────────────────────────────────────────────────────┐
│                      Full Pipeline                               │
│                                                                  │
│  Stage 1: References                                             │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  Pull repos: spec-kit, bmad, openspec                    │   │
│  └──────────────────────────────────────────────────────────┘   │
│                            │                                     │
│                            ▼                                     │
│  Stage 2: Framework Analysis (parallel possible)                 │
│  ┌────────────────┐ ┌────────────────┐ ┌────────────────┐       │
│  │   spec-kit     │ │     BMAD       │ │   OpenSpec     │       │
│  │   Analysis     │ │   Analysis     │ │   Analysis     │       │
│  └────────────────┘ └────────────────┘ └────────────────┘       │
│           │                │                   │                 │
│           └────────────────┼───────────────────┘                 │
│                            ▼                                     │
│  Stage 3: Cross-Comparisons                                      │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  By-Theme + Pairwise comparisons                         │   │
│  └──────────────────────────────────────────────────────────┘   │
│                            │                                     │
│                            ▼                                     │
│  Stage 4: Synthesis                                              │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  Cross-cutting conclusions + Recommendations              │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

## Process

### Step 1: Pull References

Run the pull-refs command to update source repositories.

### Step 2: Framework Analyses

For each framework, run the complete analysis:

```yaml
frameworks:
  - spec-kit
  - bmad
  - openspec

for each framework:
  run: /fa-all {framework}
  verify: ready_for_cross_analysis: true
```

Note: Framework analyses can be run in parallel if desired.

### Step 3: Cross-Comparisons

After all frameworks complete, run cross-comparisons:

```yaml
run: /ca-all
verify:
  - by-theme.yaml: overall_completion: 100
  - pairwise.yaml: overall_completion: 100
```

### Step 4: Synthesis

After cross-comparisons complete, run synthesis:

```yaml
run: /synth
verify: synthesis.yaml: overall_completion: 100
```

### Step 5: Final Validation

Run all validation steps:

```yaml
run:
  - /fa-validate spec-kit
  - /fa-validate bmad
  - /fa-validate openspec
  - /ca-validate
  - /synth-validate
```

### Step 6: Report Results

Generate final pipeline report.

## Resumability

This orchestrator supports resuming from any point:

1. Check all status files
2. Identify first incomplete stage
3. Resume from that point
4. Skip completed work

## Status Tracking

The orchestrator tracks overall pipeline status:

```yaml
pipeline_status:
  stage_1_references: completed
  stage_2_framework_analyses:
    spec-kit: completed
    bmad: completed
    openspec: in-progress
  stage_3_cross_comparisons: pending
  stage_4_synthesis: pending
```

## Usage

```bash
/run-all
```

## Expected Duration

The full pipeline involves significant analysis work across all stages.

## Output

Upon completion:

```markdown
# Full Pipeline Complete

## Pipeline Summary

| Stage | Status |
|-------|--------|
| 1. References | ✓ Updated |
| 2. Framework Analysis | ✓ 3/3 complete |
| 3. Cross-Comparisons | ✓ Complete |
| 4. Synthesis | ✓ Complete |

## Framework Analysis Results

| Framework | Completion | Validation |
|-----------|------------|------------|
| spec-kit | 100% | Passed |
| BMAD | 100% | Passed |
| OpenSpec | 100% | Passed |

## Cross-Analysis Results

| Analysis | Completion | Validation |
|----------|------------|------------|
| By-Theme | 100% | Passed |
| Pairwise | 100% | Passed |
| Synthesis | 100% | Passed |

## Final Deliverables

- Framework analyses: `docs/framework-analyses/`
- Cross-analyses: `docs/cross-analyses/`
- Synthesis: `docs/cross-analyses/summary/`

## Validation Summary

- Total Errors: 0
- Total Warnings: 3
- Overall Status: PASSED
```
