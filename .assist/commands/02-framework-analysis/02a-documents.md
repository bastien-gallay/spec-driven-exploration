---
name: framework-analysis-documents
description: Extract key sources and take reading notes for a framework
arguments:
  - name: framework
    description: Framework name (spec-kit, bmad, openspec)
    required: true
outputs:
  - path: docs/framework-analyses/{framework}/documents/key-sources.md
  - path: docs/framework-analyses/{framework}/documents/reading-notes.md
status_file: .assist/status/framework-analyses/{framework}.yaml
---

# Framework Analysis: Documents

Extract and document key sources from the framework's reference materials.

## Prerequisites

- Framework reference cloned in `docs/references/{framework}/`
- No prior steps required (this is the first step)

## Context Loading

1. Read the status file at `.assist/status/framework-analyses/{framework}.yaml`
2. Check if `stages.documents.key_sources` and `stages.documents.reading_notes` are pending
3. If already completed, ask user if they want to regenerate

## Task: Key Sources

Identify and document the most important source files from the framework.

### Process

1. Explore `docs/references/{framework}/` directory structure
2. Identify files by category:
   - **Core documentation**: README, getting started, philosophy docs
   - **Workflow definitions**: Command/workflow documentation
   - **Templates**: Artifact templates
   - **Configuration**: Settings, schemas, config files
   - **Examples**: Sample projects or usage examples

### Output Format (key-sources.md)

```markdown
# Key Sources - {framework}

## Core Documentation

| File | Purpose | Priority |
|------|---------|----------|
| path/to/file.md | Brief description | High/Medium/Low |

## Workflow Definitions

...

## Templates

...

## Configuration

...

## Examples

...
```

## Task: Reading Notes

Create structured notes from reading the key sources.

### Process

1. Read each high-priority source file
2. Extract key concepts, terminology, and patterns
3. Note questions or unclear areas
4. Identify relationships between concepts

### Output Format (reading-notes.md)

```markdown
# Reading Notes - {framework}

## Summary

Brief overview of what was learned.

## Key Concepts

### {Concept Name}

- Definition/explanation
- Where defined: {source file}
- Related concepts: {list}

## Workflow Observations

- How the framework structures work
- Key patterns observed

## Terminology

Terms to define in the glossary:
- Term 1: initial understanding
- Term 2: initial understanding

## Questions/Unclear Areas

- Question 1
- Question 2

## Cross-References

Connections to other frameworks noticed during reading.
```

## Status Update

After completing both tasks, update the status file:

```yaml
stages:
  documents:
    key_sources:
      status: completed
      last_updated: {current_datetime}
    reading_notes:
      status: completed
      last_updated: {current_datetime}
```

## Quality Checklist

- [ ] All major source files identified
- [ ] Priority levels assigned based on importance
- [ ] Reading notes cover all high-priority sources
- [ ] Questions documented for later clarification
- [ ] Status file updated
