<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.47.1

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.47.1** was hardened automatically. 2 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): The 'Install Skylos' step directly interpolates `${{ github.action_path }}` inside a `run:` shell command string: `run: python -m pip install "${{ github.action_path }}"`.

Any `${{ ... }}` expression directly inside a `run:` script is a script-injection finding — the value is substituted by the Actions template engine before the shell ever sees it, bypassing shell quoting. The fix is to pass the value via an `env:` variable and reference `"$SKYLOS_ACTION_PATH"` in the script (as is already done in the 'Build Skylos Go engine' step above it).

Locations:

- `action.yml:76`

### script-injection (severity: high)

Sub-rule (b): The 'Run Skylos Scan' step uses the `$FLAGS` variable **unquoted** in the shell command:

```
python -m skylos.cli "$SKYLOS_PATH" \
  --confidence "$SKYLOS_CONFIDENCE" \
  $FLAGS \
  "${SARIF_ARGS[@]}" \
  --json > "$REPORT"
```

`FLAGS` is built by appending fixed strings based on `$SKYLOS_ANALYSIS`, which is sourced from `inputs.analysis` (caller-controlled). An attacker who controls `inputs.analysis` can inject shell metacharacters (`;`, `|`, `&`, `$(...)`, etc.) through `$FLAGS` because it is expanded without double-quoting. The fix is to use an array (`FLAGS_ARRAY=()`) and expand it as `"${FLAGS_ARRAY[@]}"`.

Same pattern also appears in the 'Upload to Skylos Dashboard' step (see second location).

Locations:

- `action.yml:130`
- `action.yml:175`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed all three script-injection instances in action.yml:
1. 'Install Skylos' step (line 76): Moved `${{ github.action_path }}` into an `env:` variable `SKYLOS_ACTION_PATH` and referenced it as `"$SKYLOS_ACTION_PATH"` in the run command.
2. 'Run Skylos Scan' step (line 130): Replaced the unquoted `$FLAGS` string variable with a `FLAGS_ARRAY=()` bash array, appending flags with `FLAGS_ARRAY+=(--flag)` and expanding with `"${FLAGS_ARRAY[@]}"` (properly quoted).
3. 'Upload to Skylos Dashboard' step (line 175): Same FLAGS_ARRAY conversion, including properly separating `--verify-model` and `"$SKYLOS_VERIFY_MODEL_INPUT"` as distinct array elements to avoid the single-word trap.

