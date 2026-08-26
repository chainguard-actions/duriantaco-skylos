<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.35.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.35.0** was hardened automatically. 1 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): The 'Install Skylos' step directly interpolates `${{ github.action_path }}` inside a `run:` shell command string: `run: python -m pip install "${{ github.action_path }}"`.

Any `${{ ... }}` expression directly inside a `run:` script is a script-injection risk — the expression is substituted by the YAML template engine before the shell ever sees it, bypassing shell quoting. The value should be passed via an `env:` variable and referenced as `"$ENV_VAR"` instead.

Sub-rule (b): In both the 'Run Skylos Scan' step and the 'Upload to Skylos Dashboard' step, the `$FLAGS` variable (built from `$SKYLOS_ANALYSIS`, which is sourced from `inputs.analysis`) is expanded unquoted in the shell command:
```
python -m skylos.cli "$SKYLOS_PATH" \
  --confidence "$SKYLOS_CONFIDENCE" \
  $FLAGS \
  --json > "$REPORT"
```
An unquoted shell variable expansion allows the shell to parse metacharacters (`;`, `|`, `&`, `$(...)`, whitespace, glob chars) out of the value. `$FLAGS` should be double-quoted: `"$FLAGS"`.

Locations:

- `action.yml:87`
- `action.yml:107`
- `action.yml:147`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed three script-injection issues in action.yml:
1. 'Install Skylos' step: moved `${{ github.action_path }}` out of the run: shell string into an env: variable `SKYLOS_ACTION_PATH`, referenced as `"$SKYLOS_ACTION_PATH"` in the shell command.
2. 'Run Skylos Scan' step: converted `FLAGS` from an unquoted string variable to a bash array (`FLAGS=()`), populated with `FLAGS+=("--flag")` conditionals, and expanded safely as `"${FLAGS[@]}"` in the python command.
3. 'Upload to Skylos Dashboard' step: same bash array treatment applied to `FLAGS` for the upload command.

