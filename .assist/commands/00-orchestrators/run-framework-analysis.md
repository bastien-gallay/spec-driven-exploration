---
name: run-framework-analysis
description: Run complete framework analysis for one framework
arguments:
  - name: framework
    description: Framework name (spec-kit, bmad, openspec)
    required: true
outputs:
  - path: docs/framework-analyses/{framework}/
status_file: .assist/status/framework-analyses/{framework}.yaml
---

# Orchestrator: Run Framework Analysis

Execute the complete 4-step framework analysis workflow for a single framework.

## Overview

This orchestrator runs all framework analysis steps in sequence:

1. **02a-documents** - Extract key sources and take reading notes
2. **02b-glossaries** - Build glossary, taxonomy, and concept mapping
3. **02c-descriptions** - Document philosophy, workflow, features
4. **02d-summary** - Write executive summary and conclusions

## Prerequisites

- Framework reference cloned in `docs/references/{framework}/`

## Execution Flow

```text
┌─────────────────────────────────────────────────────────────────┐
│                    Framework Analysis                            │
│                                                                  │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐       │
│  │  Documents   │───▶│  Glossaries  │───▶│ Descriptions │       │
│  │   (02a)      │    │    (02b)     │    │    (02c)     │       │
│  └──────────────┘    └──────────────┘    └──────────────┘       │
│                                                 │                │
│                                                 ▼                │
│                                          ┌──────────────┐       │
│                                          │   Summary    │       │
│                                          │    (02d)     │       │
│                                          └──────────────┘       │
│                                                 │                │
│                                                 ▼                │
│                                          ┌──────────────┐       │
│                                          │   Validate   │       │
│                                          │    (02v)     │       │
│                                          └──────────────┘       │
└─────────────────────────────────────────────────────────────────┘
```

## Process

### Step 1: Check Status

Read the status file at `.assist/status/framework-analyses/{framework}.yaml`

- If `overall_completion: 100` and user hasn't requested regeneration, ask if they want to re-run
- Identify the first incomplete step to resume from

### Step 2: Execute Steps

For each step in order, check if already completed:

```yaml
# Step execution logic
for step in [documents, glossaries, descriptions, summary]:
  if step.status != "completed":
    execute step
    verify outputs exist
    update status
    if error:
      report and stop
```

### Step 3: Run Validation

After all steps complete, run the validation step:

```bash
# Equivalent to running /fa-validate {framework}
```

### Step 4: Report Results

Report final status including:

- Which steps were executed
- Final validation status
- Any warnings or issues

## Resumability

This orchestrator supports resuming from the last incomplete step:

1. Check status file for current progress
2. Skip completed steps
3. Resume from first incomplete step
4. Handle errors gracefully

## Status Updates

The orchestrator updates the status file after each step:

```yaml
# After documents step
stages:
  documents:
    key_sources:
      status: completed
      last_updated: {datetime}
    reading_notes:
      status: completed
      last_updated: {datetime}
```

## Error Handling

If a step fails:

1. Mark the step as `in-progress` (not completed)
2. Record the error in notes
3. Report the failure to user
4. Do not proceed to next step

## Usage

```bash
/fa-all spec-kit
/fa-all bmad
/fa-all openspec
```

## Expected Duration

Each step requires careful analysis. The full workflow typically involves:

- Documents: Exploring and reading source files
- Glossaries: Defining terms and relationships
- Descriptions: Writing detailed documentation
- Summary: Synthesizing findings
- Validation: Checking completeness

## Output

Upon completion:

```markdown
# Framework Analysis Complete: {framework}

## Steps Executed

| Step | Status | Notes |
|------|--------|-------|
| Documents | ✓ | key-sources, reading-notes |
| Glossaries | ✓ | 25 terms, 10 artifacts |
| Descriptions | ✓ | 4 files |
| Summary | ✓ | exec summary, conclusions |
| Validation | ✓ | Passed |

## Final Status

- Overall Completion: 100%
- Ready for Cross-Analysis: Yes

## Next Steps

Run cross-analysis when all frameworks complete:
- `/ca-all`
```
