"""
Mail Merge - Simple Version
==============================

WHAT THIS PROGRAM DOES (Flow):
1. Read the template file (16_mail_merge_template.txt)
2. Read the names file (16_invited_names.txt)
3. For each name:
   a. Replace [name] placeholder in template with the actual name
   b. Write the personalized letter to an output file
4. Print completion message

INPUTS:
- Template file: 16_mail_merge_template.txt (must contain [name] placeholder)
- Names file: 16_invited_names.txt (one name per line)

OUTPUTS:
- Individual text files in output/ folder: for_<Name>.txt
- Progress messages (console)

SIDE EFFECTS:
- Creates output/ directory if it doesn't exist
- Writes files to disk

RULES:
- [name] placeholder is case-sensitive
- Each name generates one output file
- Output files named "for_<Name>.txt"

ASSUMPTIONS:
- Template and names files exist in same directory
- File system supports generated filenames

DEPENDENCIES:
- os (standard library)
"""

import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_PATH = os.path.join(SCRIPT_DIR, "16_mail_merge_template.txt")
NAMES_PATH = os.path.join(SCRIPT_DIR, "16_invited_names.txt")
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "output")

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(TEMPLATE_PATH, "r") as f:
    template = f.read()

with open(NAMES_PATH, "r") as f:
    names = f.readlines()

for name in names:
    name = name.strip()
    if name:
        letter = template.replace("[name]", name)
        output_path = os.path.join(OUTPUT_DIR, f"for_{name}.txt")
        with open(output_path, "w") as f:
            f.write(letter)
        print(f"Created: for_{name}.txt")

print(f"\nDone! {len([n for n in names if n.strip()])} letters generated.")
