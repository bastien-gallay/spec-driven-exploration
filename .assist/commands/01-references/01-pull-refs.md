---
name: pull-refs
description: Update cloned framework reference repositories
arguments: []
outputs:
  - path: docs/references/{framework}/
status_file: null
---

# Pull References

Update the cloned framework repositories to get the latest changes.

## Task

1. Navigate to `docs/references/`
2. For each framework directory (spec-kit, bmad, openspec):
   - Check if it's a git repository
   - If yes, run `git pull` to update
   - If no, report that it needs to be cloned manually

## Commands

```bash
cd docs/references/spec-kit && git pull
cd docs/references/bmad && git pull
cd docs/references/openspec && git pull
```

## Expected Output

Report which repositories were updated and their current commit hash.

## Notes

- This step has no status tracking as it's a simple refresh operation
- Run this before starting any analysis to ensure you have the latest sources
