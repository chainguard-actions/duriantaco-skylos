<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.33.2

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.33.2** was hardened automatically. 1 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Rule (a) violation: The 'Install Skylos' step directly interpolates a ${{ }} expression inside a `run:` shell command string. The line `run: python -m pip install "${{ github.action_path }}"` embeds `${{ github.action_path }}` directly into the shell command before the shell ever sees it. Any `${{ ... }}` expression inside a `run:` block is a script-injection finding regardless of which context it reads from. The value should instead be passed via an `env:` variable and referenced as `"$ACTION_PATH"` in the script.

Locations:

- `action.yml:57`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed the script injection in the 'Install Skylos' step of action.yml. Moved `${{ github.action_path }}` from the `run:` shell command string into an `env:` block as `ACTION_PATH: ${{ github.action_path }}`, and updated the shell command to reference it as `"$ACTION_PATH"` instead of `"${{ github.action_path }}"`.

