"""
Mail Merge - Production Version
==================================

WHAT THIS PROGRAM DOES (Flow):
1. Validate that template file and names file exist
2. Read and validate template (must contain [name] placeholder)
3. Read names file, strip whitespace, filter empty/invalid names
4. Create output directory if it doesn't exist
5. For each valid name:
   a. Sanitize name for filename safety
   b. Replace [name] placeholder in template
   c. Write personalized letter to output file
   d. Log progress
6. Display summary: files created, skipped names, errors

INPUTS:
- Template file: 16_mail_merge_template.txt (must contain [name] placeholder)
- Names file: 16_invited_names.txt (one name per line)

OUTPUTS:
- Individual text files in output/ folder: for_<Name>.txt
- Progress messages and summary (console)
- Error messages for invalid inputs (console)

SIDE EFFECTS:
- Creates output/ directory if it doesn't exist
- Writes text files to disk
- Overwrites existing output files with same names

RULES:
- [name] placeholder is case-sensitive
- Empty lines and whitespace-only names are skipped
- Names sanitized for filesystem safety (alphanumeric + spaces + hyphens)
- Existing output files are overwritten

ASSUMPTIONS:
- Template and names files exist in same directory as script
- UTF-8 encoding for all files

DEPENDENCIES:
- os (standard library)
- pathlib (standard library)
"""

import os
import re
from pathlib import Path


SCRIPT_DIR = Path(__file__).parent.resolve()
TEMPLATE_PATH = SCRIPT_DIR / "16_mail_merge_template.txt"
NAMES_PATH = SCRIPT_DIR / "16_invited_names.txt"
OUTPUT_DIR = SCRIPT_DIR / "output"
PLACEHOLDER = "[name]"


def validate_files() -> bool:
    """Check that required input files exist.

    Returns:
        True if both files exist.
    """
    ok = True
    if not TEMPLATE_PATH.exists():
        print(f"  Error: Template file not found: {TEMPLATE_PATH}")
        ok = False
    if not NAMES_PATH.exists():
        print(f"  Error: Names file not found: {NAMES_PATH}")
        ok = False
    return ok


def read_template() -> str:
    """Read the template file and validate it contains the placeholder.

    Returns:
        Template text.

    Raises:
        ValueError: If template doesn't contain [name] placeholder.
    """
    text = TEMPLATE_PATH.read_text(encoding="utf-8")
    if PLACEHOLDER not in text:
        raise ValueError(f"Template must contain '{PLACEHOLDER}' placeholder.")
    return text


def read_names() -> list[str]:
    """Read and clean the names file.

    Returns:
        List of non-empty, stripped name strings.
    """
    raw = NAMES_PATH.read_text(encoding="utf-8")
    names = []
    for line in raw.splitlines():
        name = line.strip()
        if name:
            names.append(name)
    return names


def sanitize_filename(name: str) -> str:
    """Sanitize a name for safe use in a filename.

    Args:
        name: The raw name string.

    Returns:
        Filesystem-safe name (alphanumeric, spaces, hyphens only).
    """
    return re.sub(r"[^\w\s-]", "", name).strip()


def generate_letters(template: str, names: list[str]) -> dict:
    """Generate personalized letters for each name.

    Args:
        template: Template text with [name] placeholder.
        names: List of names to personalize for.

    Returns:
        Dict with 'created', 'skipped', 'errors' counts.
    """
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    stats = {"created": 0, "skipped": 0, "errors": 0}

    for name in names:
        safe_name = sanitize_filename(name)
        if not safe_name:
            print(f"  Skipped: '{name}' (invalid characters)")
            stats["skipped"] += 1
            continue

        letter = template.replace(PLACEHOLDER, name)
        output_path = OUTPUT_DIR / f"for_{safe_name}.txt"

        try:
            output_path.write_text(letter, encoding="utf-8")
            print(f"  Created: {output_path.name}")
            stats["created"] += 1
        except OSError as e:
            print(f"  Error writing {output_path.name}: {e}")
            stats["errors"] += 1

    return stats


def run() -> None:
    """Main program entry."""
    print("=" * 40)
    print("        Mail Merge Generator")
    print("=" * 40)
    print()

    if not validate_files():
        print("\nCannot proceed without required files.")
        return

    try:
        template = read_template()
    except ValueError as e:
        print(f"  Error: {e}")
        return

    names = read_names()
    if not names:
        print("  No valid names found in names file.")
        return

    print(f"  Template: {TEMPLATE_PATH.name}")
    print(f"  Names found: {len(names)}")
    print(f"  Output dir: {OUTPUT_DIR}\n")

    stats = generate_letters(template, names)

    print(f"\n--- Summary ---")
    print(f"  Letters created: {stats['created']}")
    print(f"  Names skipped:   {stats['skipped']}")
    print(f"  Errors:          {stats['errors']}")
    print(f"----------------\n")


if __name__ == "__main__":
    run()
