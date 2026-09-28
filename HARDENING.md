<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.40.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.40.0** was hardened automatically. 1 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Rule (a) violation: A `${{ }}` expression is interpolated directly inside a `run:` shell command string. In the "Install Skylos" step, `${{ github.action_path }}` is embedded directly in the shell command `python -m pip install "${{ github.action_path }}"`. Even though `github.action_path` is not typically attacker-controlled, any `${{ ... }}` expression inside a `run:` block undergoes YAML template substitution before the shell ever sees it, making it a script-injection risk. The value should be passed via an `env:` variable and referenced as `"$ENV_VAR"` instead.

Locations:

- `action.yml:75`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed the 'Install Skylos' step in action.yml (line 75): moved `${{ github.action_path }}` out of the `run:` shell command and into an `env:` block as `SKYLOS_ACTION_PATH`. The shell command now uses `"$SKYLOS_ACTION_PATH"` instead of the inline expression, eliminating the script-injection risk.

