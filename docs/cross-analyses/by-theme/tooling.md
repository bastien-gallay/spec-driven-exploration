# Cross-Analysis: Tooling

## Overview

This analysis compares how spec-kit, BMAD, and OpenSpec integrate with
development tools, IDEs, and configuration systems. Each framework has
distinct tooling philosophies and integration patterns.

## Tooling Comparison

| Aspect | spec-kit | BMAD | OpenSpec |
|--------|----------|------|----------|
| Primary IDE | VS Code | Cursor/VS Code | Cursor |
| Command Interface | Slash commands | Slash commands | Slash commands (OPSX) |
| Config Format | Markdown | Markdown + YAML | YAML |
| Templates | Markdown files | Markdown files | Markdown files |
| Package Manager | npm | npm | npm |
| Runtime | Node.js | Node.js | Node.js |

## Command Comparison

### Command Invocation

| Framework | Command Prefix | Example |
|-----------|---------------|---------|
| spec-kit | `/speckit.` | `/speckit.specify` |
| BMAD | `/` (direct) | `/create-prd` |
| OpenSpec | `/opsx:` | `/opsx:continue` |

### Command Counts

| Framework | Total Commands | Categories |
|-----------|----------------|------------|
| spec-kit | ~8 | Lifecycle (specify, plan, implement, etc.) |
| BMAD | ~20+ | Phase-organized (analysis, planning, etc.) |
| OpenSpec | ~10 | Action-based (new, continue, apply, etc.) |

### Command Parameters

| Framework | Parameter Style | Example |
|-----------|-----------------|---------|
| spec-kit | Natural language after command | `/speckit.specify Build a photo organizer` |
| BMAD | Flags (-c, -v, -e) | `/create-prd -c` |
| OpenSpec | Change name (optional) | `/opsx:apply feature-name` |

## Configuration

### spec-kit Configuration

**Location**: `.specify/` directory

```text
.specify/
├── memory/
│   └── constitution.md      # Governance document
├── templates/               # Document templates
│   ├── spec-template.md
│   ├── plan-template.md
│   └── tasks-template.md
└── scripts/                 # Setup scripts
```

**Configuration Style**: Markdown-based, embedded in templates and constitution

**Customization Points**:

- Constitution articles (governance principles)
- Template sections
- Setup scripts for project initialization

### BMAD Configuration

**Location**: BMAD-METHOD package + project artifacts

```text
BMAD-METHOD/
├── src/
│   ├── core/
│   │   └── agents/          # Agent definitions
│   └── bmm/
│       ├── agents/          # BMM agents
│       └── workflows/       # Step-file workflows
└── templates/               # Document templates

Project/
├── {{planning_artifacts}}/
│   └── project-context.md   # Brownfield context
└── {{implementation_artifacts}}/
```

**Configuration Style**: YAML frontmatter + Markdown content

**Customization Points**:

- Agent YAML files (identity, workflows, style)
- Workflow step files
- Configurable artifact paths (`{{planning_artifacts}}`)
- Project context for brownfield

### OpenSpec Configuration

**Location**: `openspec/` directory

```yaml
# openspec/config.yaml
schema: spec-driven           # Which workflow schema

context:                      # Injected into instructions
  tech_stack: TypeScript, React
  conventions: |
    - Use functional components
    - Prefer hooks over HOCs

rules:                        # Per-artifact constraints
  proposal:
    max_length: 500
  tasks:
    max_tasks_per_phase: 10
```

**Configuration Style**: YAML with schema-based validation

**Customization Points**:

- Schema selection (workflow definition)
- Context injection (tech stack, conventions)
- Per-artifact rules and constraints
- Multi-level resolution (package → user → project)

## Template Systems

### Template Format Comparison

| Framework | Template Format | Interpolation |
|-----------|-----------------|---------------|
| spec-kit | Markdown with sections | None (copied as-is) |
| BMAD | Markdown with `{{vars}}` | Mustache-style |
| OpenSpec | Markdown with instructions | Context injection |

### Template Sections

#### spec-kit Templates

```markdown
# Feature Specification: {{feature-name}}

## User Scenarios
<!-- Priority-ordered scenarios with acceptance criteria -->

## Functional Requirements
<!-- Numbered, testable requirements -->

## Key Entities
<!-- Data model overview -->

## Success Criteria
<!-- Measurable outcomes -->

## Edge Cases
<!-- Boundary conditions -->
```

#### BMAD Templates

```markdown
---
stepsCompleted: []
inputDocuments: []
workflowType: 'prd'
---

# Product Requirements Document - {{project_name}}

**Author:** {{user_name}}
**Date:** {{date}}

## Problem Statement
## Target Users
## Functional Requirements
...
```

#### OpenSpec Templates

