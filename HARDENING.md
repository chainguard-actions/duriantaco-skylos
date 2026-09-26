<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.24.1

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.24.1** was hardened automatically. 1 finding(s) were identified and resolved across 2 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): The 'Install Skylos' step directly interpolates a ${{ github.action_path }} expression inside a run: shell command string: `run: python -m pip install "${{ github.action_path }}"`.

Any ${{ ... }} expression interpolated directly into a run: block is a script injection risk because the value is substituted into the shell command before the shell parses it. The safe alternative is to use the pre-set environment variable $GITHUB_ACTION_PATH instead, which avoids template substitution entirely.

Locations:

- `action.yml:57`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Replaced `${{ github.action_path }}` in the 'Install Skylos' step's run: block with the pre-set environment variable `$GITHUB_ACTION_PATH`. GitHub Actions automatically sets this variable to the same path, so the behavior is identical but the value is no longer template-substituted into the shell command string before parsing, eliminating the script injection risk.

### Iteration 2

**Fixes applied:** script-injection

**Notes:**

Fixed both occurrences of unquoted $FLAGS expansion in action.yml. In both the 'Run Skylos Scan' step (line 75) and 'Upload to Skylos Dashboard' step (line 103), converted FLAGS from a string variable to a bash array. Flags are now appended with FLAGS+=("--flag") and expanded safely with "${FLAGS[@]}", preventing word-splitting and glob expansion that could allow shell metacharacter injection via the inputs.analysis value.

