<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.22.1

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.22.1** was hardened automatically. 1 finding(s) were identified and resolved across 2 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): The 'Install Skylos' step directly interpolates the GitHub Actions expression `${{ github.action_path }}` inside a `run:` shell command string. Any `${{ ... }}` expression interpolated directly into a `run:` block is a script-injection risk because the value is substituted into the shell command before the shell parses it. Offending line: `run: python -m pip install "${{ github.action_path }}"`

Locations:

- `action.yml:55`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed script injection in the 'Install Skylos' step (action.yml line 55): moved `${{ github.action_path }}` from the `run:` shell command string into the step's `env:` block as `ACTION_PATH`, and updated the shell command to reference it as `"$ACTION_PATH"` instead of `"${{ github.action_path }}"`.

### Iteration 2

**Fixes applied:** script-injection

**Notes:**

Fixed unquoted $FLAGS variable expansion in two steps ('Run Skylos Scan' at line 90 and 'Upload to Skylos Dashboard' at line 116). Changed FLAGS from a string variable to a bash array (FLAGS=()), with each flag appended as a separate element (FLAGS+=("--danger") etc.), and expanded safely with "${FLAGS[@]}". This prevents word splitting and glob expansion while correctly passing multiple flags as distinct arguments.

