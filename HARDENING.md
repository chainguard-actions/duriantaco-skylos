<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.22.1

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.22.1** was hardened automatically. 2 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): The 'Install Skylos' step directly interpolates `${{ github.action_path }}` inside a `run:` shell command string: `run: python -m pip install "${{ github.action_path }}"`.

Any `${{ ... }}` expression interpolated directly into a run: block is a script-injection risk — the value flows through YAML template substitution before the shell ever sees it, bypassing shell quoting. The safe pattern is to use the `$GITHUB_ACTION_PATH` environment variable instead, which is already available as a pre-set env var in composite actions.

Locations:

- `action.yml:59`

### script-injection (severity: high)

Sub-rule (b): The variable `$FLAGS` is expanded unquoted in two `run:` blocks. `$FLAGS` is built from `$SKYLOS_ANALYSIS`, which is sourced from `inputs.analysis` (an attacker-controllable input via the `env:` block). An unquoted shell expansion allows the shell to parse metacharacters (`;`, `|`, `&`, `$(...)`, whitespace, glob chars) out of the value, enabling command injection.

Offending lines:
- 'Run Skylos Scan' step: `          $FLAGS \`
- 'Upload to Skylos Dashboard' step: `          $FLAGS \`

Fix: quote the expansion as `"$FLAGS"`.

Locations:

- `action.yml:88`
- `action.yml:117`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed three script-injection issues in hardened/action/action.yml:
1. 'Install Skylos' step (line 59): Replaced `${{ github.action_path }}` with `$GITHUB_ACTION_PATH` to avoid YAML template substitution before shell execution.
2. 'Run Skylos Scan' step (line 88): Converted string-based `FLAGS` variable to a bash array (`FLAGS=()`/`FLAGS+=("--flag")`/`"${FLAGS[@]}"`), preventing shell metacharacter injection from the attacker-controllable `inputs.analysis` input while preserving correct multi-argument expansion.
3. 'Upload to Skylos Dashboard' step (line 117): Applied the same bash array fix for `FLAGS` as in the scan step.

