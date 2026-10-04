<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.44.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.44.0** was hardened automatically. 1 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): The 'Install Skylos' step directly interpolates a `${{ ... }}` expression inside a `run:` shell command string. The line `run: python -m pip install "${{ github.action_path }}"` embeds `${{ github.action_path }}` directly into the shell command before the shell ever sees it. Per the check rules, ANY `${{ ... }}` expression directly inside a `run:` block is a script-injection finding, regardless of whether the specific context value is attacker-controlled. The value should instead be passed via an `env:` variable and referenced as `"$ENV_VAR"` in the script.

Locations:

- `action.yml:74`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed the 'Install Skylos' step in action.yml (line 74): moved `${{ github.action_path }}` out of the `run:` shell command and into an `env:` block as `ACTION_PATH`. The shell command now references it as `"$ACTION_PATH"` instead of directly interpolating the expression.

