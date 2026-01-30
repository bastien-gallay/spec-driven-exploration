# Analysis Process Commands

## Vision

This system provides a **reusable prompt infrastructure** for systematic
framework analysis. Instead of ad-hoc exploration, it enforces a structured
workflow that produces consistent, comparable documentation across different
spec-driven development frameworks.

### Why This Exists

When analyzing multiple SDD (Spec-Driven Development) frameworks, we need:

- **Consistency** — Same structure for each framework's documentation
- **Comparability** — Standardized glossaries and taxonomies enable
  cross-framework analysis
- **Resumability** — Status tracking allows interrupted work to continue
- **Reproducibility** — Documented prompts can be re-run or adapted

### What Problem It Solves

Manual framework analysis leads to:

- Inconsistent documentation depth across frameworks
- Missing cross-references between concepts
- No way to track progress or resume work
- Difficulty comparing frameworks with different terminology

This system standardizes the process through structured prompts, schemas, and
status tracking.

## Architecture

### Directory Structure

```text
.assist/
├── commands/                    # Structured analysis prompts
│   ├── 00-orchestrators/        # Multi-step workflow coordinators
│   ├── 01-references/           # Source repo management
│   ├── 02-framework-analysis/   # Per-framework analysis steps
│   ├── 03-cross-comparisons/    # Multi-framework comparisons
│   └── 04-synthesis/            # Final conclusions
│
├── schemas/                     # YAML validation schemas
│   ├── glossary.schema.yaml
│   ├── artifact-taxonomy.schema.yaml
│   ├── concept-mapping.schema.yaml
│   └── status.schema.yaml
│
└── status/                      # Progress tracking
    ├── framework-analyses/      # Per-framework status
    │   ├── spec-kit.yaml
    │   ├── bmad.yaml
    │   └── openspec.yaml
    └── cross-analyses/          # Cross-analysis status
        ├── by-theme.yaml
        ├── pairwise.yaml
        └── synthesis.yaml

.claude/commands/                # User-invocable slash commands
    ├── fa-*.md                  # Framework analysis commands
    ├── ca-*.md                  # Cross-analysis commands
    └── synth*.md                # Synthesis commands
```

### Prompt Naming Convention

| Prefix  | Stage              | Purpose                        |
| ------- | ------------------ | ------------------------------ |
| `01-`   | References         | Source repo management         |
| `02a-d` | Framework Analysis | Per-framework steps (sequence) |
| `02v`   | Framework Analysis | Validation                     |
| `03a-b` | Cross-Comparisons  | Comparison types               |
| `03v`   | Cross-Comparisons  | Validation                     |
| `04a`   | Synthesis          | Final synthesis                |
| `04v`   | Synthesis          | Validation                     |

## The 4-Stage Workflow

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  STAGE 1: REFERENCES                                                        │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │  Pull/update source repositories for each framework                   │  │
│  │  • spec-kit  • bmad  • openspec                                       │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                      │                                      │
│                                      ▼                                      │
│  STAGE 2: FRAMEWORK ANALYSIS (can run in parallel)                          │
│  ┌───────────────┐  ┌───────────────┐  ┌───────────────┐                   │
│  │   spec-kit    │  │     BMAD      │  │   OpenSpec    │                   │
│  │  ┌─────────┐  │  │  ┌─────────┐  │  │  ┌─────────┐  │                   │
│  │  │Documents│  │  │  │Documents│  │  │  │Documents│  │                   │
│  │  │Glossary │  │  │  │Glossary │  │  │  │Glossary │  │                   │
│  │  │Descript.│  │  │  │Descript.│  │  │  │Descript.│  │                   │
│  │  │Summary  │  │  │  │Summary  │  │  │  │Summary  │  │                   │
│  │  └─────────┘  │  │  └─────────┘  │  │  └─────────┘  │                   │
│  └───────────────┘  └───────────────┘  └───────────────┘                   │
│           │                 │                 │                             │
│           └─────────────────┼─────────────────┘                             │
│                             ▼                                               │
│  STAGE 3: CROSS-COMPARISONS                                                 │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │  By-Theme Analysis          │  Pairwise Comparisons                   │  │
│  │  • Concepts                 │  • spec-kit ↔ BMAD                      │  │
│  │  • Workflows                │  • spec-kit ↔ OpenSpec                  │  │
│  │  • Artifacts                │  • BMAD ↔ OpenSpec                      │  │
│  │  • Roles                    │                                         │  │
│  │  • Tooling                  │                                         │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                      │                                      │
│                                      ▼                                      │
│  STAGE 4: SYNTHESIS                                                         │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │  Cross-cutting conclusions + Recommendations                          │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Stage 1: References

Pull or update source repositories containing each framework's documentation.

- **Input:** Git repository URLs
- **Output:** `docs/references/{framework}/`
- **Command:** Manual git operations

### Stage 2: Framework Analysis

Analyze each framework independently through 4 sequential steps:

| Step         | Prompt                 | Output                               |
| ------------ | ---------------------- | ------------------------------------ |
| Documents    | `02a-documents.md`     | `key-sources.md`, `reading-notes.md` |
| Glossaries   | `02b-glossaries.md`    | YAML glossary files (3 files)        |
| Descriptions | `02c-descriptions.md`  | `overview.md`, `workflow.md`, etc.   |
| Summary      | `02d-summary.md`       | `README.md`                          |

