# Reference Repositories

Read-only cloned repositories for AI exploration, referencing and partial reuse.

## Configuration

The list of repositories to clone is maintained in `repositories.txt`.
Format: `URL PATH`

## Structure

- **spec-kit** — [github/spec-kit](https://github.com/github/spec-kit)
- **BMAD** — BMAD method and modules (4 repos)
- **OpenSpec** — [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec)

## Installing References

Run the following command from the project root:

```bash
just clone-refs
```

## Updating

To update all reference repositories:

```bash
just pull-refs
```
