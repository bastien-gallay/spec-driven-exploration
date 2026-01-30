# Specific Features - BMAD

## Overview

BMAD distinguishes itself through its multi-agent architecture, extensive
workflow library, and unique collaboration mechanisms. This document covers
features that set BMAD apart from other SDD frameworks.

## Agent System

### 21 Specialized Agents

BMAD includes a complete team of AI agents with distinct personas:

#### Core Domain Agents

| Agent | Role | Key Specialty |
|-------|------|---------------|
| John (PM) | Product Manager | PRD creation, requirements |
| Winston | Architect | System design, ADRs |
| Amelia | Developer | Story implementation |
| Bob | Scrum Master | Sprint management |
| Mary | Business Analyst | Research, product brief |
| Sally | UX Designer | User experience |
| Paige | Technical Writer | Documentation |
| Quinn | QA Engineer | Test automation |

#### Special Purpose Agents

| Agent | Role | Key Specialty |
|-------|------|---------------|
| Barry | Quick Flow Dev | Minimum ceremony |
| BMad Master | Orchestrator | Party Mode, help |

### Agent Definition Structure

```yaml
# Example: pm.agent.yaml
identity:
  name: "John"
  role: "Product Manager"

persona:
  communication_style: "Asks 'WHY?' relentlessly"
  principles:
    - User-centered design
    - Jobs-to-be-Done framework
    - Iterate over perfection

workflows:
  - id: CP
    name: Create PRD
  - id: VP
    name: Validate PRD

critical_actions:
  - "Always start with user needs"
  - "Challenge assumptions"
```

## Party Mode

### Multi-Agent Collaboration

Party Mode enables multiple agents in one conversation, orchestrated by
BMad Master.

**How it works**:

1. Run `party-mode` command
2. BMad Master picks relevant agents per message
3. Agents respond in character
4. Agents agree, disagree, build on each other
5. Continue until resolution

**Use cases**:

- Big decisions with tradeoffs
- Brainstorming sessions
- Post-mortems
- Sprint retrospectives
- Architecture reviews

### Agent Interaction Patterns

| Pattern | Description |
|---------|-------------|
| Agreement | Agents align on approach |
| Disagreement | Agents present alternatives |
| Building | Agents extend each other's ideas |
| Challenge | Agents question assumptions |

## Module Ecosystem

### Available Modules

| Module | Code | Purpose |
|--------|------|---------|
| BMad Method | BMM | Core framework (34+ workflows) |
| BMad Builder | BMB | Custom agents/workflows/modules |
| Test Architect | TEA | Enterprise testing (8 workflows) |
| Game Dev Studio | BMGD | Unity, Unreal, Godot |
| Creative Intelligence | CIS | Innovation, design thinking |

### Module Installation

```bash
npx bmad-method install          # Core module
npx bmad-method install --tea    # Add Test Architect
```

## Adversarial Review

### Forced Problem-Finding

Unlike traditional reviews, BMAD's adversarial review requires finding issues:

**Rules**:

- Reviewer MUST find issues
- "Looks good" is not acceptable
- Problems are assumed to exist
- Human filters false positives

**Benefits**:

- Prevents confirmation bias
- Forces genuine analysis
- Catches real issues
- Improves artifact quality

### Application

| Workflow | Adversarial Element |
|----------|---------------------|
| Code Review | Implementation quality |
| PRD Validation | Requirements completeness |
| Implementation Readiness | Architecture alignment |

## Brainstorming Workflow

### 60+ Ideation Techniques

Structured facilitation with technique categories:

- Divergent thinking
- Convergent thinking
- Analogical reasoning
- Constraint manipulation
- Perspective shifting

### Workflow Structure

1. **Setup**: Define topic, goals, constraints
2. **Approach Selection**: Pick techniques, get recommendations
3. **Facilitation**: Work through with probing questions
4. **Organization**: Group ideas into themes
5. **Action**: Next steps for top ideas

### Key Principle

AI acts as coach/guide, not content generator. Every idea comes from the user.

## Step-File Architecture

### Unique Implementation

Unlike linear prompts, BMAD uses micro-files for each step:

```text
src/bmm/workflows/2-plan-workflows/create-prd/
├── workflow.md           # Entry point
├── steps/
│   ├── step-1-setup.md
│   ├── step-2-problem.md
│   ├── step-3-users.md
│   └── ...
└── templates/
    └── prd-template.md
```

### Advantages

| Advantage | Benefit |
|-----------|---------|
| Context isolation | Each step has focused context |
| State preservation | Frontmatter tracks progress |
| Reproducibility | Same steps produce same structure |
| Maintenance | Steps can be updated independently |

## Tri-Modal Workflows

### Three Operation Modes

Key workflows support Create, Validate, and Edit modes:

| Mode | Flag | Purpose |
|------|------|---------|
| Create | `-c` | New artifact from scratch |
| Validate | `-v` | Check against standards |
| Edit | `-e` | Improve existing artifact |

### Supported Workflows

- Create PRD
- Create Architecture
- Create UX Design

## Customization System

### Without Code Changes

Customization through YAML files in `_bmad/_config/agents/`:

```yaml
# Custom agent behavior
identity:
  name: "Custom Name"
persona:
  communication_style: "Team preference"
critical_actions:
  - "Team-specific action"
menu:
  - label: "Team Standard"
    action: "Custom prompt"
```

### Preservation Through Updates

```bash
npx bmad-method install
```

Updates framework while preserving customizations.

## Quality Mechanisms

### Implementation Readiness Check

Gate before Phase 4 with three outcomes:

| Outcome | Meaning |
|---------|---------|
| PASS | Ready for implementation |
| CONCERNS | Issues to address |
| FAIL | Significant problems |

### Code Review Facets

Multi-dimensional quality validation:

- Functional correctness
- Code quality
- Test coverage
- Architecture alignment
- Performance considerations

## Sources

- [README.md](../../references/BMAD/BMAD-METHOD/README.md)
- [Party Mode](../../references/BMAD/BMAD-METHOD/docs/explanation/party-mode.md)
- [Adversarial Review](../../references/BMAD/BMAD-METHOD/docs/explanation/adversarial-review.md)
- [Brainstorming](../../references/BMAD/BMAD-METHOD/docs/explanation/brainstorming.md)
- [Customize BMAD](../../references/BMAD/BMAD-METHOD/docs/how-to/customize-bmad.md)
