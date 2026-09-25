<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.23.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.23.0** was hardened automatically. 1 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): The 'Install Skylos' step directly interpolates `${{ github.action_path }}` inside a `run:` shell command string: `run: python -m pip install "${{ github.action_path }}"`.

Any `${{ ... }}` expression interpolated directly inside a `run:` block is a script-injection risk because the value is substituted by the YAML template engine before the shell ever sees it, bypassing shell quoting. Even though `github.action_path` is GitHub-controlled rather than attacker-supplied, the rule requires that no `${{ ... }}` expression appear directly inside a `run:` script. The safe alternative is to pass the value through an `env:` variable and reference it as `"$ACTION_PATH"` in the shell.

Locations:

- `action.yml:57`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed the 'Install Skylos' step in action.yml (line 57): moved `${{ github.action_path }}` out of the `run:` shell string into an `env:` block as `ACTION_PATH: ${{ github.action_path }}`, and updated the shell command to reference it as `"$ACTION_PATH"`. This prevents the template engine from substituting the value directly into the shell command string.

