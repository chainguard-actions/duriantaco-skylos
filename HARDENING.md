<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.36.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.36.0** was hardened automatically. 1 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): The 'Install Skylos' step directly interpolates `${{ github.action_path }}` inside a `run:` shell command string: `run: python -m pip install "${{ github.action_path }}"`.

Any `${{ ... }}` expression interpolated directly into a `run:` block is a script-injection risk because the value is substituted by the GitHub Actions template engine before the shell ever sees it, bypassing shell quoting. The safe pattern is to route the value through an `env:` variable (as the 'Build Skylos Go engine' step already does correctly with `SKYLOS_ACTION_PATH: ${{ github.action_path }}`) and then reference it as `"$SKYLOS_ACTION_PATH"` inside the `run:` block.

Locations:

- `action.yml:86`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed the 'Install Skylos' step in hardened/action/action.yml (line 86): moved `${{ github.action_path }}` out of the `run:` shell string and into an `env:` block as `SKYLOS_ACTION_PATH: ${{ github.action_path }}`, then referenced it as `"$SKYLOS_ACTION_PATH"` in the run command. This follows the same safe pattern already used in the 'Build Skylos Go engine' step.

