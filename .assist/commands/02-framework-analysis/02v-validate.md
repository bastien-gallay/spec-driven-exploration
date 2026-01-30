---
name: framework-analysis-validate
description: Validate completeness and consistency of framework analysis
arguments:
  - name: framework
    description: Framework name (spec-kit, bmad, openspec)
    required: true
outputs:
  - path: .assist/status/framework-analyses/{framework}.yaml (validation section)
status_file: .assist/status/framework-analyses/{framework}.yaml
---

# Framework Analysis: Validate

Independently validate the framework analysis for completeness and consistency.

## Purpose

This validation step can be run at any time to check the current state of the
framework analysis. It does not auto-fix issues - it reports them for human review.

## Validation Checks

### 1. File Existence

Check that all expected files exist:

```text
docs/framework-analyses/{framework}/
├── documents/
│   ├── key-sources.md
│   └── reading-notes.md
├── glossaries/
│   ├── glossary.yaml
│   ├── artifact-taxonomy.yaml
│   └── concept-mapping.yaml
├── descriptions/
│   ├── philosophy.md
│   ├── workflow.md
│   ├── context-organization.md
│   └── specific-features.md
└── summary/
    ├── executive-summary.md
    └── conclusions.md
```

### 2. Content Validation

For each file, check:

- **Non-empty**: File has meaningful content (not just headers)
- **Structure**: Required sections present
- **Minimum length**: Content meets minimum thresholds

| File | Min Sections | Min Words |
|------|--------------|-----------|
| key-sources.md | 3 categories | 100 |
| reading-notes.md | 4 sections | 200 |
| glossary.yaml | 10 terms | N/A |
| artifact-taxonomy.yaml | 5 artifacts | N/A |
| concept-mapping.yaml | 5 mappings | N/A |
| philosophy.md | 3 sections | 150 |
| workflow.md | 2 stages | 200 |
| context-organization.md | 3 sections | 100 |
| specific-features.md | 2 features | 150 |
| executive-summary.md | 4 sections | 100 |
| conclusions.md | 3 findings | 150 |

### 3. YAML Schema Validation

For YAML files, validate against schemas:

- `glossary.yaml` → `.assist/schemas/glossary.schema.yaml`
- `artifact-taxonomy.yaml` → `.assist/schemas/artifact-taxonomy.schema.yaml`
- `concept-mapping.yaml` → `.assist/schemas/concept-mapping.schema.yaml`

**Validation Script**: Use the provided validation script for automated checks:

```bash
# Validate a single framework
uv run .assist/scripts/validate_yaml.py --framework {framework}

# Validate all frameworks
uv run .assist/scripts/validate_yaml.py --all

# Validate a specific file
uv run .assist/scripts/validate_yaml.py <yaml_file> <schema_file>
```

The script checks:

- YAML syntax validity
- Schema version and metadata presence
- Minimum content requirements (terms, artifacts, mappings)
- JSON Schema validation (if jsonschema is installed)

### 4. Cross-Reference Validation

Check that references are consistent:

- Terms in glossary are used in descriptions
- Artifacts in taxonomy appear in workflow
- Cross-framework mappings reference valid frameworks
- Source links are valid (files exist)

### 5. Terminology Consistency

Check that key terms are used consistently:

- Same term not defined differently in different files
- Framework name spelled consistently
- Artifact names match between taxonomy and descriptions

## Output Format

Report validation results in this format:

```markdown
# Validation Report - {framework}

**Date**: {date}
**Overall Status**: PASSED | PASSED WITH WARNINGS | FAILED

## File Existence

| File | Status |
|------|--------|
| documents/key-sources.md | ✓ exists |
| ... | ... |

## Content Checks

| File | Sections | Words | Status |
|------|----------|-------|--------|
| key-sources.md | 5/3 | 250 | ✓ |
| ... | ... | ... | ... |

## Schema Validation

| File | Valid | Errors |
|------|-------|--------|
| glossary.yaml | ✓ | - |
| ... | ... | ... |

## Cross-References

| Check | Status | Issues |
|-------|--------|--------|
| Glossary usage | ✓ | - |
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
/fa-validate {framework}
```

It does not require prior steps to be completed - it simply reports the current state.
