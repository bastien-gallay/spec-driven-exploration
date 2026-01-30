# Assist Scripts

Utility scripts for validating and processing analysis files.

## Available Scripts

### validate_yaml.py

Validates YAML files against JSON Schema-style schemas defined in
`.assist/schemas/`.

#### Requirements

- Python 3.10+
- PyYAML (required)
- jsonschema (optional, for full schema validation)

Dependencies are automatically installed via uv's inline script metadata.

#### Usage

```bash
# Validate all glossary files for a framework
uv run .assist/scripts/validate_yaml.py --framework openspec

# Validate all status files
uv run .assist/scripts/validate_yaml.py --status

# Validate everything (frameworks + status)
uv run .assist/scripts/validate_yaml.py --all

# Validate a specific file against a schema
uv run .assist/scripts/validate_yaml.py \
    docs/framework-analyses/openspec/glossaries/glossary.yaml \
    .assist/schemas/glossary.schema.yaml
```

#### Output

The script exits with:

- `0` if all validations pass
- `1` if any validation fails

Example output:

```text
============================================================
Framework: openspec - ✓ PASSED
============================================================

✓ glossary.yaml
✓ artifact-taxonomy.yaml
✓ concept-mapping.yaml

============================================================
Category: status - ✓ PASSED
============================================================

✓ framework-analyses/spec-kit.yaml
✓ framework-analyses/bmad.yaml
✓ framework-analyses/openspec.yaml
✓ cross-analyses/by-theme.yaml
✓ cross-analyses/pairwise.yaml
✓ cross-analyses/synthesis.yaml
```

#### Validated Files

**Glossary files** (per framework):

- `docs/framework-analyses/{framework}/glossaries/glossary.yaml`
- `docs/framework-analyses/{framework}/glossaries/artifact-taxonomy.yaml`
- `docs/framework-analyses/{framework}/glossaries/concept-mapping.yaml`

**Status files**:

- `.assist/status/framework-analyses/{spec-kit,bmad,openspec}.yaml`
- `.assist/status/cross-analyses/{by-theme,pairwise,synthesis}.yaml`

#### Checks Performed

**For glossary files**:

1. **YAML Syntax**: Ensures the file is valid YAML
2. **Schema Version**: Checks for `schema_version: "1.0"`
3. **Metadata**: Verifies `metadata.framework` exists
4. **Content Minimums**:
   - glossary.yaml: ≥10 terms
   - artifact-taxonomy.yaml: ≥5 artifacts
   - concept-mapping.yaml: ≥5 total mappings
5. **JSON Schema**: Full schema validation

**For status files**:

1. **YAML Syntax**: Ensures the file is valid YAML
2. **Schema Version**: Checks for `schema_version: "1.0"`
3. **Required Fields**: `last_updated`, `stages`
4. **Identifier**: Either `framework` or `analysis_type` present
5. **Completion Range**: `overall_completion` is 0-100 if present
6. **JSON Schema**: Full schema validation
