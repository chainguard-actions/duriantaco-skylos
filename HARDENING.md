<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.32.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.32.0** was hardened automatically. 3 finding(s) were identified and resolved across 2 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): The 'Install Skylos' step directly interpolates `${{ github.action_path }}` inside a `run:` shell command string: `run: python -m pip install "${{ github.action_path }}"`. Any `${{ ... }}` expression interpolated directly in a run block is a script-injection risk — the YAML template substitution occurs before the shell ever sees the value, bypassing shell quoting.

Locations:

- `action.yml:59`

### script-injection (severity: high)

Sub-rule (b): In the 'Run Skylos Scan' step, the shell variable `$FLAGS` is expanded unquoted in the `python -m skylos.cli` invocation (`$FLAGS \`). `$FLAGS` is built from `$SKYLOS_ANALYSIS`, which is sourced from `inputs.analysis` (attacker-controllable). An unquoted expansion allows shell metacharacter injection (`;`, `|`, `&`, `$(...)`, etc.) from the input value.

Locations:

- `action.yml:91`

### script-injection (severity: high)

Sub-rule (b): In the 'Upload to Skylos Dashboard' step, the shell variable `$FLAGS` is expanded unquoted in the `python -m skylos.cli` invocation (`$FLAGS \`). `$FLAGS` is built from `$SKYLOS_ANALYSIS`, which is sourced from `inputs.analysis` (attacker-controllable). An unquoted expansion allows shell metacharacter injection from the input value.

Locations:

- `action.yml:129`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed all three script-injection findings in hardened/action/action.yml:
1. 'Install Skylos' step (line 59): Moved `${{ github.action_path }}` out of the run block into an `env:` variable `ACTION_PATH`, referenced as `"$ACTION_PATH"` in the shell command.
2. 'Run Skylos Scan' step (line 91): Replaced the unquoted `$FLAGS` string variable with a bash array (`FLAGS=()`), appending flags with `FLAGS+=(--flag)` and expanding safely as `"${FLAGS[@]}"`.
3. 'Upload to Skylos Dashboard' step (line 129): Applied the same bash array pattern to eliminate the unquoted `$FLAGS` expansion in the upload step.

### Iteration 2

**Fixes applied:** script-injection, github-env-injection, missing-permissions, unpinned-uses

**Notes:**

Fixed all findings across 7 workflow files:

1. **script-injection** (high): Moved all ${{ }} expressions out of run: shell strings into env: blocks across corpus.yml (lines 59-60), quality-benchmark.yml (lines 49-50), skylos.yaml (lines 57-62 and 140), tests.yaml (lines 43, 72, 81, 113-115), publish.yml (line 270), examples/skylos-plus-claude-security.yml (line 59), and examples/skylos-tokenless-ci.yml (line 43).

2. **github-env-injection** (high): In skylos.yaml 'Resolve diff base' step, all github context values written to $GITHUB_OUTPUT are now sanitized with `printf '%s' "$VAR" | tr -d '\n\r'` before writing. The 'Run Skylos' step also sanitizes the REPORT value before writing to $GITHUB_OUTPUT.

3. **missing-permissions** (medium): Added `permissions: contents: read` top-level blocks to analyzer-speed.yml, corpus.yml, and quality-benchmark.yml.

4. **unpinned-uses** (high): Pinned all unpinned action references in examples/skylos-plus-claude-security.yml and examples/skylos-tokenless-ci.yml to full 40-character SHA digests: actions/checkout@v4→11d5960a..., actions/setup-python@v5→a26af69b..., actions/upload-artifact@v4→ea165f8d..., anthropics/claude-code-action@main→be7b93b1..., actions/download-artifact@v4→d3f86a10...

