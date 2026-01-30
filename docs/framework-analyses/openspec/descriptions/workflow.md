# Workflow and Prompts - OpenSpec

## Overview

OpenSpec uses OPSX, an action-based workflow architecture. Unlike phase-based
approaches, OPSX provides commands that can be used when their dependencies
are satisfied.

## OPSX Commands

### Exploration

#### `/opsx:explore`

**Purpose**: Think through ideas, investigate problems.

**Output**: None (conversation only)

**When to use**:

- Unclear requirements
- Performance optimization
- Debugging investigation
- Approach consideration

### Creation Commands

#### `/opsx:new`

**Purpose**: Start a new change folder.

**Output**: `changes/[change-name]/` with `.openspec.yaml`

**Creates**:

```text
changes/add-dark-mode/
└── .openspec.yaml          # Change metadata
```

#### `/opsx:continue`

**Purpose**: Create next artifact step-by-step.

**Flow**:

1. Check completed artifacts
2. Identify available (unblocked) artifacts
3. Create next artifact
4. Update completion state

**Respects dependency graph**:

```text
proposal ─────┬───────► specs
              │
              └───────► design
                            │
specs ────────┴───────► tasks
```

#### `/opsx:ff` (Fast-Forward)

**Purpose**: Create all planning artifacts at once.

**Output**: All artifacts created in dependency order

**When to use**:

- Clear requirements
- Simple changes
- Experienced teams

### Implementation

#### `/opsx:apply`

**Purpose**: Implement tasks, checking off as complete.

**Flow**:

1. Load `tasks.md`
2. Find next uncompleted task
3. Implement task
4. Mark task complete
5. Continue until done

**Progress tracking**: Checkbox format in `tasks.md`

```markdown
- [x] 1.1 Create module structure
- [x] 1.2 Add dependencies
- [ ] 2.1 Implement main function  ← Current
- [ ] 2.2 Add utilities
```

#### `/opsx:apply <change-name>`

**Purpose**: Switch to different change for implementation.

**Use case**: Parallel work on multiple changes

### Validation

#### `/opsx:verify`

**Purpose**: Validate implementation matches artifacts.

**Three dimensions**:

| Dimension | Validation |
|-----------|------------|
| Completeness | All tasks done? All requirements implemented? |
| Correctness | Implementation matches spec intent? |
| Coherence | Design decisions reflected in code? |

**Output**: Verification report

### Completion

#### `/opsx:sync`

**Purpose**: Merge delta specs to main specs.

**Flow**:

1. Read delta specs from change
2. Apply ADDED sections
3. Apply MODIFIED sections
4. Apply REMOVED sections
5. Update main specs

**When to use**: Before or during archive

#### `/opsx:archive`

**Purpose**: Complete change and move to archive.

**Flow**:

1. Verify change is complete
2. Prompt for spec sync if needed
3. Move to `archive/[date]-[change-name]/`
4. Preserve all artifacts

#### `/opsx:bulk-archive`

**Purpose**: Archive multiple changes at once.

**Handles**: Spec conflicts between changes

## Workflow Patterns

### Quick Feature

Best for small to medium features with straightforward requirements:

```text
/opsx:new → /opsx:ff → /opsx:apply → /opsx:verify → /opsx:archive
```

### Exploratory

Best for unclear requirements or investigation work:

```text
/opsx:explore → /opsx:new → /opsx:continue → /opsx:apply
```

### Parallel Changes

Best for multiple work streams:

```text
# Start multiple changes
/opsx:new feature-a
/opsx:new feature-b

# Work on feature-a
/opsx:apply feature-a

# Switch to feature-b
/opsx:apply feature-b

# Complete as each finishes
/opsx:archive feature-a
/opsx:archive feature-b
```

### Iterative Refinement

Best for evolving requirements:

```text
/opsx:new → /opsx:continue (proposal)
          → /opsx:continue (specs)
          → /opsx:apply (partial)
          → /opsx:continue (update specs)  # Iterate
          → /opsx:apply (complete)
          → /opsx:verify
          → /opsx:archive
```

## Artifact Flow

### Default Schema (spec-driven)

```text
proposal ──► specs ──► design ──► tasks ──► (apply)
    │           │         │          │
   why        what       how      steps
 + scope    changes    approach   to take
```

### Dependency Rules

From `schema.yaml`:

```yaml
artifacts:
  - id: proposal
    generates: proposal.md
    requires: []

  - id: specs
    generates: specs/**/*.md
    requires: [proposal]

  - id: design
    generates: design.md
    requires: [proposal]

  - id: tasks
    generates: tasks.md
    requires: [specs, design]

apply:
  requires: [tasks]
  tracks: tasks.md
```

## Task Structure

### Phase Organization

```markdown
## 1. Setup
- [ ] 1.1 Create module structure
- [ ] 1.2 Add dependencies

## 2. Core Implementation
- [ ] 2.1 Implement main function
- [ ] 2.2 Add utilities

## 3. Integration
- [ ] 3.1 Wire components
- [ ] 3.2 Add error handling
```

### Task Characteristics

- Small (completable in one session)
- Ordered by dependency
- Checkbox format for parsing
- Numbered for reference

## Sources

- [OPSX Reference](../../references/OpenSpec/docs/opsx.md)
- [Workflows](../../references/OpenSpec/docs/workflows.md)
- [Schema Definition](../../references/OpenSpec/schemas/spec-driven/schema.yaml)
