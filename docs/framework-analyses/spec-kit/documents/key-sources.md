# Key Sources - spec-kit

## Primary Documentation

| Document | Path | Description |
|----------|------|-------------|
| README | [README.md](../../references/spec-kit/README.md) | Main overview and introduction |
| Spec-Driven Philosophy | [spec-driven.md](../../references/spec-kit/spec-driven.md) | Core methodology |
| Quick Start | [docs/quickstart.md](../../references/spec-kit/docs/quickstart.md) | Getting started guide |

## Constitution

| Document | Path | Description |
|----------|------|-------------|
| Constitution Template | [memory/constitution.md](../../references/spec-kit/memory/constitution.md) | Project governing principles |

## Templates

| Template | Path | Purpose |
|----------|------|---------|
| Specification | [templates/spec-template.md](../../references/spec-kit/templates/spec-template.md) | Feature specification |
| Implementation Plan | [templates/plan-template.md](../../references/spec-kit/templates/plan-template.md) | Technical architecture |
| Tasks | [templates/tasks-template.md](../../references/spec-kit/templates/tasks-template.md) | Implementation checklist |

## Command Workflows

| Command | Path | Purpose |
|---------|------|---------|
| Constitution | [templates/commands/constitution.md](../../references/spec-kit/templates/commands/constitution.md) | Create principles |
| Specify | [templates/commands/specify.md](../../references/spec-kit/templates/commands/specify.md) | Create specification |
| Clarify | [templates/commands/clarify.md](../../references/spec-kit/templates/commands/clarify.md) | Resolve ambiguities |
| Plan | [templates/commands/plan.md](../../references/spec-kit/templates/commands/plan.md) | Generate plan |
| Analyze | [templates/commands/analyze.md](../../references/spec-kit/templates/commands/analyze.md) | Cross-artifact validation |
| Tasks | [templates/commands/tasks.md](../../references/spec-kit/templates/commands/tasks.md) | Generate task list |
| Implement | [templates/commands/implement.md](../../references/spec-kit/templates/commands/implement.md) | Execute implementation |
| Checklist | [templates/commands/checklist.md](../../references/spec-kit/templates/commands/checklist.md) | Validate completeness |

## Scripts

| Script | Path | Purpose |
|--------|------|---------|
| Prerequisites Check | [.specify/scripts/bash/check-prerequisites.sh](../../references/spec-kit/.specify/scripts/bash/check-prerequisites.sh) | Environment validation |
| Create Feature | [.specify/scripts/bash/create-new-feature.sh](../../references/spec-kit/.specify/scripts/bash/create-new-feature.sh) | Feature scaffolding |
| Setup Plan | [.specify/scripts/bash/setup-plan.sh](../../references/spec-kit/.specify/scripts/bash/setup-plan.sh) | Plan initialization |
| Update Agent Context | [.specify/scripts/bash/update-agent-context.sh](../../references/spec-kit/.specify/scripts/bash/update-agent-context.sh) | Context synchronization |

## Directory Structure Reference

```text
.specify/
├── memory/
│   └── constitution.md          # Project governing principles
├── scripts/
│   ├── bash/                    # Bash scripts
│   └── powershell/              # PowerShell scripts
├── specs/
│   └── [###-feature-name]/      # Feature specifications
│       ├── spec.md              # Feature specification
│       ├── plan.md              # Implementation plan
│       ├── research.md          # Technology research
│       ├── data-model.md        # Data entities
│       ├── quickstart.md        # Key validation scenarios
│       ├── contracts/           # API specifications
│       └── tasks.md             # Task checklist
└── templates/                   # Document templates
```
