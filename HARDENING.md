<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.24.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.24.0** was hardened automatically. 3 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): The 'Install Skylos' step directly interpolates `${{ github.action_path }}` inside a `run:` shell command string: `run: python -m pip install "${{ github.action_path }}"`. Any `${{ ... }}` expression directly inside a `run:` block is a script-injection risk because the value is substituted into the shell command before the shell parses it.

Locations:

- `action.yml:59`

### script-injection (severity: high)

Sub-rule (b): The 'Run Skylos Scan' step uses unquoted `$FLAGS` in the command invocation (`$FLAGS \`). `FLAGS` is built from `$SKYLOS_ANALYSIS`, which is sourced from `inputs.analysis` (an untrusted caller-controlled input). An unquoted shell variable expansion allows shell metacharacters (`;`, `|`, `&`, `$(...)`, etc.) embedded in the input to be interpreted by the shell, enabling command injection.

Locations:

- `action.yml:88`

### script-injection (severity: high)

Sub-rule (b): The 'Upload to Skylos Dashboard' step uses unquoted `$FLAGS` in the command invocation (`$FLAGS \`). `FLAGS` is built from `$SKYLOS_ANALYSIS`, which is sourced from `inputs.analysis` (an untrusted caller-controlled input). An unquoted shell variable expansion allows shell metacharacters embedded in the input to be interpreted by the shell, enabling command injection.

Locations:

- `action.yml:124`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed all three script-injection findings in hardened/action/action.yml:
1. Line 59 (Install Skylos): Moved `${{ github.action_path }}` into an `env:` block as `ACTION_PATH` and referenced it as `"$ACTION_PATH"` in the run command.
2. Line 88 (Run Skylos Scan): Converted string-based `FLAGS` variable to a bash array (`FLAGS=()`), using `FLAGS+=("--flag")` for appending and `"${FLAGS[@]}"` for safe quoted expansion, eliminating the unquoted `$FLAGS` expansion.
3. Line 124 (Upload to Skylos Dashboard): Applied the same bash array pattern for `FLAGS` in the upload step.

