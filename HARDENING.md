<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.36.1

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.36.1** was hardened automatically. 1 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): A GitHub Actions expression `${{ github.action_path }}` is interpolated directly inside a `run:` shell command string in the 'Install Skylos' step. The offending line is: `run: python -m pip install "${{ github.action_path }}"`. Even though `github.action_path` is GitHub-controlled, any `${{ ... }}` expression directly inside a `run:` block is a script-injection risk because the value flows through YAML template substitution before the shell ever sees it, bypassing shell quoting protections. The fix is to pass the value via an `env:` variable and reference it as `"$ENV_VAR"` in the shell script.

Locations:

- `action.yml:64`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed the 'Install Skylos' step in hardened/action/action.yml (line 64): moved `${{ github.action_path }}` out of the `run:` shell command and into an `env:` block as `SKYLOS_ACTION_PATH`, then referenced it as `"$SKYLOS_ACTION_PATH"` in the shell script. This eliminates the YAML template substitution bypass that constituted the script-injection risk.

