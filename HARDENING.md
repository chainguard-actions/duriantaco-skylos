<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.28.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.28.0** was hardened automatically. 3 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Rule (a): The 'Install Skylos' step directly interpolates `${{ github.action_path }}` inside a `run:` shell command string: `run: python -m pip install "${{ github.action_path }}"`  Any ${{ ... }} expression interpolated directly into a run: block is a script-injection risk because the value is substituted by the YAML template engine before the shell ever sees it, bypassing shell quoting.

Locations:

- `action.yml:57`

### script-injection (severity: high)

Rule (b): In the 'Run Skylos Scan' step, the shell variable `$FLAGS` is expanded unquoted in the command `python -m skylos.cli "$SKYLOS_PATH" --confidence "$SKYLOS_CONFIDENCE" $FLAGS --json`. `$FLAGS` is built from `$SKYLOS_ANALYSIS`, which is sourced from `inputs.analysis` (attacker-controllable). Unquoted expansion allows shell metacharacters (`;`, `|`, `&`, `$(...)`, etc.) embedded in the input to be interpreted by the shell, enabling command injection.

Locations:

- `action.yml:83`

### script-injection (severity: high)

Rule (b): In the 'Upload to Skylos Dashboard' step, the shell variable `$FLAGS` is expanded unquoted in the command `python -m skylos.cli "$SKYLOS_PATH" --confidence "$SKYLOS_CONFIDENCE" $FLAGS --upload`. `$FLAGS` is built from `$SKYLOS_ANALYSIS`, which is sourced from `inputs.analysis` (attacker-controllable). Unquoted expansion allows shell metacharacters embedded in the input to be interpreted by the shell, enabling command injection.

Locations:

- `action.yml:107`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed all three script-injection findings in action.yml:
1. 'Install Skylos' step (line 57): Moved `${{ github.action_path }}` into an env var `ACTION_PATH` and referenced it as `"$ACTION_PATH"` in the run command.
2. 'Run Skylos Scan' step (line 83): Converted `FLAGS` from a string to a bash array (`FLAGS=()`), appending elements with `FLAGS+=("--flag")`, and expanded safely with `"${FLAGS[@]}"` instead of unquoted `$FLAGS`.
3. 'Upload to Skylos Dashboard' step (line 107): Same bash array fix applied to the FLAGS variable in the upload step.

