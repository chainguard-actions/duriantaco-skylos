<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.33.1

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.33.1** was hardened automatically. 1 finding(s) were identified and resolved across 2 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a) violation: The 'Install Skylos' step directly interpolates a `${{ }}` expression inside a `run:` shell command string. The offending line is: `run: python -m pip install "${{ github.action_path }}"`

Any `${{ ... }}` expression interpolated directly into a `run:` block is a script-injection risk because the value is substituted by the GitHub Actions template engine before the shell ever sees it, bypassing shell quoting. The correct pattern is to assign the value to an `env:` variable and reference that variable in the script (as is already done correctly in the adjacent 'Build Skylos Go engine' step with `SKYLOS_ACTION_PATH: ${{ github.action_path }}`).

Locations:

- `action.yml:96`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed the script injection vulnerability in the 'Install Skylos' step (action.yml line 96). Moved `${{ github.action_path }}` from the `run:` shell command string into an `env:` block as `SKYLOS_ACTION_PATH: ${{ github.action_path }}`, and updated the run command to reference it as `"$SKYLOS_ACTION_PATH"`. This follows the same pattern already used correctly in the adjacent 'Build Skylos Go engine' step.

### Iteration 2

**Fixes applied:** script-injection

**Notes:**

Fixed script injection in two locations in action.yml (lines 107 and 148). In both the 'Run Skylos Scan' and 'Upload to Skylos Dashboard' steps, converted the $FLAGS string variable (built from $SKYLOS_ANALYSIS / inputs.analysis) to a bash array. Changed `FLAGS=""` to `FLAGS=()`, changed `FLAGS="$FLAGS --flag"` to `FLAGS+=("--flag")` for each conditional, and changed the unquoted `$FLAGS` expansion to `"${FLAGS[@]}"`. This ensures each flag is a separate, properly quoted argument and prevents shell metacharacters in inputs.analysis from being interpreted as shell commands.