Validation: `02v-validate.md` checks completeness and schema compliance.

### Stage 3: Cross-Comparisons

Compare all frameworks once individual analyses complete:

| Analysis Type | Prompt             | Output                              |
| ------------- | ------------------ | ----------------------------------- |
| By-Theme      | `03a-by-theme.md`  | 5 theme files (concepts, workflows) |
| Pairwise      | `03b-pairwise.md`  | 3 comparison files                  |

Validation: `03v-validate.md` checks cross-references and consistency.

### Stage 4: Synthesis

Produce final conclusions and recommendations:

| Task      | Prompt             | Output                   |
| --------- | ------------------ | ------------------------ |
| Synthesis | `04a-synthesis.md` | Final synthesis document |

Validation: `04v-validate.md` checks completeness.

## Command Reference

### Framework Analysis Commands

| Command                       | Description                          |
| ----------------------------- | ------------------------------------ |
| `/fa-all {framework}`         | Run complete framework analysis      |
| `/fa-documents {framework}`   | Extract key sources and reading notes|
| `/fa-glossaries {framework}`  | Build glossary and taxonomy files    |
| `/fa-descriptions {framework}`| Write overview, workflow docs        |
| `/fa-summary {framework}`     | Generate framework README summary    |
| `/fa-validate {framework}`    | Validate analysis completeness       |

**Framework options:** `spec-kit`, `bmad`, `openspec`

### Cross-Analysis Commands

| Command        | Description                           |
| -------------- | ------------------------------------- |
| `/ca-all`      | Run all cross-comparisons             |
| `/ca-by-theme` | Compare frameworks by theme (5 themes)|
| `/ca-pairwise` | Compare frameworks in pairs (3 pairs) |
| `/ca-validate` | Validate cross-analysis completeness  |

### Synthesis Commands

| Command           | Description                    |
| ----------------- | ------------------------------ |
| `/synth`          | Generate final synthesis       |
| `/synth-validate` | Validate synthesis completeness|

### Orchestrator Commands

| Command    | Description                       |
| ---------- | --------------------------------- |
| `/run-all` | Run the complete 4-stage pipeline |

## Quick Start

### 1. Verify References

Ensure framework source repos exist:

```bash
ls docs/references/
# Should show: spec-kit/ bmad/ openspec/
```

### 2. Run Framework Analysis

Analyze each framework (can run in parallel):

```text
/fa-all spec-kit
/fa-all bmad
/fa-all openspec
```

Or run individual steps:

```text
/fa-documents spec-kit
/fa-glossaries spec-kit
/fa-descriptions spec-kit
/fa-summary spec-kit
/fa-validate spec-kit
```

### 3. Run Cross-Comparisons

After all framework analyses complete:

```text
/ca-all
```

Or individually:

```text
/ca-by-theme
/ca-pairwise
/ca-validate
```

### 4. Generate Synthesis

After cross-comparisons complete:

```text
/synth
/synth-validate
```

### 5. Run Full Pipeline

Or run everything in sequence:

```text
/run-all
```

### Checking Progress

View status files to see progress:

```bash
cat .assist/status/framework-analyses/spec-kit.yaml
cat .assist/status/cross-analyses/by-theme.yaml
```

Status values: `pending` → `in-progress` → `completed`

## Status Tracking

### Status File Structure

Each analysis stage has a status file tracking:

- **Stage completion** — Which steps are done
- **Last updated** — Timestamp of last change
- **Validation status** — Pass/fail/warnings
- **Overall completion** — Percentage complete

### Status Values

| Value         | Meaning                    |
| ------------- | -------------------------- |
| `pending`     | Not started                |
| `in-progress` | Currently being worked on  |
| `completed`   | Finished and validated     |
| `skipped`     | Intentionally skipped      |

### Validation Status

| Value                   | Meaning                 |
| ----------------------- | ----------------------- |
| `not-started`           | Validation never run    |
| `passed`                | All checks passed       |
| `passed-with-warnings`  | Passed with minor issues|
| `failed`                | Critical issues found   |

## Schemas

YAML schemas in `.assist/schemas/` define the structure of:

| Schema                          | Purpose                          |
| ------------------------------- | -------------------------------- |
| `glossary.schema.yaml`          | Term definitions and categories  |
| `artifact-taxonomy.schema.yaml` | Document/file type classification|
| `concept-mapping.schema.yaml`   | Cross-framework equivalences     |
| `status.schema.yaml`            | Progress tracking structure      |

## Next Steps

### Remaining Setup Tasks

1. **Convert remaining glossaries to YAML**
   - [ ] BMAD glossaries (`docs/framework-analyses/bmad/glossaries/`)
   - [ ] OpenSpec glossaries (`docs/framework-analyses/openspec/glossaries/`)

2. **Test prompts manually**
   - [ ] Run `/fa-all` on one framework end-to-end
   - [ ] Verify status tracking updates correctly
   - [ ] Check output matches expected structure

3. **Validate schemas**
   - [ ] Test YAML files against schemas
   - [ ] Fix any validation errors

### Future Improvements

- Add CI validation of YAML schemas
- Create visualization of cross-framework mappings
- Add support for additional frameworks
- Export comparison data to structured formats
