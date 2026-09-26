<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.27.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.27.0** was hardened automatically. 1 finding(s) were identified and resolved across 2 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): The 'Install Skylos' step directly interpolates `${{ github.action_path }}` inside a `run:` shell command string: `run: python -m pip install "${{ github.action_path }}"`.

Any `${{ ... }}` expression interpolated directly into a `run:` block is a script-injection risk because the value is substituted into the shell command string before the shell parses it. Even though `github.action_path` is typically controlled by GitHub, the rule requires that no `${{ }}` expression appear directly inside a `run:` script. The safe pattern is to pass the value via an `env:` variable and reference it as `"$ACTION_PATH"` in the shell script.

Locations:

- `action.yml:59`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed script injection in the 'Install Skylos' step of action.yml (line 59). Moved `${{ github.action_path }}` from the `run:` shell command string into an `env:` block as `ACTION_PATH`, then referenced it as `"$ACTION_PATH"` in the shell script. This prevents the expression from being interpolated directly into the shell command before parsing.

### Iteration 2

**Fixes applied:** script-injection

**Notes:**

Fixed unquoted $FLAGS expansion in two steps ('Run Skylos Scan' and 'Upload to Skylos Dashboard'). Changed FLAGS from a string variable to a bash array (FLAGS=() and FLAGS+=("--flag")), and replaced the unquoted $FLAGS expansion with the properly quoted "${FLAGS[@]}" array expansion. This prevents word-splitting and glob expansion while correctly passing each flag as a separate argument.

