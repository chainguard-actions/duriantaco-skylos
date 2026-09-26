<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.31.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.31.0** was hardened automatically. 1 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Rule (a) violation: The 'Install Skylos' step directly interpolates `${{ github.action_path }}` inside a `run:` shell command string. Any `${{ ... }}` expression inside a `run:` block flows through YAML template substitution before the shell sees it, making it a script-injection risk. The offending line is: `run: python -m pip install "${{ github.action_path }}"`

Fix: Use the `$GITHUB_ACTION_PATH` environment variable instead, which is automatically set by the runner and does not require template interpolation: `run: python -m pip install "$GITHUB_ACTION_PATH"`

Locations:

- `action.yml:56`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed the script-injection vulnerability in hardened/action/action.yml at line 56. Replaced `python -m pip install "${{ github.action_path }}"` with `python -m pip install "$GITHUB_ACTION_PATH"`. The `$GITHUB_ACTION_PATH` environment variable is automatically set by the GitHub Actions runner and provides the same value without going through YAML template substitution, eliminating the injection risk.

