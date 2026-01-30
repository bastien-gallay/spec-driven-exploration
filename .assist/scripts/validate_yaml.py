#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pyyaml>=6.0",
#     "jsonschema>=4.0",
# ]
# ///
"""
YAML Schema Validator

Validates YAML files against JSON Schema-style schemas.
Supports the schema format used in .assist/schemas/.

Usage:
    # Validate a single file
    uv run .assist/scripts/validate_yaml.py <yaml_file> <schema_file>

    # Validate framework glossaries
    uv run .assist/scripts/validate_yaml.py --framework <name>

    # Validate status files
    uv run .assist/scripts/validate_yaml.py --status

    # Validate all (frameworks + status)
    uv run .assist/scripts/validate_yaml.py --all

Examples:
    uv run .assist/scripts/validate_yaml.py \\
        docs/framework-analyses/openspec/glossaries/glossary.yaml \\
        .assist/schemas/glossary.schema.yaml

    uv run .assist/scripts/validate_yaml.py --framework openspec
    uv run .assist/scripts/validate_yaml.py --status
    uv run .assist/scripts/validate_yaml.py --all
"""

import argparse
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Error: PyYAML is required. Install with: uv pip install pyyaml")
    sys.exit(1)

HAS_JSONSCHEMA = False
jsonschema_validate = None
JsonSchemaValidationError: type[Exception] = Exception

try:
    from jsonschema import validate as _validate
    from jsonschema import ValidationError as _ValidationError

    jsonschema_validate = _validate
    JsonSchemaValidationError = _ValidationError
    HAS_JSONSCHEMA = True
except ImportError:
    pass


# Schema file mappings for glossaries
GLOSSARY_SCHEMA_MAPPINGS = {
    "glossary.yaml": "glossary.schema.yaml",
    "artifact-taxonomy.yaml": "artifact-taxonomy.schema.yaml",
    "concept-mapping.yaml": "concept-mapping.schema.yaml",
}

# Status files to validate
STATUS_FILES = {
    "framework-analyses": [
        "spec-kit.yaml",
        "bmad.yaml",
        "openspec.yaml",
    ],
    "cross-analyses": [
        "by-theme.yaml",
        "pairwise.yaml",
        "synthesis.yaml",
    ],
}

FRAMEWORKS = ["spec-kit", "bmad", "openspec"]


def load_yaml(path: Path) -> dict:
    """Load and parse a YAML file."""
    with open(path) as f:
        return yaml.safe_load(f)


def validate_yaml_syntax(path: Path) -> tuple[bool, str | None, dict | None]:
    """Validate YAML syntax and return parsed content."""
    try:
        data = load_yaml(path)
        return True, None, data
    except yaml.YAMLError as e:
        return False, str(e), None


def validate_against_schema(
    data: dict, schema_path: Path
) -> tuple[bool, list[str]]:
    """Validate data against a JSON Schema."""
    if not HAS_JSONSCHEMA or jsonschema_validate is None:
        return True, ["jsonschema not installed, skipping schema validation"]

    try:
        schema = load_yaml(schema_path)
        jsonschema_validate(instance=data, schema=schema)
        return True, []
    except JsonSchemaValidationError as e:
        msg = getattr(e, "message", str(e))
        return False, [f"Schema validation error: {msg}"]
    except Exception as e:
        return False, [f"Error loading schema: {e}"]


def validate_glossary_structure(data: dict, filename: str) -> tuple[bool, list[str]]:
    """Validate basic structure requirements for glossary files."""
    errors = []

    # Check schema_version
    if data.get("schema_version") != "1.0":
        errors.append("Missing or invalid schema_version (expected '1.0')")

    # Check metadata
    if "metadata" not in data:
        errors.append("Missing 'metadata' section")
    elif "framework" not in data.get("metadata", {}):
        errors.append("Missing 'framework' in metadata")

    # Check content based on file type
    if filename == "glossary.yaml":
        terms = data.get("terms", [])
        if len(terms) < 10:
            errors.append(f"Insufficient terms: {len(terms)} (minimum 10)")

    elif filename == "artifact-taxonomy.yaml":
        artifacts = data.get("artifacts", [])
        if len(artifacts) < 5:
            errors.append(f"Insufficient artifacts: {len(artifacts)} (minimum 5)")

    elif filename == "concept-mapping.yaml":
        relationships = len(data.get("relationships", []))
        mappings = len(data.get("cross_framework_mappings", []))
        unique = len(data.get("unique_concepts", []))
        total = relationships + mappings + unique
        if total < 5:
            errors.append(f"Insufficient mappings: {total} (minimum 5)")

    return len(errors) == 0, errors


def validate_status_structure(data: dict, _filename: str) -> tuple[bool, list[str]]:
    """Validate basic structure requirements for status files."""
    errors = []

    # Check schema_version
    if data.get("schema_version") != "1.0":
        errors.append("Missing or invalid schema_version (expected '1.0')")

    # Check last_updated
    if "last_updated" not in data:
        errors.append("Missing 'last_updated' field")

    # Check stages
    if "stages" not in data:
        errors.append("Missing 'stages' section")

    # Check for framework or analysis_type
    has_framework = "framework" in data
    has_analysis_type = "analysis_type" in data

    if not has_framework and not has_analysis_type:
        errors.append("Missing 'framework' or 'analysis_type' field")

    # Check overall_completion
    completion = data.get("overall_completion")
    if completion is not None:
        if not isinstance(completion, int) or completion < 0 or completion > 100:
            errors.append(f"Invalid overall_completion: {completion} (expected 0-100)")

    return len(errors) == 0, errors


