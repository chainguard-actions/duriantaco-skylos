<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.41.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.41.0** was hardened automatically. 2 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): The 'Install Skylos' step directly interpolates `${{ github.action_path }}` inside a `run:` shell command string: `run: python -m pip install "${{ github.action_path }}"`.

Any `${{ ... }}` expression interpolated directly into a `run:` block is a script-injection risk because the value is substituted into the shell command before the shell parses it. The safe pattern is to pass the value via an `env:` variable and reference it as `"$ENV_VAR"` in the script.

Locations:

- `action.yml:116`

### script-injection (severity: high)

Sub-rule (b): The 'Run Skylos Scan' step builds a `$FLAGS` variable from `$SKYLOS_ANALYSIS` (which is set from `inputs.analysis`, a caller-controlled input) and then expands it **unquoted** in the shell command:

```
python -m skylos.cli "$SKYLOS_PATH" \
  --confidence "$SKYLOS_CONFIDENCE" \
  $FLAGS \
  "${SARIF_ARGS[@]}" \
  --json > "$REPORT"
```

An unquoted `$FLAGS` allows the shell to perform word-splitting and glob expansion on the value, enabling an attacker who controls `inputs.analysis` to inject arbitrary shell arguments or metacharacters. The variable should be quoted (`"$FLAGS"`) or the flags should be accumulated in an array and expanded as `"${FLAGS[@]}"`.

The same pattern also appears in the 'Upload to Skylos Dashboard' step.

Locations:

- `action.yml:175`
- `action.yml:220`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed all three script-injection findings in hardened/action/action.yml:
1. 'Install Skylos' step (line 116): Moved `${{ github.action_path }}` from the run: shell string into an env: variable `SKYLOS_ACTION_PATH`, referenced as `"$SKYLOS_ACTION_PATH"` in the shell command.
2. 'Run Skylos Scan' step (line 175): Converted FLAGS from a string variable with unquoted `$FLAGS` expansion to a bash array `FLAGS=()` with `FLAGS+=(--flag)` additions, expanded safely as `"${FLAGS[@]}"`. 
3. 'Upload to Skylos Dashboard' step (line 220): Same bash array conversion as above for the identical FLAGS pattern.

