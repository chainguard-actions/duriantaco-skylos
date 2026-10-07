<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.47.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.47.0** was hardened automatically. 2 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): The 'Install Skylos' step directly interpolates `${{ github.action_path }}` inside a `run:` shell command string: `run: python -m pip install "${{ github.action_path }}"`. Any `${{ ... }}` expression directly inside a `run:` block is a script-injection risk because the expression is substituted by the YAML template engine before the shell ever sees it, bypassing shell quoting.

Locations:

- `action.yml:126`

### script-injection (severity: high)

Sub-rule (b): The variable `$FLAGS` is expanded unquoted in two `run:` blocks. `$FLAGS` is built by appending strings derived from `$SKYLOS_ANALYSIS`, which is sourced from `inputs.analysis` (a workflow-controllable input). Unquoted expansion of `$FLAGS` in the `python -m skylos.cli` invocation allows shell metacharacters (`;`, `|`, `&`, `$(...)`, etc.) embedded in the input to be interpreted by the shell. Affected steps: 'Run Skylos Scan' (line ~163: `$FLAGS \`) and 'Upload to Skylos Dashboard' (line ~215: `$FLAGS \`). Fix: use an array to accumulate flags and expand it as `"${FLAGS[@]}"`  or quote `"$FLAGS"`.

Locations:

- `action.yml:163`
- `action.yml:215`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed three script-injection issues in action.yml: (1) Moved `${{ github.action_path }}` from the 'Install Skylos' run: shell string into an env: block as SKYLOS_ACTION_PATH, referenced safely as "$SKYLOS_ACTION_PATH". (2) Converted FLAGS from an unquoted string variable to a bash array in the 'Run Skylos Scan' step, using FLAGS+=() to append flags and "${FLAGS[@]}" for safe expansion. (3) Same array conversion applied to the 'Upload to Skylos Dashboard' step, including proper quoting of the --verify-model argument as a separate array element.

