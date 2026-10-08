<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.47.2

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.47.2** was hardened automatically. 1 finding(s) were identified and resolved across 2 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a) violation: The 'Install Skylos' step interpolates `${{ github.action_path }}` directly inside a `run:` shell command string: `run: python -m pip install "${{ github.action_path }}[dart]"`. Any `${{ ... }}` expression directly inside a `run:` block is a script-injection risk because the value is substituted into the shell command string before the shell parses it. This should be moved to an `env:` variable and referenced as `"$ACTION_PATH"` instead.

Locations:

- `action.yml:76`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed the script injection vulnerability in the 'Install Skylos' step of action.yml. Moved `${{ github.action_path }}` from the `run:` shell command string into an `env:` block as `ACTION_PATH`, and updated the shell command to reference `"$ACTION_PATH"` instead of the inline expression.

### Iteration 2

**Fixes applied:** script-injection

**Notes:**

Fixed unquoted $FLAGS expansion in two 'run:' blocks by converting FLAGS from a string variable to a bash array. In both the 'Run Skylos Scan' and 'Upload to Skylos Dashboard' steps: (1) changed FLAGS="" to FLAGS=(), (2) changed FLAGS="$FLAGS --flag" to FLAGS+=(--flag) for each conditional flag, (3) changed unquoted $FLAGS to "${FLAGS[@]}" in the python command. In the upload step, also fixed FLAGS+=(--verify-model "$SKYLOS_VERIFY_MODEL_INPUT") to properly store the flag and its value as separate array elements with the value quoted.

