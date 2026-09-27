<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.39.2

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.39.2** was hardened automatically. 1 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): A ${{ }} expression is directly interpolated inside a run: shell command string. The 'Install Skylos' step uses `run: python -m pip install "${{ github.action_path }}"`, which injects the github.action_path context value directly into the shell command via YAML template substitution before the shell ever sees it. Per the check rules, any ${{ ... }} expression directly inside a run: block is a script-injection finding regardless of which context it reads from. The safe pattern is to pass the value via an env: variable and reference it as "$ENV_VAR" in the shell script.

Locations:

- `action.yml:72`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed the 'Install Skylos' step at line 72 of action.yml. Moved `${{ github.action_path }}` out of the `run:` shell command into an `env:` block as `SKYLOS_ACTION_PATH`, then referenced it as `"$SKYLOS_ACTION_PATH"` in the shell script. This prevents the context value from being interpolated directly into the shell command string before the shell sees it.

