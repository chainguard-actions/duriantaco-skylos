<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.39.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.39.0** was hardened automatically. 1 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): A `${{ }}` expression is directly interpolated inside a `run:` shell command string in the 'Install Skylos' step. The expression `${{ github.action_path }}` is embedded directly in the shell command `python -m pip install "${{ github.action_path }}"`. Any `${{ ... }}` expression inside a `run:` block undergoes YAML template substitution before the shell ever sees it, making it a script-injection risk. The value should be passed via an `env:` variable and referenced as `"$ENV_VAR"` in the shell script instead.

Locations:

- `action.yml:76`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed the 'Install Skylos' step in action.yml (line 76): moved `${{ github.action_path }}` out of the `run:` shell command and into an `env:` block as `ACTION_PATH: ${{ github.action_path }}`. The shell command now references it safely as `"$ACTION_PATH"` instead of the direct template expression.

