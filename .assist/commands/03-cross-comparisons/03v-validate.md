---
name: cross-comparisons-validate
description: Validate completeness and consistency of cross-comparison analysis
arguments: []
outputs:
  - path: .assist/status/cross-analyses/by-theme.yaml (validation section)
  - path: .assist/status/cross-analyses/pairwise.yaml (validation section)
status_file: .assist/status/cross-analyses/
---

# Cross-Comparisons: Validate

Independently validate the cross-comparison analysis for completeness and consistency.

## Purpose

This validation step can be run at any time to check the current state of the
cross-comparison analysis. It does not auto-fix issues - it reports them for human review.

## Validation Checks

### 1. File Existence

Check that all expected files exist:

```text
docs/cross-analyses/
├── by-theme/
│   ├── concepts.md
│   ├── workflows.md
│   ├── artifacts.md
│   ├── roles.md
│   └── tooling.md
└── pairwise/
    ├── spec-kit-vs-bmad.md
    ├── spec-kit-vs-openspec.md
    └── bmad-vs-openspec.md
```

### 2. Content Validation

For each file, check:

| File | Required Sections | Min Words |
|------|-------------------|-----------|
| concepts.md | Overview, Matrix, Unique | 300 |
| workflows.md | Overview, Comparison, Diagrams | 300 |
| artifacts.md | Overview, Mapping, Lifecycle | 300 |
| roles.md | Overview, Comparison, Agent Models | 200 |
| tooling.md | Overview, Comparison, Commands | 200 |
| *-vs-*.md | Overview, Similarities, Differences, Conclusions | 400 |

### 3. Cross-Reference Validation

Check that:

- All three frameworks mentioned in each theme file
- Concept mappings reference valid terms from glossaries
- Comparison tables are complete (no empty cells)
- All pairwise comparisons cover the same aspects

### 4. Consistency Checks

Check that:

- Same facts stated consistently across files
- No contradictions between theme and pairwise analyses
- Terminology matches framework glossaries

### 5. Balance Check

Check that:

- Each framework gets equal coverage
- Comparisons don't favor one framework
- Both strengths and weaknesses noted

## Output Format

Report validation results in this format:

```markdown
# Validation Report - Cross-Comparisons

**Date**: {date}
**Overall Status**: PASSED | PASSED WITH WARNINGS | FAILED

## By-Theme Analysis

### File Existence

| File | Status |
|------|--------|
| by-theme/concepts.md | ✓ exists |
| ... | ... |

### Content Checks

| File | Sections | Words | Status |
|------|----------|-------|--------|
| concepts.md | 5/3 | 450 | ✓ |
| ... | ... | ... | ... |

## Pairwise Analysis

### File Existence

| File | Status |
|------|--------|
| pairwise/spec-kit-vs-bmad.md | ✓ exists |
| ... | ... |

### Content Checks

| File | Sections | Words | Status |
|------|----------|-------|--------|
| spec-kit-vs-bmad.md | 6/4 | 520 | ✓ |
| ... | ... | ... | ... |

## Cross-Reference Checks

| Check | Status | Issues |
|-------|--------|--------|
| Framework coverage | ✓ | - |
| Term references | ⚠ | 2 undefined terms |
| ... | ... | ... |

## Balance Assessment

| Framework | Mentions | Favorable | Unfavorable |
|-----------|----------|-----------|-------------|
| spec-kit | 45 | 12 | 8 |
| BMAD | 42 | 10 | 9 |
| OpenSpec | 40 | 11 | 7 |

## Issues Found

### Errors (must fix)

1. Error description

### Warnings (should fix)

1. Warning description

## Recommendations

1. Recommendation
```

## Status Update

Update the validation section of both status files:

```yaml
# by-theme.yaml
stages:
  validation:
    last_run: {current_datetime}
    status: passed  # or passed-with-warnings, failed
    errors: {count}
    warnings: {count}

# pairwise.yaml
stages:
  validation:
    last_run: {current_datetime}
    status: passed
    errors: {count}
    warnings: {count}
```

## Running Validation

This prompt can be invoked independently at any time:

```bash
/ca-validate
```

It does not require prior steps to be completed - it simply reports the current state.
