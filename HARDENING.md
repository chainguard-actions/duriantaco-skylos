<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.35.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.35.0** was hardened automatically. 1 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): The 'Install Skylos' step directly interpolates a ${{ }} expression inside a run: shell command string. The line `run: python -m pip install "${{ github.action_path }}"` embeds `${{ github.action_path }}` directly in the shell command. Per the script-injection check, ANY ${{ ... }} expression directly inside a run: block is a finding — the value is substituted by the GitHub Actions template engine before the shell ever sees it, bypassing shell quoting. The fix is to pass the value via an env: variable and reference it as "$ENV_VAR" in the script.

Locations:

- `action.yml:96`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed the 'Install Skylos' step in action.yml (line 96): moved `${{ github.action_path }}` from the `run:` shell command into an `env:` block as `SKYLOS_ACTION_PATH`, and updated the shell command to reference it as `"$SKYLOS_ACTION_PATH"`. This prevents the GitHub Actions template engine from substituting the value directly into the shell command string before the shell processes it.

