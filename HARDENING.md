<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.45.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.45.0** was hardened automatically. 2 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): The 'Install Skylos' step directly interpolates `${{ github.action_path }}` inside the `run:` shell command string: `python -m pip install "${{ github.action_path }}"`. Any `${{ ... }}` expression inside a `run:` block is a script-injection risk because the expression is substituted by the Actions template engine before the shell ever sees it, bypassing shell quoting. The value should be passed via an `env:` variable and referenced as `"$ENV_VAR"` instead.

Locations:

- `action.yml:83`

### script-injection (severity: high)

Sub-rule (b): In the 'Run Skylos Scan' step and the 'Upload to Skylos Dashboard' step, the shell variable `$FLAGS` is expanded **unquoted** in the `python -m skylos.cli` invocation (e.g. `python -m skylos.cli "$SKYLOS_PATH" --confidence "$SKYLOS_CONFIDENCE" $FLAGS ...`). `$FLAGS` is constructed by appending strings derived from `$SKYLOS_ANALYSIS`, which is sourced from the user-controlled `inputs.analysis` input. An unquoted expansion allows the shell to perform word splitting and interpret metacharacters (`;`, `|`, `&`, `$(...)`, etc.) embedded in the input value, enabling command injection. `$FLAGS` should be replaced with an array (e.g. `FLAGS=(); FLAGS+=(--danger)`) and expanded as `"${FLAGS[@]}"`.

Offending lines:
- Run Skylos Scan step: `$FLAGS \` (unquoted)
- Upload to Skylos Dashboard step: `$FLAGS \` (unquoted)

Locations:

- `action.yml:163`
- `action.yml:207`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed three script-injection issues in hardened/action/action.yml:
1. 'Install Skylos' step (line 83): Moved `${{ github.action_path }}` into an `env:` block as `SKYLOS_ACTION_PATH` and referenced it as `"$SKYLOS_ACTION_PATH"` in the run command.
2. 'Run Skylos Scan' step (line 163): Converted `FLAGS` string variable to a bash array (`FLAGS=()`), appending flags with `FLAGS+=(--flag)` and expanding safely as `"${FLAGS[@]}"`.
3. 'Upload to Skylos Dashboard' step (line 207): Same bash array conversion, including the `--verify-model` flag which now correctly passes the model name as a separate quoted argument via `FLAGS+=(--verify-model "$SKYLOS_VERIFY_MODEL_INPUT")`.

