<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.50.1

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.50.1** was hardened automatically. 3 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): A ${{ }} expression is directly interpolated inside a run: shell command string. The 'Install Skylos' step uses `run: python -m pip install "${{ github.action_path }}[dart]"`. Any ${{ ... }} expression directly inside a run: script is a script-injection finding regardless of which context it reads from. The value should be passed via an env: variable instead.

Locations:

- `action.yml:126`

### script-injection (severity: high)

Sub-rule (b): The 'Run Skylos Scan' step builds a FLAGS variable from $SKYLOS_ANALYSIS (sourced from inputs.analysis, which is user-controlled) and then expands it unquoted as `$FLAGS` in the python command invocation: `python -m skylos.cli "$SKYLOS_PATH" \ --confidence "$SKYLOS_CONFIDENCE" \ $FLAGS \ ...`. An unquoted shell variable expansion of untrusted data allows shell metacharacter injection (word splitting, glob expansion, etc.).

Locations:

- `action.yml:255`

### script-injection (severity: high)

Sub-rule (b): The 'Upload to Skylos Dashboard' step has the same unquoted $FLAGS pattern as the 'Run Skylos Scan' step. FLAGS is built from $SKYLOS_ANALYSIS (sourced from inputs.analysis) and expanded unquoted in `python -m skylos.cli "$SKYLOS_PATH" \ --confidence "$SKYLOS_CONFIDENCE" \ $FLAGS \ --upload`. Unquoted expansion of a variable derived from user-controlled input allows shell metacharacter injection.

Locations:

- `action.yml:315`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed all three script-injection findings in hardened/action/action.yml:
1. 'Install Skylos' step (line 126): Moved `${{ github.action_path }}` into an env: block as SKYLOS_ACTION_PATH and referenced it as `${SKYLOS_ACTION_PATH}` in the shell command.
2. 'Run Skylos Scan' step (line 255): Converted FLAGS from an unquoted string variable to a bash array (FLAGS=()), appending flags with FLAGS+=(--flag) and expanding with "${FLAGS[@]}" to prevent word-splitting/glob injection.
3. 'Upload to Skylos Dashboard' step (line 315): Same bash array fix applied; also fixed `--verify-model $SKYLOS_VERIFY_MODEL_INPUT` to use `FLAGS+=(--verify-model "$SKYLOS_VERIFY_MODEL_INPUT")` keeping the value and flag as separate properly-quoted array elements.

