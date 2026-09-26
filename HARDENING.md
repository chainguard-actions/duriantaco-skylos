<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.33.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.33.0** was hardened automatically. 1 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): The 'Install Skylos' step directly interpolates `${{ github.action_path }}` inside a `run:` shell command string: `run: python -m pip install "${{ github.action_path }}"`.

Any `${{ ... }}` expression interpolated directly into a `run:` block is a script-injection risk because the value flows through YAML template substitution before the shell ever sees it, allowing shell metacharacters to be injected. The fix is to pass the value via an `env:` variable and reference it as a quoted shell variable: set `ACTION_PATH: ${{ github.action_path }}` in an `env:` block and use `"$ACTION_PATH"` in the run script.

Locations:

- `action.yml:59`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed the script injection vulnerability in the 'Install Skylos' step (action.yml line 59). Moved `${{ github.action_path }}` out of the `run:` shell command and into an `env:` block as `ACTION_PATH: ${{ github.action_path }}`. The shell command now uses the quoted shell variable `"$ACTION_PATH"` instead of the direct expression interpolation.

