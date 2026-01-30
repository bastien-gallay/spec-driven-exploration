# Glossary - BMAD

## Core Concepts

### Agent

A specialized AI persona with defined role, identity, communication style, and
workflows. BMAD includes 21 agents such as PM, Architect, Developer, UX
Designer, and Scrum Master.

### BMad Master

The core orchestrator agent responsible for managing Party Mode, providing
`/bmad-help` guidance, and coordinating multi-agent interactions.

### BMad Method (BMM)

The core BMAD module containing 34+ workflows across the four development
phases. The primary framework for AI-assisted software development.

### Party Mode

Multi-agent collaboration mode where multiple specialized agents participate in
a single conversation, orchestrated by BMad Master. Used for big decisions,
brainstorming, and retrospectives.

## Workflow Terms

### Phase

One of four sequential stages in the BMAD development lifecycle:

1. **Analysis** (Optional): Brainstorming, research, product brief
2. **Planning**: PRD creation, UX design
3. **Solutioning**: Architecture, epics, stories, readiness check
4. **Implementation**: Sprint planning, story development, code review

### Quick Flow

Minimum ceremony track for simple changes (bug fixes, small features). Uses
`quick-spec` and `quick-dev` workflows, bypassing full planning.

### Step-File Architecture

Workflow design pattern where each step is a self-contained micro-file. Steps
are loaded just-in-time, executed sequentially, and never pre-loaded.

### Tri-Modal Workflow

Workflow supporting three operation modes: Create, Validate, and Edit. Used for
key workflows like PRD creation.

## Artifact Terms

### ADR (Architecture Decision Record)

Document capturing a technical decision, its context, considered alternatives,
and rationale. Created during the Solutioning phase.

### Epic

High-level feature grouping containing related user stories. Created from
PRD requirements.

### PRD (Product Requirements Document)

Comprehensive document defining functional and non-functional requirements,
personas, metrics, and risks. Primary output of the Planning phase.

### Project Context

Document (`project-context.md`) describing existing codebase rules and patterns.
Required for brownfield development.

### Sprint Status

YAML file (`sprint-status.yaml`) tracking epics and stories across sprints.
Initialized during Sprint Planning.

### Story

Individual implementable unit of work with tasks, subtasks, and acceptance
criteria. Format: `story-[slug].md`.

## Technical Terms

### Adversarial Review

Review technique where the reviewer MUST find issues. Prevents confirmation bias
by assuming problems exist and forcing genuine analysis.

### Context Loading

Process of loading relevant documents before workflow execution. Different
workflows load different context (PRD, architecture, stories, etc.).

### Frontmatter

YAML metadata at the start of documents tracking workflow progress
(`stepsCompleted`), input documents, and workflow type.

### Solutioning

Phase 3 of BMAD focused on preventing agent conflicts through Architecture
Decision Records before implementation begins.

## Agent Names

| Name | Role | Specialty |
|------|------|-----------|
| John | Product Manager | PRD creation, requirements |
| Winston | Architect | System design, ADRs |
| Amelia | Developer | Story implementation |
| Bob | Scrum Master | Sprint management |
| Mary | Business Analyst | Research, product brief |
| Sally | UX Designer | User experience |
| Paige | Technical Writer | Documentation |
| Quinn | QA Engineer | Test automation |
| Barry | Quick Flow Dev | Minimum ceremony |

## Sources

- [README.md](../../references/BMAD/BMAD-METHOD/README.md)
- [Getting Started](../../references/BMAD/BMAD-METHOD/docs/tutorials/getting-started.md)
- [Workflow Map](../../references/BMAD/BMAD-METHOD/docs/reference/workflow-map.md)
