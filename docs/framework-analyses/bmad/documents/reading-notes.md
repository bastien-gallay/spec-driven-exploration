# Reading Notes - BMAD

## Metadata

| Field | Value |
|-------|-------|
| Framework | BMAD-METHOD |
| Version Analyzed | Commit `5fe54de` (2025-01-30) |
| Analysis Date | 2025-01-30 |
| Repository | `docs/references/BMAD/BMAD-METHOD/` |

## First Impressions

- Comprehensive framework with 21 specialized agents and 50+ workflows
- Clear four-phase development lifecycle (Analysis → Planning → Solutioning →
  Implementation)
- Strong emphasis on AI as collaborator, not decision-maker
- Scale-adaptive: from bug fixes (Quick Flow) to enterprise systems

## Key Observations

### Architecture

- **Modular agent system**: Each agent has distinct persona, capabilities, and
  workflows
- **Step-file architecture**: Micro-file design with sequential enforcement
- **Progressive context building**: Each phase produces documents for next
  phase
- **Tri-modal workflows**: Create/Validate/Edit modes for key workflows

### Philosophy

- "AI as collaborator, not decision maker" - positions AI to guide structured
  processes
- Structure enables AI effectiveness through clear context
- Grounded in agile best practices
- Adversarial review technique forces genuine analysis

### Workflow Design

- Fresh chats recommended for each workflow to avoid context limitations
- Just-in-time loading of step files (never pre-load future steps)
- State tracking via frontmatter in output files
- Append-only document building

### Unique Elements

- **Party Mode**: Multi-agent collaboration in single conversation
- **Solutioning Phase**: Prevents agent conflicts through ADRs
- **Quick Flow**: Minimum ceremony track for simple changes
- **Brownfield Support**: `project-context.md` for existing codebases

## Questions for Further Investigation

1. How does agent customization affect workflow behavior?
2. What is the practical overhead of maintaining 21 agents?
3. How are conflicts resolved when agents disagree in Party Mode?

## Notes During Analysis

- Agent definitions use YAML with structured persona sections
- Workflows reference tasks, templates, and checklists
- Module configuration provides cross-workflow variables
- Strong documentation with tutorials, explanations, and how-to guides
