<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.34.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.34.0** was hardened automatically. 1 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): A ${{ }} expression is directly interpolated inside a run: shell command string in the 'Install Skylos' step. The line `run: python -m pip install "${{ github.action_path }}"` embeds the github.action_path context directly into the shell command before the shell ever sees it. Any ${{ ... }} expression inside a run: block is a script-injection risk regardless of which context it reads from.

Locations:

- `action.yml:100`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed the script injection vulnerability in the 'Install Skylos' step (action.yml line 100). Moved `${{ github.action_path }}` from the run: shell command string into an env: block as `SKYLOS_ACTION_PATH: ${{ github.action_path }}`, and updated the shell command to reference it as `"$SKYLOS_ACTION_PATH"` instead.

