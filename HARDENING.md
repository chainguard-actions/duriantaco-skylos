<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.49.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.49.0** was hardened automatically. 1 finding(s) were identified and resolved across 2 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): The 'Install Skylos' step interpolates `${{ github.action_path }}` directly inside a `run:` shell command string: `run: python -m pip install "${{ github.action_path }}[dart]"`. Any `${{ ... }}` expression directly inside a `run:` block is a script-injection risk because the value is substituted into the shell command string before the shell parses it. The correct pattern (already used in the adjacent 'Build Skylos Go engine' step) is to assign the value to an `env:` variable (e.g. `SKYLOS_ACTION_PATH: ${{ github.action_path }}`) and then reference it as `"$SKYLOS_ACTION_PATH"` inside the run block.

Locations:

- `action.yml:100`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed the 'Install Skylos' step in action.yml: moved `${{ github.action_path }}` from the `run:` shell command string into an `env:` variable (`SKYLOS_ACTION_PATH: ${{ github.action_path }}`), then referenced it as `"$SKYLOS_ACTION_PATH[dart]"` in the run block. This matches the pattern already used in the adjacent 'Build Skylos Go engine' step.

### Iteration 2

**Fixes applied:** script-injection

**Notes:**

Fixed unquoted $FLAGS expansion in two steps of action.yml:
1. 'Run Skylos Scan' step: Changed FLAGS from a string variable to a bash array (FLAGS=() with FLAGS+=(--flag) appends), and expanded it as "${FLAGS[@]}" instead of unquoted $FLAGS.
2. 'Upload to Skylos Dashboard' step: Same array conversion, plus fixed the --verify-model flag to use FLAGS+=(--verify-model "$SKYLOS_VERIFY_MODEL_INPUT") so the flag and its value are separate array elements rather than concatenated into one string.
This prevents word splitting and glob expansion on workflow-controllable data from inputs.analysis and inputs.verify-model.

