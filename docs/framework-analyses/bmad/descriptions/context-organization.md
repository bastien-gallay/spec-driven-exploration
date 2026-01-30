# Context Organization - BMAD

## Overview

BMAD organizes specification documentation through a module-based system with
configurable output locations, progressive context building, and workflow-
specific context loading.

## Directory Structure

### Installation Layout

```text
_bmad/
├── agents/                    # Agent definitions
│   ├── pm.agent.yaml
│   ├── architect.agent.yaml
│   ├── dev.agent.yaml
│   └── ...
├── workflows/                 # Workflow definitions
│   ├── 1-analysis-workflows/
│   ├── 2-plan-workflows/
│   ├── 3-solution-workflows/
│   ├── 4-impl-workflows/
│   └── quick-flow/
├── tasks/                     # Task definitions
├── checklists/                # Quality checklists
└── _config/
    └── agents/                # Customization files
        ├── core-bmad-master.customize.yaml
        ├── bmm-dev.customize.yaml
        └── ...

_bmad-output/                  # Generated artifacts
├── planning/                  # Phase 1-3 artifacts
├── implementation/            # Phase 4 artifacts
└── knowledge/                 # Long-term knowledge
```

### Module Configuration Variables

From `module.yaml`:

| Variable | Purpose |
|----------|---------|
| `user_name` | User's name for document attribution |
| `communication_language` | Output language preference |
| `document_output_language` | Documentation language |
| `output_folder` | Base output directory |
| `project_name` | Project identifier |
| `user_skill_level` | Explanation depth adjustment |
| `planning_artifacts` | Phase 1-3 output location |
| `implementation_artifacts` | Phase 4 output location |
| `project_knowledge` | Long-term knowledge storage |

## Artifact Organization

### By Phase

| Phase | Location | Artifacts |
|-------|----------|-----------|
| Analysis | `{{planning_artifacts}}/` | Product brief, research |
| Planning | `{{planning_artifacts}}/` | PRD, UX spec |
| Solutioning | `{{planning_artifacts}}/` | Architecture, epics |
| Implementation | `{{implementation_artifacts}}/` | Stories, sprint status |

### By Type

```text
{{planning_artifacts}}/
├── product-brief.md           # Strategic vision
├── PRD.md                     # Requirements
├── ux-spec.md                 # UX design
├── architecture.md            # Technical decisions
└── epics/
    ├── epic-auth.md
    └── epic-payments.md

{{implementation_artifacts}}/
├── sprint-status.yaml         # Sprint tracking
├── stories/
│   ├── story-login-flow.md
│   └── story-user-profile.md
└── project-context.md         # Brownfield rules

{{project_knowledge}}/
├── research/
│   └── market-analysis.md
└── docs/
    └── api-reference.md
```

## Context Loading Strategy

### Progressive Building

Each document becomes context for the next phase:

```text
Product Brief
     │
     ▼
   PRD ───────────► tells Architect constraints
     │
     ▼
Architecture ─────► tells Developer patterns
     │
     ▼
Story Files ──────► focused implementation context
```

### Per-Workflow Loading

| Workflow | Loads |
|----------|-------|
| `create-prd` | Product Brief |
| `create-architecture` | PRD, UX Spec |
| `create-story` | Epics, PRD, Architecture, UX |
| `dev-story` | Story file only |
| `code-review` | Architecture, Story file |
| `quick-spec` | Planning docs (if exist) |
| `quick-dev` | Tech-spec |

### Context Isolation

Fresh chats recommended for each workflow to:

- Avoid context window limitations
- Prevent cross-contamination
- Ensure focused execution

## Brownfield Support

### Project Context Document

For existing codebases, `project-context.md` captures:

- Existing patterns and conventions
- Technology constraints
- Rules for all implementation workflows

### When to Create/Update

| Timing | Action |
|--------|--------|
| Before Phase 4 | Initial creation |
| Significant changes | Update document |
| New patterns discovered | Extend rules |

### Context in PRD/Architecture

During creation:

- Agent scans existing project docs
- Identifies existing patterns
- Ensures compatibility with current codebase

## Customization System

### Agent Customization Files

Located in `_bmad/_config/agents/`:

```yaml
# bmm-dev.customize.yaml
identity:
  name: "Alex"  # Custom name
persona:
  communication_style: "Detailed explanations"
critical_actions:
  - "Run linter before commits"
menu:
  - label: "Project Standards"
    action: "Load project-standards.md"
```

### Customizable Elements

| Element | What Can Change |
|---------|-----------------|
| Identity | Agent name, self-introduction |
| Persona | Role, communication style |
| Critical Actions | Startup behaviors |
| Menu Items | Custom prompts, skills |
| Memory | Project-specific context |

### Rebuild Process

```bash
npx bmad-method install
```

Updates agents/workflows while preserving customizations.

## Template Organization

### Workflow Templates

```text
src/bmm/workflows/[phase]/[workflow]/
├── workflow.md              # Main workflow definition
├── steps/                   # Step files
│   ├── step-1.md
│   ├── step-2.md
│   └── ...
└── templates/               # Output templates
    └── output-template.md
```

### Template Variables

Templates use Handlebars-style variables:

```markdown
# Product Requirements Document - {{project_name}}
**Author:** {{user_name}}
**Date:** {{date}}
```

## Sources

- [Module Config](../../references/BMAD/BMAD-METHOD/src/bmm/module.yaml)
- [Customize BMAD](../../references/BMAD/BMAD-METHOD/docs/how-to/customize-bmad.md)
- [Brownfield Guide](../../references/BMAD/BMAD-METHOD/docs/how-to/brownfield/index.md)
- [Workflow Map](../../references/BMAD/BMAD-METHOD/docs/reference/workflow-map.md)
