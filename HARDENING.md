<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.22.1

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.22.1** was hardened automatically. 1 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Rule (a) violation: The 'Install Skylos' step directly interpolates a ${{ }} expression inside a run: shell command string. Specifically, `run: python -m pip install "${{ github.action_path }}"` embeds `${{ github.action_path }}` directly in the shell command. Per the check rules, ANY ${{ ... }} expression directly inside a run: block is a script-injection finding, as the value flows through YAML template substitution before the shell ever sees it. The fix is to pass the value via an env: variable and reference it as `"$ACTION_PATH"` in the shell script.

Locations:

- `action.yml:59`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed script injection in the 'Install Skylos' step (action.yml line 59). Moved `${{ github.action_path }}` out of the run: shell string and into an env: block as `ACTION_PATH: ${{ github.action_path }}`. The shell command now references it safely as `"$ACTION_PATH"` instead of directly interpolating the expression.

