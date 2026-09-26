<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.24.2

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.24.2** was hardened automatically. 3 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): The 'Install Skylos' step interpolates `${{ github.action_path }}` directly inside a `run:` shell command string: `run: python -m pip install "${{ github.action_path }}"`.

Any `${{ ... }}` expression inside a `run:` block is a script-injection risk because the value is substituted by the Actions template engine before the shell ever sees it, bypassing shell quoting. The safe pattern is to pass the value via an `env:` variable and reference it as `"$ENV_VAR"` in the script.

Locations:

- `action.yml:59`

### script-injection (severity: high)

Sub-rule (b): The 'Run Skylos Scan' step uses `$FLAGS` unquoted in the shell command:

```
python -m skylos.cli "$SKYLOS_PATH" \
  --confidence "$SKYLOS_CONFIDENCE" \
  $FLAGS \
  --json > "$REPORT" || true
```

`FLAGS` is built by appending strings derived from `$SKYLOS_ANALYSIS`, which is sourced from `inputs.analysis` (a caller-controlled input). An unquoted `$FLAGS` allows the shell to parse metacharacters (`;`, `|`, `&`, `$(...)`, etc.) out of the value, enabling command injection. The fix is to use an array or quote the expansion: `"$FLAGS"`.

Locations:

- `action.yml:88`

### script-injection (severity: high)

Sub-rule (b): The 'Upload to Skylos Dashboard' step uses `$FLAGS` unquoted in the shell command:

```
python -m skylos.cli "$SKYLOS_PATH" \
  --confidence "$SKYLOS_CONFIDENCE" \
  $FLAGS \
  --upload || echo "Upload failed (non-fatal)"
```

Same issue as the 'Run Skylos Scan' step: `FLAGS` is built from `$SKYLOS_ANALYSIS` which comes from `inputs.analysis`, a caller-controlled input. Unquoted `$FLAGS` allows shell metacharacter injection.

Locations:

- `action.yml:124`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed all three script-injection findings in hardened/action/action.yml:
1. 'Install Skylos' step: moved `${{ github.action_path }}` to an `env:` block as `ACTION_PATH` and referenced it as `"$ACTION_PATH"` in the run command.
2. 'Run Skylos Scan' step: converted `FLAGS` string variable to a bash array (`FLAGS=()`), appending flags with `FLAGS+=("--flag")` and expanding safely with `"${FLAGS[@]}"` instead of unquoted `$FLAGS`.
3. 'Upload to Skylos Dashboard' step: same bash array fix as finding 2.

