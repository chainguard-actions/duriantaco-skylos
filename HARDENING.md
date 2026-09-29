<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.42.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.42.0** was hardened automatically. 1 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): The 'Install Skylos' step interpolates `${{ github.action_path }}` directly inside a `run:` shell command string: `run: python -m pip install "${{ github.action_path }}"`.

Per the check rules, ANY `${{ ... }}` expression directly inside a `run:` script is a script-injection finding regardless of which context it reads from. The value flows through YAML template substitution before the shell ever quotes it. The safe pattern is to route it through an `env:` variable and reference that variable (e.g., `env: ACTION_PATH: ${{ github.action_path }}` then `run: python -m pip install "$ACTION_PATH"`).

Offending line: `run: python -m pip install "${{ github.action_path }}"`

Locations:

- `action.yml:72`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed the 'Install Skylos' step in action.yml: moved `${{ github.action_path }}` from the `run:` shell command string into an `env:` block as `ACTION_PATH: ${{ github.action_path }}`, then updated the shell command to reference it as `python -m pip install "$ACTION_PATH"`. This eliminates the script-injection risk by routing the expression through an environment variable instead of direct YAML template substitution into the shell command.

