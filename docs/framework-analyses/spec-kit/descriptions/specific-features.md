# Specific Features - spec-kit

## Overview

spec-kit distinguishes itself through its constitutional governance model,
structured clarification process, and template-driven quality constraints.
This document covers features unique to spec-kit.

## Constitutional System

### 9 Articles of Governance

The constitution provides immutable architectural DNA:

#### Article I: Library-First Principle

Every feature must begin as a standalone library:

- Enforces modular design from start
- No direct application implementation without abstraction
- Enables composition and reuse

#### Article II: CLI Interface Mandate

All CLI interfaces must:

- Accept text input (stdin, arguments, files)
- Produce text output via stdout
- Support JSON format for structured data exchange
- Ensures observability and testability

#### Article III: Test-First Imperative (NON-NEGOTIABLE)

- Strict Test-Driven Development required
- Red-Green-Refactor cycle enforced
- Tests written BEFORE implementation
- Tests validated and approved by user

#### Articles VII & VIII: Simplicity & Anti-Abstraction

- Maximum 3 projects for initial implementation
- Additional projects require documented justification
- Use framework features directly, avoid wrapping
- Combat over-engineering through principled constraints

#### Article IX: Integration-First Testing

- Prefer real databases over mocks
- Use actual service instances over stubs
- Contract tests mandatory before implementation
- Ensures generated code works in practice

### Amendment Process

Section 4.2 defines amendment procedures:

- Explicit documentation of rationale required
- Review and approval by maintainers
- Backwards compatibility assessment
- Demonstrates constitution's own evolution

## Clarification Workflow

### Structured Ambiguity Detection

8 categories for systematic scanning:

1. User scenarios
2. Functional requirements
3. Data model
4. Integration points
5. Performance constraints
6. Security considerations
7. Error handling
8. Edge cases

### Constrained Questioning

| Constraint | Value |
|------------|-------|
| Questions per round | Max 5 |
| Questions per session | Max 10 |
| Answer format | Multiple-choice (2-5) or short-phrase (≤5 words) |
| Delivery | Sequential (one at a time) |

### Incremental Updates

After each answer:

1. Specification updated
2. Coverage reassessed
3. Next question determined
4. Progress tracked

## Quality Markers

### NEEDS CLARIFICATION System

`[NEEDS CLARIFICATION]` markers:

- Maximum 3 per specification
- Prevent assumption-making
- Force explicit resolution before planning
- Visible in specification document

### Specification Quality Checklist

Acts as "unit tests" for specification:

| Category | Validation |
|----------|------------|
| Requirement completeness | All requirements testable |
| Feature readiness | Sufficient detail for planning |
| Ambiguity check | No unresolved markers |
| Traceability | Requirements to user stories |

## Pre-Implementation Gates

### Constitution-Based Validation

Phase -1 in implementation plan:

| Gate | Article | Validation |
|------|---------|------------|
| Simplicity Gate | VII | ≤3 projects |
| Anti-Abstraction Gate | VIII | Direct framework usage |
| Integration-First Gate | IX | Real dependencies |

### Complexity Tracking

Justified violations documented:

```markdown
## Complexity Tracking

### Deviation: 4 Projects
**Rationale**: Separate API, Web, Mobile, Shared library required for...
**Approval**: [Date]
```

## Cross-Artifact Analysis

### Detection Passes

| Pass | Focus | Severity |
|------|-------|----------|
| A: Duplication | Repeated requirements/tasks | MEDIUM |
| B: Ambiguity | Vague adjectives, placeholders | HIGH |
| C: Underspecification | Missing outcomes | CRITICAL |
| D: Constitution Alignment | MUST violations | CRITICAL |
| E: Coverage Gaps | Orphaned requirements | HIGH |
| F: Inconsistency | Terminology drift | MEDIUM |

### Analysis Output

Structured markdown report with:

- Findings table by severity
- Coverage summary
- Unmapped tasks
- Constitution issues

## Multi-Agent Support

### Supported AI Agents (20+)

| Agent | Support Level |
|-------|--------------|
| Claude Code | Full |
| Cursor | Full |
| GitHub Copilot | Full |
| Windsurf | Full |
| Jules | Full |
| Amazon Q Developer | Partial |

### Agent Detection

```bash
specify init . --ai claude       # Specify agent
specify check                    # Verify agent tools
```

### Context Files

Agent-specific context files updated by `update-agent-context.sh`:

- Technology stack
- Project conventions
- Feature context

## Script Automation

### Cross-Platform Support

| Operation | Bash | PowerShell |
|-----------|------|------------|
| Prerequisites check | ✓ | ✓ |
| Feature creation | ✓ | ✓ |
| Plan setup | ✓ | ✓ |
| Agent context update | ✓ | ✓ |

### Feature Scaffolding

`create-new-feature.sh`:

1. Determines next feature number
2. Creates branch
3. Creates spec directory
4. Copies templates
5. Initializes specification

## Contract-First Development

### API Specification

Generated during planning phase:

```text
contracts/
├── api-spec.json           # OpenAPI specification
└── [service]-spec.md       # Service contracts
```

### Contract Tests

Mandatory before implementation (Article IX):

- Define expected behavior
- Validate integration points
- Prevent drift

## Task Organization

### Phase Structure

| Phase | Purpose | Dependencies |
|-------|---------|--------------|
| 1: Setup | Initialize project | None |
| 2: Foundational | Core infrastructure | Phase 1 |
| 3+: User Stories | Feature implementation | Phase 2 |
| Final: Polish | Cross-cutting concerns | All prior |

### Parallel Markers

`[P]` indicates parallelizable tasks:

```markdown
## Phase 3: User Stories
- [P] 3.1 Implement photo upload endpoint
- [P] 3.2 Implement gallery view component
- [ ] 3.3 Wire upload to gallery (depends on 3.1, 3.2)
```

### Story Tracking

`[Story]` links tasks to user stories:

```markdown
- [ ] [Story: US1] 3.1 Implement user login
- [ ] [Story: US1] 3.2 Add session management
- [ ] [Story: US2] 3.3 Implement photo upload
```

## Sources

- [README.md](../../references/spec-kit/README.md)
- [Spec-Driven Philosophy](../../references/spec-kit/spec-driven.md)
- [Constitution](../../references/spec-kit/memory/constitution.md)
- [Command Workflows](../../references/spec-kit/templates/commands/)
