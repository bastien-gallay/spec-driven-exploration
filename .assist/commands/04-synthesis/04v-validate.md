---
name: synthesis-validate
description: Validate completeness and consistency of synthesis
arguments: []
outputs:
  - path: .assist/status/cross-analyses/synthesis.yaml (validation section)
status_file: .assist/status/cross-analyses/synthesis.yaml
---

# Synthesis: Validate

Independently validate the synthesis for completeness and consistency.

## Purpose

This validation step can be run at any time to check the current state of the
synthesis. It does not auto-fix issues - it reports them for human review.

## Validation Checks

### 1. File Existence

Check that all expected files exist:

```text
docs/cross-analyses/summary/
├── synthesis.md
└── recommendations.md
```

### 2. Content Validation

For each file, check:

| File | Required Sections | Min Words |
|------|-------------------|-----------|
| synthesis.md | Overview, Themes, Insights, Landscape | 500 |
| recommendations.md | Selection Guide, Best Practices, Anti-Patterns | 400 |

### 3. Traceability

Check that:

- Synthesis references specific findings from cross-analyses
- Recommendations are grounded in analysis
- Claims can be traced back to framework analyses

### 4. Completeness

Check that:

- All three frameworks represented in synthesis
- Decision tree covers common scenarios
- Recommendations cover different user types

### 5. Actionability

Check that:

- Recommendations are specific enough to act on
- Decision tree leads to clear choices
- Getting started paths are practical

## Output Format

Report validation results in this format:

```markdown
# Validation Report - Synthesis

**Date**: {date}
**Overall Status**: PASSED | PASSED WITH WARNINGS | FAILED

## File Existence

| File | Status |
|------|--------|
| summary/synthesis.md | ✓ exists |
| summary/recommendations.md | ✓ exists |

## Content Checks

| File | Sections | Words | Status |
|------|----------|-------|--------|
| synthesis.md | 6/4 | 650 | ✓ |
| recommendations.md | 5/3 | 480 | ✓ |

## Traceability

| Claim | Source | Status |
|-------|--------|--------|
| "spec-kit enforces TDD" | spec-kit/philosophy.md | ✓ |
| ... | ... | ... |

## Completeness

| Coverage Area | Status |
|---------------|--------|
| All frameworks in synthesis | ✓ |
| Decision tree scenarios | ⚠ missing large team |
| User type recommendations | ✓ |

## Actionability

| Recommendation | Actionable? | Notes |
|----------------|-------------|-------|
| "Use spec-kit for TDD" | ✓ | Clear action |
| ... | ... | ... |

## Issues Found

### Errors (must fix)

1. Error description

### Warnings (should fix)

1. Warning description

## Recommendations

1. Recommendation
```

## Status Update

Update the validation section of the status file:

```yaml
stages:
  validation:
    last_run: {current_datetime}
    status: passed  # or passed-with-warnings, failed
    errors: {count}
    warnings: {count}
```

## Running Validation

This prompt can be invoked independently at any time:

```bash
/synth-validate
```

It does not require prior steps to be completed - it simply reports the current state.
