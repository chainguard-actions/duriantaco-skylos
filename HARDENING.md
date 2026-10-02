<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.43.2

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.43.2** was hardened automatically. 1 finding(s) were identified and resolved across 2 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): The 'Install Skylos' step directly interpolates a GitHub Actions expression inside a `run:` shell command string. The line `run: python -m pip install "${{ github.action_path }}"` embeds `${{ github.action_path }}` (a `github.*` context value) directly into the shell command before the shell ever sees it. Any `${{ ... }}` expression inside a `run:` block is a script-injection risk because the value is substituted into the shell command string by the Actions runner before execution, bypassing shell quoting. The fix is to pass the value via an `env:` variable (e.g. `ACTION_PATH: ${{ github.action_path }}`) and reference it as `"$ACTION_PATH"` in the script.

Locations:

- `action.yml:91`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed the script injection vulnerability in the 'Install Skylos' step of action.yml. Moved `${{ github.action_path }}` from the `run:` shell command string into an `env:` block as `ACTION_PATH: ${{ github.action_path }}`, and updated the shell command to reference it as `"$ACTION_PATH"` instead of the inline expression.

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed script injection in two steps of action.yml:
1. 'Run Skylos Scan' step: Replaced string-based `FLAGS` variable (expanded unquoted as `$FLAGS`) with a bash array `FLAGS_ARRAY=()`. Each analysis flag is now appended with `FLAGS_ARRAY+=(--flag)` and expanded safely as `"${FLAGS_ARRAY[@]}"`.
2. 'Upload to Skylos Dashboard' step: Same fix applied. Additionally, the `--verify-model` flag and its value are now added as two separate array elements (`FLAGS_ARRAY+=(--verify-model "$SKYLOS_VERIFY_MODEL_INPUT")`), preventing the flag+value from being collapsed into a single argument.
Both fixes prevent an attacker who controls the `inputs.analysis` or `inputs.verify-model` inputs from injecting shell metacharacters into the python command.

