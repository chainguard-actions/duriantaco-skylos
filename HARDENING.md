<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.23.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.23.0** was hardened automatically. 2 finding(s) were identified and resolved across 4 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Rule (a): The 'Install Skylos' step directly interpolates `${{ github.action_path }}` inside a `run:` shell command string: `run: python -m pip install "${{ github.action_path }}"`.

Any `${{ ... }}` expression directly inside a `run:` block is a script-injection risk because the value is substituted by the YAML template engine before the shell ever sees it, bypassing shell quoting. The fix is to pass the value via an `env:` variable and reference it as `"$ACTION_PATH"` in the script.

Locations:

- `action.yml:52`

### script-injection (severity: high)

Rule (b): In both the 'Run Skylos Scan' step and the 'Upload to Skylos Dashboard' step, the shell variable `$FLAGS` is expanded **unquoted** in the `python -m skylos.cli` command line (e.g., `python -m skylos.cli "$SKYLOS_PATH" --confidence "$SKYLOS_CONFIDENCE" $FLAGS --json`). `FLAGS` is constructed by appending strings derived from `$SKYLOS_ANALYSIS`, which is set from `inputs.analysis` — a caller-controlled input. An attacker supplying a crafted `inputs.analysis` value could inject shell metacharacters (`;`, `|`, `&`, `$(...)`, etc.) that survive into `$FLAGS` and are then interpreted by the shell due to the unquoted expansion. The fix is to quote the expansion: `"$FLAGS"`.

Locations:

- `action.yml:77`
- `action.yml:113`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed three script-injection issues in action.yml:
1. 'Install Skylos' step (line 52): Moved `${{ github.action_path }}` into an `env:` block as `ACTION_PATH` and referenced it as `"$ACTION_PATH"` in the run script.
2. 'Run Skylos Scan' step (line 77): Converted `FLAGS` from an unquoted string variable to a bash array (`FLAGS=()`), using `FLAGS+=(--flag)` to append and `"${FLAGS[@]}"` to expand safely.
3. 'Upload to Skylos Dashboard' step (line 113): Applied the same bash array pattern for `FLAGS` to prevent unquoted expansion of caller-controlled input values.

### Iteration 2

**Fixes applied:** script-injection, github-env-injection, missing-permissions, unpinned-uses

**Notes:**

Fixed all findings across 7 workflow files:

1. **script-injection** (corpus.yml, quality-benchmark.yml, skylos.yaml, tests.yaml, examples/skylos-plus-claude-security.yml, examples/skylos-tokenless-ci.yml, publish.yml): Moved all ${{ }} expressions from run: shell strings into step env: blocks, referencing them as plain $VAR_NAME environment variables in the shell scripts.

2. **github-env-injection** (skylos.yaml): In the 'Resolve diff base' step, all three values written to $GITHUB_OUTPUT are now sanitized with `printf '%s' ... | tr -d '\n\r'` before writing, preventing newline injection attacks.

3. **missing-permissions** (analyzer-speed.yml, corpus.yml, quality-benchmark.yml): Added `permissions: contents: read` top-level blocks to all three workflow files that lacked explicit permissions.

4. **unpinned-uses** (examples/skylos-plus-claude-security.yml, examples/skylos-tokenless-ci.yml): Pinned all mutable tag/branch references to full 40-character commit SHAs:
   - actions/checkout@v4 → @34e114876b0b11c390a56381ad16ebd13914f8d5
   - actions/setup-python@v5 → @a26af69be951a213d495a4c3e4e4022e16d87065
   - actions/upload-artifact@v4 → @ea165f8d65b6e75b540449e92b4886f43607fa02
   - anthropics/claude-code-action@main → @af0559ee4f514d1ef21826982bed13f7edc3c35e
   - actions/download-artifact@v4 → @d3f86a106a0bac45b974a628896c90dbdf5c8093

### Iteration 3

**Fixes applied:** github-env-injection

**Notes:**

Fixed two github-env-injection locations in hardened/action/.github/workflows/publish.yml:
1. Line 62 ('Resolve release tag input' step): Added `safe_tag="$(printf '%s' "$tag" | tr -d '\n\r')"` and changed the GITHUB_OUTPUT write to use `$safe_tag`.
2. Lines 172+ ('Derive image metadata' step): Added sanitization for $version (`safe_version`), $major (`safe_major`), and $minor (`safe_minor`) using the same `printf '%s' ... | tr -d '\n\r'` pipeline before each is written to $GITHUB_OUTPUT.

### Iteration 4

**Fixes applied:** github-env-injection

**Notes:**

Fixed the github-env-injection finding in hardened/action/.github/workflows/skylos.yaml. In the 'Run Skylos' step, added sanitization of the REPORT variable (built from github.run_number and github.sha) before writing to $GITHUB_OUTPUT. Changed `echo "REPORT=$REPORT" >> "$GITHUB_OUTPUT"` to first compute `safe_report=$(printf '%s' "$REPORT" | tr -d '\n\r')` and then write `echo "REPORT=$safe_report" >> "$GITHUB_OUTPUT"`.

