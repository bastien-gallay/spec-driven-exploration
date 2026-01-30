# Key Sources - BMAD

## Primary Documentation

| Document | Path | Description |
|----------|------|-------------|
| README | [README.md](../../references/BMAD/BMAD-METHOD/README.md) | Main overview and introduction |
| Getting Started | [docs/tutorials/getting-started.md](../../references/BMAD/BMAD-METHOD/docs/tutorials/getting-started.md) | Installation and first steps |
| Workflow Map | [docs/reference/workflow-map.md](../../references/BMAD/BMAD-METHOD/docs/reference/workflow-map.md) | Complete workflow reference |

## Agent Definitions

| Agent | Path | Role |
|-------|------|------|
| John (PM) | [src/bmm/agents/pm.agent.yaml](../../references/BMAD/BMAD-METHOD/src/bmm/agents/pm.agent.yaml) | Product Manager - PRD creation |
| Winston (Architect) | [src/bmm/agents/architect.agent.yaml](../../references/BMAD/BMAD-METHOD/src/bmm/agents/architect.agent.yaml) | System architecture |
| Amelia (Dev) | [src/bmm/agents/dev.agent.yaml](../../references/BMAD/BMAD-METHOD/src/bmm/agents/dev.agent.yaml) | Developer - story implementation |
| Bob (SM) | [src/bmm/agents/sm.agent.yaml](../../references/BMAD/BMAD-METHOD/src/bmm/agents/sm.agent.yaml) | Scrum Master |
| Mary (Analyst) | [src/bmm/agents/analyst.agent.yaml](../../references/BMAD/BMAD-METHOD/src/bmm/agents/analyst.agent.yaml) | Business Analyst |
| Sally (UX) | [src/bmm/agents/ux-designer.agent.yaml](../../references/BMAD/BMAD-METHOD/src/bmm/agents/ux-designer.agent.yaml) | UX Designer |
| Barry (Quick Flow) | [src/bmm/agents/quick-flow-solo-dev.agent.yaml](../../references/BMAD/BMAD-METHOD/src/bmm/agents/quick-flow-solo-dev.agent.yaml) | Quick Flow Specialist |
| BMad Master | [src/core/agents/bmad-master.agent.yaml](../../references/BMAD/BMAD-METHOD/src/core/agents/bmad-master.agent.yaml) | Master Orchestrator |

## Workflow Definitions

| Workflow | Path | Phase |
|----------|------|-------|
| Create PRD | [src/bmm/workflows/2-plan-workflows/create-prd/](../../references/BMAD/BMAD-METHOD/src/bmm/workflows/2-plan-workflows/create-prd/) | Planning |
| Create Architecture | [src/bmm/workflows/3-solution-workflows/create-architecture/](../../references/BMAD/BMAD-METHOD/src/bmm/workflows/3-solution-workflows/create-architecture/) | Solutioning |
| Dev Story | [src/bmm/workflows/4-impl-workflows/dev-story/](../../references/BMAD/BMAD-METHOD/src/bmm/workflows/4-impl-workflows/dev-story/) | Implementation |
| Quick Spec | [src/bmm/workflows/quick-flow/quick-spec/](../../references/BMAD/BMAD-METHOD/src/bmm/workflows/quick-flow/quick-spec/) | Quick Flow |

## Explanatory Content

| Topic | Path | Focus |
|-------|------|-------|
| Party Mode | [docs/explanation/party-mode.md](../../references/BMAD/BMAD-METHOD/docs/explanation/party-mode.md) | Multi-agent collaboration |
| Adversarial Review | [docs/explanation/adversarial-review.md](../../references/BMAD/BMAD-METHOD/docs/explanation/adversarial-review.md) | Forced problem-finding |
| Why Solutioning | [docs/explanation/why-solutioning-matters.md](../../references/BMAD/BMAD-METHOD/docs/explanation/why-solutioning-matters.md) | Conflict prevention |
| Preventing Conflicts | [docs/explanation/preventing-agent-conflicts.md](../../references/BMAD/BMAD-METHOD/docs/explanation/preventing-agent-conflicts.md) | Architecture ADRs |
| Quick Flow | [docs/explanation/quick-flow.md](../../references/BMAD/BMAD-METHOD/docs/explanation/quick-flow.md) | Minimum ceremony |
| Brainstorming | [docs/explanation/brainstorming.md](../../references/BMAD/BMAD-METHOD/docs/explanation/brainstorming.md) | Ideation techniques |

## Configuration

| File | Path | Purpose |
|------|------|---------|
| Module Config | [src/bmm/module.yaml](../../references/BMAD/BMAD-METHOD/src/bmm/module.yaml) | Cross-workflow variables |
| Customization | [docs/how-to/customize-bmad.md](../../references/BMAD/BMAD-METHOD/docs/how-to/customize-bmad.md) | Agent and workflow customization |
| Brownfield | [docs/how-to/brownfield/index.md](../../references/BMAD/BMAD-METHOD/docs/how-to/brownfield/index.md) | Existing project support |

## Templates

| Template | Path | Purpose |
|----------|------|---------|
| PRD Template | [src/bmm/workflows/2-plan-workflows/create-prd/templates/prd-template.md](../../references/BMAD/BMAD-METHOD/src/bmm/workflows/2-plan-workflows/create-prd/templates/prd-template.md) | Product requirements |
| Story Template | [src/bmm/workflows/4-impl-workflows/create-story/templates/story-template.md](../../references/BMAD/BMAD-METHOD/src/bmm/workflows/4-impl-workflows/create-story/templates/story-template.md) | User stories |
