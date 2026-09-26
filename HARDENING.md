<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.29.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.29.0** was hardened automatically. 1 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Rule (a) violation: The 'Install Skylos' step directly interpolates `${{ github.action_path }}` inside a `run:` shell command string: `python -m pip install "${{ github.action_path }}"`.

Any `${{ ... }}` expression interpolated directly into a `run:` block is a script-injection risk because the value is substituted into the shell command string before the shell parses it. The safe alternative is to reference the pre-set environment variable `$GITHUB_ACTION_PATH` instead, which avoids template substitution entirely.

Locations:

- `action.yml:54`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed script injection in the 'Install Skylos' step (action.yml line 54): replaced `${{ github.action_path }}` with the pre-set environment variable `$GITHUB_ACTION_PATH`. GitHub Actions automatically sets this variable before executing the shell command, so no template substitution occurs in the shell string, eliminating the injection risk.

