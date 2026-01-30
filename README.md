# Spec-Driven Development Exploration

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A comparative study of three Spec-Driven Development (SDD) frameworks for
AI-assisted software engineering.

## What's Inside

```text
docs/
├── references/          # Cloned framework repositories (read-only)
├── framework-analyses/  # Individual framework analyses
├── cross-analyses/      # Cross-framework comparisons
└── adr/                 # Architecture Decision Records
```

## Frameworks Analyzed

| Framework | Description | Repository |
|-----------|-------------|------------|
| **spec-kit** | Lightweight SDD toolkit | [github.com/spec-kit/spec-kit](https://github.com/spec-kit/spec-kit) |
| **BMAD** | Business-Model-Aligned Development | [github.com/bmadcode/BMAD-METHOD](https://github.com/bmadcode/BMAD-METHOD) |
| **OpenSpec** | Open specification framework | [github.com/openspec-dev/OpenSpec](https://github.com/openspec-dev/OpenSpec) |

## Getting Started

### Prerequisites

- [just](https://github.com/casey/just) — command runner
- [git](https://git-scm.com/) — version control

### Clone and Setup

```bash
git clone https://github.com/bastiengallay/spec-driven-exploration.git
cd spec-driven-exploration

# Clone all reference repositories
just clone-refs
```

### Updating

To update the reference repositories:

```bash
just pull-refs
```

## AI-Assisted Workflows

This project includes AI-assisted analysis workflows in the `.assist/`
directory. These provide structured prompts and skill definitions for
conducting framework analyses with AI assistants.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute.

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE)
file for details.
