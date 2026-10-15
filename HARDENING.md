<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.50.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.50.0** was hardened automatically. 3 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): The 'Install Skylos' step directly interpolates `${{ github.action_path }}` inside a `run:` shell command string: `run: python -m pip install "${{ github.action_path }}[dart]"`. Any `${{ ... }}` expression interpolated directly into a `run:` block is a script-injection risk because the value is substituted by the YAML template engine before the shell ever sees it, bypassing shell quoting.

Locations:

- `action.yml:125`

### script-injection (severity: high)

Sub-rule (b): The 'Run Skylos Scan' step expands `$FLAGS` unquoted in the shell command `python -m skylos.cli "$SKYLOS_PATH" --confidence "$SKYLOS_CONFIDENCE" $FLAGS ...`. `$FLAGS` is constructed from `$SKYLOS_ANALYSIS`, which is sourced from `inputs.analysis` (attacker-controllable). An unquoted expansion allows the shell to parse metacharacters (`;`, `|`, `&`, `$(...)`, whitespace, glob chars) out of the value, enabling command injection.

Locations:

- `action.yml:175`

### script-injection (severity: high)

Sub-rule (b): The 'Upload to Skylos Dashboard' step expands `$FLAGS` unquoted in the shell command `python -m skylos.cli "$SKYLOS_PATH" --confidence "$SKYLOS_CONFIDENCE" $FLAGS --upload`. `$FLAGS` is constructed from `$SKYLOS_ANALYSIS` (inputs.analysis, attacker-controllable) and may also include `$SKYLOS_VERIFY_MODEL_INPUT` (inputs.verify-model). An unquoted expansion allows the shell to parse metacharacters out of the value, enabling command injection.

Locations:

- `action.yml:230`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed all three script-injection findings in action.yml:
1. 'Install Skylos' step (line 125): Moved `${{ github.action_path }}` into an `env:` block as `SKYLOS_ACTION_PATH` and referenced it as `"${SKYLOS_ACTION_PATH}[dart]"` in the shell command.
2. 'Run Skylos Scan' step (line 175): Converted `FLAGS` from an unquoted string to a bash array (`FLAGS=()`), appending flags with `FLAGS+=(--flag)` and expanding with `"${FLAGS[@]}"` instead of unquoted `$FLAGS`.
3. 'Upload to Skylos Dashboard' step (line 230): Same bash array conversion, including properly quoting `--verify-model "$SKYLOS_VERIFY_MODEL_INPUT"` as separate array elements.

