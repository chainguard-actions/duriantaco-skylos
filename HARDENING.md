<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.43.1

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.43.1** was hardened automatically. 2 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Rule (a): The 'Install Skylos' step interpolates `${{ github.action_path }}` directly inside a `run:` shell command string: `run: python -m pip install "${{ github.action_path }}"`.

Any `${{ ... }}` expression inside a `run:` block is a script-injection risk because the value is substituted into the shell command string before the shell parses it. The safe pattern is to assign the value to an `env:` variable and reference that variable (double-quoted) in the script instead.

Locations:

- `action.yml:75`

### script-injection (severity: high)

Rule (b): In the 'Run Skylos Scan' step, the shell variable `$FLAGS` is expanded **unquoted** in the `python -m skylos.cli` invocation:

```
python -m skylos.cli "$SKYLOS_PATH" \
  --confidence "$SKYLOS_CONFIDENCE" \
  $FLAGS \
  "${SARIF_ARGS[@]}" \
  --json > "$REPORT"
```

`FLAGS` is built by appending strings derived from `$SKYLOS_ANALYSIS`, which holds the value of `inputs.analysis` (a workflow-controllable input). An unquoted `$FLAGS` allows the shell to word-split and glob-expand the value, enabling injection of arbitrary shell arguments or metacharacters. `$FLAGS` should be changed to an array and expanded as `"${FLAGS[@]}"`.

The same pattern appears in the 'Upload to Skylos Dashboard' step.

Locations:

- `action.yml:165`
- `action.yml:215`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed three script-injection issues in action.yml: (1) Moved `${{ github.action_path }}` in the 'Install Skylos' step from the run: shell string into an env: variable (SKYLOS_ACTION_PATH) and referenced it as "$SKYLOS_ACTION_PATH". (2) Converted FLAGS from a string variable (unquoted $FLAGS expansion) to a bash array in the 'Run Skylos Scan' step — built with FLAGS+=(...) and expanded as "${FLAGS[@]}". (3) Applied the same FLAGS array conversion to the 'Upload to Skylos Dashboard' step, including the --verify-model flag which now uses FLAGS+=(--verify-model "$SKYLOS_VERIFY_MODEL_INPUT") to keep the value properly quoted and as a separate argument.

