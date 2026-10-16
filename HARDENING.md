<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.49.1

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.49.1** was hardened automatically. 2 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Rule (a): The 'Install Skylos' step directly interpolates `${{ github.action_path }}` inside a `run:` shell command string: `run: python -m pip install "${{ github.action_path }}[dart]"`. Any `${{ ... }}` expression inside a `run:` block is a script-injection risk because the value is substituted by the YAML template engine before the shell ever sees it, bypassing shell quoting.

Locations:

- `action.yml:96`

### script-injection (severity: high)

Rule (b): The `$FLAGS` variable is passed unquoted to `python -m skylos.cli` in both the 'Run Skylos Scan' step and the 'Upload to Skylos Dashboard' step. `FLAGS` is built by appending values derived from `inputs.analysis` (via `$SKYLOS_ANALYSIS`) and `inputs.verify-model` (via `$SKYLOS_VERIFY_MODEL_INPUT`), which are attacker-controllable. Unquoted expansion of `$FLAGS` allows shell word-splitting and metacharacter injection. Affected lines: `$FLAGS \` in the scan step and `$FLAGS \` in the upload step.

Locations:

- `action.yml:167`
- `action.yml:222`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Three script-injection issues fixed in action.yml:
1. 'Install Skylos' step (line 96): Moved `${{ github.action_path }}` out of the run: shell string into an env: block as SKYLOS_ACTION_PATH, referenced as $SKYLOS_ACTION_PATH in the shell command.
2. 'Run Skylos Scan' step (line 167): Converted FLAGS from an unquoted string variable to a bash array (FLAGS=()), appending flags with FLAGS+=("--flag") and expanding safely with "${FLAGS[@]}".
3. 'Upload to Skylos Dashboard' step (line 222): Same FLAGS array conversion, plus the --verify-model flag and its value are now added as two separate array elements to preserve argument boundaries.