```markdown
# Proposal: {change-name}

<!--
Instructions: Fill in each section. Context will be injected below.
-->

<context>
{injected from config.yaml}
</context>

## Why

## Scope

### In Scope

### Out of Scope

## Approach
```

## Extensibility

### spec-kit Extensibility

**Extension Mechanism**: Script-based

- Setup scripts in `.specify/scripts/`
- Custom templates in `.specify/templates/`
- Constitution articles for custom principles

**Limitations**:

- No plugin system
- No agent customization (single agent model)
- Template changes apply globally

### BMAD Extensibility

**Extension Mechanism**: File-based agents and workflows

- Add new agents via YAML files
- Create custom workflows via step files
- Extend existing workflows with new steps

```yaml
# Custom agent example
identity:
  name: "Custom Expert"
  role: "Domain Specialist"

communication:
  style: "Formal"
  tone: "Expert"

workflows:
  - custom-workflow
```

**Limitations**:

- Step-file architecture requires specific format
- Agent must fit persona model
- Workflow integration with phases

### OpenSpec Extensibility

**Extension Mechanism**: Schema-based

- Custom schemas define entirely new workflows
- Multi-level resolution for customization
- Schema inherits from package defaults

```yaml
# Custom schema example
name: my-workflow
extends: spec-driven

artifacts:
  - id: custom-artifact
    generates: custom.md
    requires: [proposal]
    template: templates/custom.md
```

**Extensibility Features**:

- Multi-level resolution: Package → User → Project
- Schema inheritance
- Per-artifact customization
- Custom templates

## IDE Integration

### VS Code / Cursor Integration

| Framework | Integration Method | Features |
|-----------|-------------------|----------|
| spec-kit | Rules files | Command suggestions, templates |
| BMAD | .cursorrules, .cursorindexingignore | Agent selection, workflow guidance |
| OpenSpec | Cursor rules | OPSX command help |

### Common Patterns

All three frameworks rely on:

1. **Slash commands** in chat interface
2. **Rules files** for context
3. **File watching** for artifact updates
4. **Markdown preview** for documents

## Dependency Management

### Runtime Dependencies

| Framework | Core Dependencies |
|-----------|------------------|
| spec-kit | Node.js |
| BMAD | Node.js |
| OpenSpec | Node.js, TypeScript |

### Package Installation

| Framework | Install Method |
|-----------|---------------|
| spec-kit | `npx spec-kit init` |
| BMAD | Clone or npm package |
| OpenSpec | `npx openspec init` |

## Error Handling

### Validation Tools

| Framework | Validation Approach |
|-----------|---------------------|
| spec-kit | `/speckit.analyze` (consistency check) |
| BMAD | Readiness check workflow |
| OpenSpec | `/opsx:verify` (3-dimensional) |

### Error Reporting

| Framework | Error Format |
|-----------|--------------|
| spec-kit | Severity levels (CRITICAL/HIGH/MEDIUM/LOW) |
| BMAD | PASS/CONCERNS/FAIL outcomes |
| OpenSpec | Completeness/Correctness/Coherence dimensions |

## Unique Tooling Features

### spec-kit: Quality Checklist

Built-in validation checklist for specifications:

- Requirement completeness
- Feature readiness
- Quality markers

### BMAD: Step-File Architecture

Unique workflow execution model:

- Micro-files for each step
- Just-in-time loading
- Progress tracking in frontmatter
- Reproducible execution

### OpenSpec: Artifact Graph

Algorithmic artifact management:

- DAG-based dependencies
- Topological sort (Kahn's algorithm)
- Deterministic creation order
- Schema-defined relationships

## Conclusions

### Tooling Philosophy Differences

1. **Simplicity vs Features**:
   - spec-kit: Minimal tooling, markdown-centric
   - BMAD: Rich agent ecosystem, extensive workflows
   - OpenSpec: Schema-driven, configurable

2. **Configuration Approach**:
   - spec-kit: Convention over configuration
   - BMAD: File-based customization
   - OpenSpec: YAML configuration with inheritance

3. **Extension Model**:
   - spec-kit: Limited (scripts, templates)
   - BMAD: Agent/workflow files
   - OpenSpec: Schema inheritance

### Recommendations

- **Choose spec-kit tooling** when: Simplicity valued, minimal setup needed,
  markdown-first workflow
- **Choose BMAD tooling** when: Rich IDE integration needed, agent customization
  valued, step-by-step reproducibility important
- **Choose OpenSpec tooling** when: Configuration flexibility needed, custom
  workflows required, schema-based validation preferred

## Sources

- [spec-kit README](../../references/spec-kit/README.md)
- [BMAD Getting Started](../../references/BMAD/BMAD-METHOD/docs/tutorials/getting-started.md)
- [OpenSpec Concepts](../../references/OpenSpec/docs/concepts.md)
