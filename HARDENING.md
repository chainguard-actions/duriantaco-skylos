<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.46.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.46.0** was hardened automatically. 1 finding(s) were identified and resolved across 2 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Rule (a) violation: The 'Install Skylos' step directly interpolates a ${{ }} expression inside a run: shell command string. The line `run: python -m pip install "${{ github.action_path }}"` embeds the github.action_path context value directly into the shell command via YAML template substitution before the shell ever sees it. Per the check rules, any ${{ ... }} expression directly inside a run: block is a script-injection finding, regardless of which context it reads from. The safe pattern is to assign the value to an env: variable and reference it as $ENV_VAR in the run: script.

Locations:

- `action.yml:111`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed the script-injection finding in the 'Install Skylos' step of action.yml. Moved the `${{ github.action_path }}` expression from the run: shell command into an env: block as `SKYLOS_ACTION_PATH: ${{ github.action_path }}`, and updated the run: command to reference it as `"$SKYLOS_ACTION_PATH"` instead of the direct template expression.

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed both script-injection findings in action.yml by converting the FLAGS string variable to a bash array in both the 'Run Skylos Scan' step and the 'Upload to Skylos Dashboard' step:

1. 'Run Skylos Scan' (line ~218): Changed `FLAGS=""` to `FLAGS=()`, replaced `FLAGS="$FLAGS --flag"` with `FLAGS+=(--flag)`, and replaced unquoted `$FLAGS` with `"${FLAGS[@]}"`.

2. 'Upload to Skylos Dashboard' (lines ~278, ~283): Same array conversion, plus fixed `FLAGS="$FLAGS --verify-model $SKYLOS_VERIFY_MODEL_INPUT"` to `FLAGS+=(--verify-model "$SKYLOS_VERIFY_MODEL_INPUT")` so the model name is properly quoted as a separate argument, and replaced unquoted `$FLAGS` with `"${FLAGS[@]}"`.

Both steps use `shell: bash`, so bash array syntax is valid. The fixes ensure each flag is a separate properly-quoted argument with no risk of shell metacharacter interpretation.

