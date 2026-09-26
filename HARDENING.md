<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.26.1

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.26.1** was hardened automatically. 2 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): The 'Install Skylos' step directly interpolates `${{ github.action_path }}` inside a `run:` shell command string: `run: python -m pip install "${{ github.action_path }}"`. Any ${{ ... }} expression directly in a run: block is a script-injection risk as the value is substituted by the template engine before the shell ever sees it.

Locations:

- `action.yml:59`

### script-injection (severity: high)

Sub-rule (b): The variable `$FLAGS` — built from `$SKYLOS_ANALYSIS` which is sourced from `inputs.analysis` (an attacker-controllable input) — is expanded unquoted in the shell command `python -m skylos.cli "$SKYLOS_PATH" \ --confidence "$SKYLOS_CONFIDENCE" \ $FLAGS \ --json`. Unquoted expansion allows shell metacharacters (`;`, `|`, `&`, `$(...)`, etc.) embedded in the input to be interpreted by the shell. This occurs in both the 'Run Skylos Scan' step (line 88) and the 'Upload to Skylos Dashboard' step (line ~123).

Locations:

- `action.yml:88`
- `action.yml:123`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed three script-injection instances in action.yml: (1) Moved `${{ github.action_path }}` from the 'Install Skylos' run: shell string into an env: block as ACTION_PATH, referenced as "$ACTION_PATH" in the shell. (2) In both 'Run Skylos Scan' (line 88) and 'Upload to Skylos Dashboard' (line ~123), replaced the unquoted string variable `$FLAGS` (built from attacker-controllable `inputs.analysis`) with a bash array `FLAGS=()` populated via `FLAGS+=("--flag")` and expanded safely as `"${FLAGS[@]}"`, preventing shell metacharacter injection.

