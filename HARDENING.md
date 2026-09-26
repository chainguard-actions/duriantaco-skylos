<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.32.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.32.0** was hardened automatically. 3 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): The 'Install Skylos' step directly interpolates `${{ github.action_path }}` inside a `run:` shell command string: `run: python -m pip install "${{ github.action_path }}"`. Any `${{ ... }}` expression interpolated directly into a run block is a script-injection risk — the value is substituted by the Actions template engine before the shell ever sees it, bypassing shell quoting. The fix is to pass the value via an env var and reference it as `"$ACTION_PATH"` instead.

Locations:

- `action.yml:59`

### script-injection (severity: high)

Sub-rule (b): In the 'Run Skylos Scan' step, the shell variable `$FLAGS` is expanded unquoted in the run command: `$FLAGS \`. `$FLAGS` is built by appending strings derived from `$SKYLOS_ANALYSIS`, which is sourced from `inputs.analysis` (a caller-controlled input). An unquoted expansion allows the shell to parse metacharacters (`;`, `|`, `&`, `$(...)`, etc.) out of the value, enabling command injection. The fix is to use an array or quote the expansion: `"$FLAGS"`.

Locations:

- `action.yml:91`

### script-injection (severity: high)

Sub-rule (b): In the 'Upload to Skylos Dashboard' step, the shell variable `$FLAGS` is expanded unquoted in the run command: `$FLAGS \`. `$FLAGS` is built from `$SKYLOS_ANALYSIS`, which is sourced from `inputs.analysis` (a caller-controlled input). An unquoted expansion allows shell metacharacter injection. The fix is to quote the expansion: `"$FLAGS"`.

Locations:

- `action.yml:130`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed all three script-injection findings in hardened/action/action.yml:
1. 'Install Skylos' step: Moved `${{ github.action_path }}` into an env var `ACTION_PATH` and referenced it as `"$ACTION_PATH"` in the run command.
2. 'Run Skylos Scan' step: Converted `FLAGS` from a string with unquoted expansion (`$FLAGS`) to a bash array (`FLAGS=()`), built with `FLAGS+=(--flag)` and expanded safely as `"${FLAGS[@]}"`.
3. 'Upload to Skylos Dashboard' step: Same bash array fix applied — `FLAGS=()` with `FLAGS+=(--flag)` appends and `"${FLAGS[@]}"` expansion, preventing shell metacharacter injection from the caller-controlled `inputs.analysis` value.

