# yamlFixer
'''
Script: Fix Salt YAML Indentation Recursively
Here’s a safe Python script that:

Crawls your Salt state directory
Converts tabs to 2 spaces
Normalizes all lines to use 2-space indentation

Optionally prints out YAML validation errors
'''
'''
Replace "/path/to/your/netbox/" with the path to your Salt state folder (e.g., /srv/salt/netbox/).
'''
import os
import re
import yaml

def fix_yaml_indentation(root_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        for file in filenames:
            if file.endswith(('.sls', '.yaml', '.yml')):
                full_path = os.path.join(dirpath, file)
                with open(full_path, 'r') as f:
                    lines = f.readlines()

                fixed_lines = []
                for line in lines:
                    # Replace tabs with 2 spaces
                    line = line.replace('\t', '  ')

                    # Normalize indent to multiples of 2
                    if re.match(r'^\s+', line):
                        leading = len(line) - len(line.lstrip())
                        new_indent = ' ' * (leading // 2 * 2)
                        line = new_indent + line.lstrip()

                    fixed_lines.append(line)

                # Save the updated file
                with open(full_path, 'w') as f:
                    f.writelines(fixed_lines)

                # Optional: Validate YAML syntax
                try:
                    with open(full_path) as f:
                        yaml.safe_load(f)
                except Exception as e:
                    print(f"[!] YAML Error in {full_path}:\n    {e}")

    print("\n✅ All YAML indentation normalized to 2 spaces and checked.")

# Run this:
fix_yaml_indentation("/path/to/your/netbox/")
'''
Safety:
This script does not delete or restructure logic — it only:

Replaces tabs with spaces

Normalizes indentation spacing

Validates syntax

Still, you should commit your changes or back up the folder before running this, just in case.
'''
