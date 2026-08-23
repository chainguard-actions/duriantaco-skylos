<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.34.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.34.0** was hardened automatically. 3 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): The 'Install Skylos' step directly interpolates `${{ github.action_path }}` inside a `run:` shell command string: `run: python -m pip install "${{ github.action_path }}"`  Any `${{ ... }}` expression inside a `run:` block is a script-injection risk because the value is substituted by the YAML template engine before the shell ever sees it, bypassing shell quoting.

Locations:

- `action.yml:97`

### script-injection (severity: high)

Sub-rule (b): The 'Run Skylos Scan' step uses `$FLAGS` unquoted in the CLI invocation: `$FLAGS \`. `$FLAGS` is built from `$SKYLOS_ANALYSIS`, which is sourced from `inputs.analysis` (an untrusted caller-controlled input). Unquoted shell variable expansion allows word splitting and glob expansion of the value.

Locations:

- `action.yml:131`

### script-injection (severity: high)

Sub-rule (b): The 'Upload to Skylos Dashboard' step uses `$FLAGS` unquoted in the CLI invocation: `$FLAGS \`. `$FLAGS` is built from `$SKYLOS_ANALYSIS`, which is sourced from `inputs.analysis` (an untrusted caller-controlled input). Unquoted shell variable expansion allows word splitting and glob expansion of the value.

Locations:

- `action.yml:184`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed all three script-injection findings in hardened/action/action.yml:
1. 'Install Skylos' step (line 97): Moved `${{ github.action_path }}` into an `env:` block as `SKYLOS_ACTION_PATH` and referenced it as `"$SKYLOS_ACTION_PATH"` in the run command.
2. 'Run Skylos Scan' step (line 131): Converted `FLAGS` from an unquoted plain string variable to a bash array (`FLAGS=()`), using `FLAGS+=("--flag")` for appending and `"${FLAGS[@]}"` for safe expansion.
3. 'Upload to Skylos Dashboard' step (line 184): Same bash array fix as finding 2, eliminating the unquoted `$FLAGS` word-splitting risk.

