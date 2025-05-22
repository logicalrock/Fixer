# YAML Indentation Fixer (Salt Execution Module)

This Salt execution module recursively normalizes YAML and SaltStack `.sls` files in a given directory to use **2-space indentation**, replacing tabs and invalid spacing automatically.

---

## What It Does

- Replaces tabs with 2 spaces
- Normalizes indentation for `.sls`, `.yaml`, `.yml` files
- Validates YAML syntax using PyYAML
- Supports dry-run mode and logs all changes
- Returns a detailed summary and per-file log

---

## Files in This Package

- `yamlfixer.py`: The execution module to place under your Salt master `_modules` directory
- `README.md`: This usage guide

---

## Installation Steps

1. Unzip this file on your Salt master**:

```bash
unzip yamlfixer_execution_module.zip -d /srv/salt/_modules/
```

2. Sync the module to all minions**:

```bash
salt '*' saltutil.sync_modules
```

3. Verify it’s available**:

```bash
salt '*' sys.list_functions yamlfixer
```

You should see: `yamlfixer.fix_indents`

---

## Usage

### Dry-run (report only):
```bash
salt 'minion-id' yamlfixer.fix_indents path=/srv/salt/netbox dry_run=True
```

### Apply formatting fixes:
```bash
salt 'minion-id' yamlfixer.fix_indents path=/srv/salt/netbox dry_run=False
```

---

## Return Output

```yaml
summary:
  total_files: 15
  modified_files: 4
  error_files: 1
log:
  - "[MODIFIED] /srv/salt/netbox/init.sls"
  - "[OK] /srv/salt/netbox/user.sls (no changes)"
  - "[ERROR] /srv/salt/netbox/bad.yaml failed YAML validation: ..."
```

---

## Notes

- This script does not modify files outside the given directory
- It's safe to use in CI/CD pipelines or highstates for YAML lint enforcement
- Always version-control your Salt states before running it in apply mode

---

## Support

For enhancements, integration with Salt returners, or custom exclusions, feel free to extend the module or ask for an advanced version.
