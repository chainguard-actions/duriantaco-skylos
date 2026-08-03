<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.31.1

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.31.1** was hardened automatically. 1 finding(s) were identified and resolved across 2 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): The 'Install Skylos' step directly interpolates `${{ github.action_path }}` inside a `run:` shell command string: `run: python -m pip install "${{ github.action_path }}"`.

Any `${{ ... }}` expression interpolated directly into a `run:` block is a script-injection risk because the value is substituted into the shell command string before the shell parses it. The safe pattern is to pass the value via an `env:` variable and reference it as a quoted shell variable (e.g., `"$ACTION_PATH"`).

Fix example:
```yaml
- name: Install Skylos
  shell: bash
  env:
    ACTION_PATH: ${{ github.action_path }}
  run: python -m pip install "$ACTION_PATH"
```

Locations:

- `action.yml:55`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed script injection in the 'Install Skylos' step of action.yml (line 55). Moved `${{ github.action_path }}` out of the `run:` shell string and into an `env:` block as `ACTION_PATH`. The shell command now uses the quoted variable `"$ACTION_PATH"` instead of the direct expression interpolation.

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed unquoted `$FLAGS` expansion in two `run:` blocks in action.yml. Converted `FLAGS` from a string variable (with string concatenation and unquoted `$FLAGS` expansion) to a bash array (using `FLAGS=()`, `FLAGS+=(--flag)` appending, and `"${FLAGS[@]}"` expansion) in both the 'Run Skylos Scan' step and the 'Upload to Skylos Dashboard' step. This eliminates word splitting and glob expansion risks while correctly passing each flag as a separate shell argument.

