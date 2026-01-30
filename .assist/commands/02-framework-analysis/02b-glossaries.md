---
name: framework-analysis-glossaries
description: Build glossary, taxonomy, and concept mapping for a framework
arguments:
  - name: framework
    description: Framework name (spec-kit, bmad, openspec)
    required: true
outputs:
  - path: docs/framework-analyses/{framework}/glossaries/glossary.yaml
  - path: docs/framework-analyses/{framework}/glossaries/artifact-taxonomy.yaml
  - path: docs/framework-analyses/{framework}/glossaries/concept-mapping.yaml
status_file: .assist/status/framework-analyses/{framework}.yaml
---

# Framework Analysis: Glossaries

Build structured data files defining the framework's vocabulary and relationships.

## Prerequisites

- Documents step completed (`stages.documents.key_sources: completed`)
- Read the reading notes for context

## Context Loading

1. Read `.assist/status/framework-analyses/{framework}.yaml`
2. Verify documents stage is completed
3. Read `docs/framework-analyses/{framework}/documents/reading-notes.md`
4. Load schema definitions from `.assist/schemas/`

## Task 1: Glossary

Create a structured glossary of all framework terminology.

### Process

1. Extract terms from reading notes
2. Research each term in source documentation
3. Categorize and define each term
4. Identify relationships between terms

### Output Format (glossary.yaml)

```yaml
# yaml-language-server: $schema=../../../.assist/schemas/glossary.schema.yaml
schema_version: "1.0"
metadata:
  framework: {framework}
  last_updated: {date}
  source_commit: {commit_hash}

terms:
  - id: term-id
    term: Display Term Name
    category: core_concept  # or workflow_term, artifact_term, etc.
    definition: |
      1-3 sentence definition of the term.
    aliases:
      - Alternative Name
    related_terms:
      - other-term-id
    source_refs:
      - path/to/source.md
```

### Categories

- `core_concept`: Fundamental framework concepts
- `workflow_term`: Process/workflow related terms
- `artifact_term`: Document/file type terms
- `technical_term`: Implementation details
- `role_term`: Agents, personas, actors
- `quality_term`: Quality, validation terms
- `directory_term`: File/folder structure terms

## Task 2: Artifact Taxonomy

Document all artifacts the framework produces.

### Output Format (artifact-taxonomy.yaml)

```yaml
# yaml-language-server: $schema=../../../.assist/schemas/artifact-taxonomy.schema.yaml
schema_version: "1.0"
metadata:
  framework: {framework}
  last_updated: {date}

artifacts:
  - id: artifact-id
    name: Artifact Name
    file_pattern: "path/pattern/{variable}/file.ext"
    description: What this artifact represents
    classifications:
      purpose: specification  # governance, specification, design, execution, validation
      lifecycle: once_per_feature  # once_per_project, once_per_feature, per_session, continuous
      creator: command-name or role
      format: markdown  # markdown, yaml, json, code, mixed
    sections:
      - name: Section Name
        required: true
        purpose: What this section contains
    dependencies:
      requires:
        - prerequisite-artifact-id
      produces:
        - downstream-artifact-id
```

## Task 3: Concept Mapping

Map relationships and cross-framework equivalences.

### Output Format (concept-mapping.yaml)

```yaml
# yaml-language-server: $schema=../../../.assist/schemas/concept-mapping.schema.yaml
schema_version: "1.0"
metadata:
  framework: {framework}
  last_updated: {date}

relationships:
  - source: term-or-artifact-id
    target: other-id
    type: produces  # precedes, produces, validates, contains, references, requires, enables
    notes: Optional explanation

cross_framework_mappings:
  - local_term: local-term-id
    mappings:
      - framework: other-framework
        term: equivalent-term
        match_level: partial  # exact, partial, low, none
        notes: Explanation of differences

unique_concepts:
  - id: unique-concept-id
    name: Unique Concept Name
    description: What this concept represents
    why_unique: Why no other framework has this
```

## Status Update

After completing all three files, update the status:

```yaml
stages:
  glossaries:
    glossary:
      status: completed
      last_updated: {current_datetime}
      item_count: {number_of_terms}
    artifact_taxonomy:
      status: completed
      last_updated: {current_datetime}
      item_count: {number_of_artifacts}
    concept_mapping:
      status: completed
      last_updated: {current_datetime}
      item_count: {number_of_mappings}
```

## Quality Checklist

- [ ] All terms from reading notes defined
- [ ] Each term has a clear, concise definition
- [ ] Categories correctly assigned
- [ ] All artifacts documented with file patterns
- [ ] Dependency graph is accurate
- [ ] Cross-framework mappings attempted
- [ ] Unique concepts identified
- [ ] YAML validates against schemas
- [ ] Status file updated
