# Contributing

Thank you for your interest in contributing to this project.

## How to Contribute

### Reporting Issues

- Use GitHub Issues to report bugs or suggest improvements
- Provide clear reproduction steps for bugs
- For feature requests, explain the use case

### Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Make your changes
4. Run linting checks (see below)
5. Commit with a descriptive message
6. Push and open a Pull Request

## Code Style

### Markdown

This project uses [markdownlint](https://github.com/DavidAnson/markdownlint)
for consistent Markdown formatting.

```bash
# Lint all markdown files
npx markdownlint-cli2 "**/*.md" "#docs/references/**"

# Lint specific files
npx markdownlint-cli2 README.md CONTRIBUTING.md
```

### Commit Messages

- Use clear, descriptive commit messages
- Start with a verb in imperative mood (e.g., "Add", "Fix", "Update")
- Keep the first line under 72 characters

Examples:

```text
Add cross-analysis for workflow comparison
Fix broken link in framework-analyses README
Update glossary format to YAML
```

## Project Structure

- `docs/references/` — Cloned framework repositories (read-only, not tracked)
- `docs/framework-analyses/` — Individual framework analysis documents
- `docs/cross-analyses/` — Cross-framework comparison documents
- `docs/adr/` — Architecture Decision Records
- `.assist/` — AI-assisted workflow definitions

## Running Workflows

Use `just` to run common tasks:

```bash
# Pull latest changes from reference repositories
just pull-refs
```

## Questions

If you have questions, open an issue or start a discussion.