def validate_file(
    yaml_path: Path,
    schema_path: Path | None = None,
    file_type: str = "glossary",
) -> tuple[bool, list[str]]:
    """Validate a single YAML file."""
    errors = []

    # Check file exists
    if not yaml_path.exists():
        return False, [f"File not found: {yaml_path}"]

    # Validate YAML syntax
    valid, error, data = validate_yaml_syntax(yaml_path)
    if not valid:
        return False, [f"YAML syntax error: {error}"]

    if data is None:
        return False, ["Empty YAML file"]

    # Validate structure based on file type
    if file_type == "status":
        valid, struct_errors = validate_status_structure(data, yaml_path.name)
    else:
        valid, struct_errors = validate_glossary_structure(data, yaml_path.name)
    errors.extend(struct_errors)

    # Validate against schema if provided
    if schema_path and schema_path.exists():
        valid, schema_errors = validate_against_schema(data, schema_path)
        errors.extend(schema_errors)

    return len(errors) == 0, errors


def validate_framework(framework: str, base_path: Path) -> dict:
    """Validate all glossary files for a framework."""
    results = {"framework": framework, "files": {}, "valid": True}

    glossary_dir = base_path / "docs/framework-analyses" / framework / "glossaries"
    schema_dir = base_path / ".assist/schemas"

    for yaml_file, schema_file in GLOSSARY_SCHEMA_MAPPINGS.items():
        yaml_path = glossary_dir / yaml_file
        schema_path = schema_dir / schema_file

        valid, errors = validate_file(yaml_path, schema_path, file_type="glossary")
        results["files"][yaml_file] = {
            "valid": valid,
            "errors": errors,
            "path": str(yaml_path),
        }
        if not valid:
            results["valid"] = False

    return results


def validate_all_status(base_path: Path) -> dict:
    """Validate all status files."""
    results = {"category": "status", "files": {}, "valid": True}

    schema_path = base_path / ".assist/schemas/status.schema.yaml"
    status_dir = base_path / ".assist/status"

    for category, files in STATUS_FILES.items():
        for filename in files:
            yaml_path = status_dir / category / filename
            display_name = f"{category}/{filename}"

            valid, errors = validate_file(
                yaml_path, schema_path, file_type="status"
            )
            results["files"][display_name] = {
                "valid": valid,
                "errors": errors,
                "path": str(yaml_path),
            }
            if not valid:
                results["valid"] = False

    return results


def print_results(results: dict) -> None:
    """Print validation results."""
    # Determine title
    if "framework" in results:
        title = f"Framework: {results['framework']}"
    elif "category" in results:
        title = f"Category: {results['category']}"
    else:
        title = "Validation"

    status = "✓ PASSED" if results["valid"] else "✗ FAILED"

    print(f"\n{'='*60}")
    print(f"{title} - {status}")
    print(f"{'='*60}")

    for filename, file_result in results["files"].items():
        status_icon = "✓" if file_result["valid"] else "✗"
        print(f"\n{status_icon} {filename}")

        if file_result["errors"]:
            for error in file_result["errors"]:
                print(f"  - {error}")


def main():
    parser = argparse.ArgumentParser(
        description="Validate YAML files against schemas",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )

    parser.add_argument(
        "yaml_file",
        nargs="?",
        help="YAML file to validate",
    )
    parser.add_argument(
        "schema_file",
        nargs="?",
        help="Schema file to validate against",
    )
    parser.add_argument(
        "--framework",
        choices=FRAMEWORKS,
        help="Validate all glossary files for a framework",
    )
    parser.add_argument(
        "--status",
        action="store_true",
        help="Validate all status files in .assist/status/",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Validate all frameworks and status files",
    )
    parser.add_argument(
        "--base-path",
        type=Path,
        default=Path.cwd(),
        help="Base path for the project (default: current directory)",
    )

    args = parser.parse_args()

    # Determine base path
    base_path = args.base_path

    # Validate all frameworks and status
    if args.all:
        all_valid = True

        # Validate frameworks
        for framework in FRAMEWORKS:
            results = validate_framework(framework, base_path)
            print_results(results)
            if not results["valid"]:
                all_valid = False

        # Validate status files
        results = validate_all_status(base_path)
        print_results(results)
        if not results["valid"]:
            all_valid = False

        sys.exit(0 if all_valid else 1)

    # Validate status files only
    if args.status:
        results = validate_all_status(base_path)
        print_results(results)
        sys.exit(0 if results["valid"] else 1)

    # Validate single framework
    if args.framework:
        results = validate_framework(args.framework, base_path)
        print_results(results)
        sys.exit(0 if results["valid"] else 1)

    # Validate single file
    if args.yaml_file:
        yaml_path = Path(args.yaml_file)
        schema_path = Path(args.schema_file) if args.schema_file else None

        # Detect file type from path
        file_type = "status" if ".assist/status" in str(yaml_path) else "glossary"

        valid, errors = validate_file(yaml_path, schema_path, file_type=file_type)

        status = "✓ PASSED" if valid else "✗ FAILED"
        print(f"\n{yaml_path.name}: {status}")

        if errors:
            for error in errors:
                print(f"  - {error}")

        sys.exit(0 if valid else 1)

    parser.print_help()
    sys.exit(1)


if __name__ == "__main__":
    main()
