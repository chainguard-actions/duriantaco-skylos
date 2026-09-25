<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.36.1

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.36.1** was hardened automatically. 1 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): A ${{ }} expression is interpolated directly inside a run: shell command string in the 'Install Skylos' step. The line `python -m pip install "${{ github.action_path }}"` embeds the github.action_path context value directly into the shell command before the shell ever sees it. Per the check rules, any ${{ ... }} directly inside a run: script is a script-injection finding regardless of which context it reads from. The fix is to route the value through an env: variable (e.g., `ACTION_PATH: ${{ github.action_path }}`) and reference `"$ACTION_PATH"` in the run: block instead.

Locations:

- `action.yml:76`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed the 'Install Skylos' step in action.yml (line 76): moved `${{ github.action_path }}` out of the `run:` shell command into an `env:` block as `ACTION_PATH: ${{ github.action_path }}`, then updated the shell command to use `"$ACTION_PATH"` instead of the inline expression.

