<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.22.1

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.22.1** was hardened automatically. 3 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Rule (a) violation: The 'Install Skylos' step directly interpolates `${{ github.action_path }}` inside a `run:` shell command string: `run: python -m pip install "${{ github.action_path }}"`. Any `${{ ... }}` expression inside a `run:` block is a script-injection risk because the value is substituted into the shell command before the shell parses it.

Locations:

- `action.yml:59`

### script-injection (severity: high)

Rule (b) violation: In the 'Run Skylos Scan' step, the shell variable `$FLAGS` is expanded **unquoted** in the `python -m skylos.cli` invocation (`$FLAGS \`). `$FLAGS` is built from `$SKYLOS_ANALYSIS`, which is sourced from `inputs.analysis` (a workflow-controllable input). An unquoted expansion allows shell metacharacter injection (`;`, `|`, `&`, `$(...)`, etc.) if the input contains such characters.

Locations:

- `action.yml:88`

### script-injection (severity: high)

Rule (b) violation: In the 'Upload to Skylos Dashboard' step, the shell variable `$FLAGS` is expanded **unquoted** in the `python -m skylos.cli` invocation (`$FLAGS \`). `$FLAGS` is built from `$SKYLOS_ANALYSIS`, which is sourced from `inputs.analysis` (a workflow-controllable input). An unquoted expansion allows shell metacharacter injection.

Locations:

- `action.yml:124`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed all three script-injection findings in hardened/action/action.yml:
1. 'Install Skylos' step (line 59): Moved `${{ github.action_path }}` to an env var `ACTION_PATH` and referenced it as `"$ACTION_PATH"` in the run command.
2. 'Run Skylos Scan' step (line 88): Converted string-based `FLAGS` variable to a bash array (`FLAGS=()`), using `FLAGS+=("--flag")` for additions and `"${FLAGS[@]}"` for safe quoted expansion, eliminating the unquoted `$FLAGS` shell metacharacter injection risk.
3. 'Upload to Skylos Dashboard' step (line 124): Same bash array fix applied as in finding 2.

