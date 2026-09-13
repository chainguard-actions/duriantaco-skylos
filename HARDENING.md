<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.37.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.37.0** was hardened automatically. 1 finding(s) were identified and resolved across 2 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a) violation: The 'Install Skylos' step directly interpolates a ${{ }} expression inside a run: shell command string. The line `run: python -m pip install "${{ github.action_path }}"` embeds `${{ github.action_path }}` directly in the shell command rather than routing it through an env: variable. Any ${{ ... }} expression directly inside a run: block is a script-injection risk regardless of which context it reads from.

Locations:

- `action.yml:55`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed the script injection vulnerability in the 'Install Skylos' step (action.yml line 55). Moved `${{ github.action_path }}` from the `run:` shell command into an `env:` block as `SKYLOS_ACTION_PATH`, and updated the shell command to reference `"$SKYLOS_ACTION_PATH"` instead. This eliminates the direct interpolation of a ${{ }} expression inside the run: shell string.

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed unquoted $FLAGS expansion in two steps ('Run Skylos Scan' at line 113 and 'Upload to Skylos Dashboard' at line 152) by converting the FLAGS string variable to a bash array. Changed `FLAGS=""` to `FLAGS=()`, changed `FLAGS="$FLAGS --flag"` to `FLAGS+=("--flag")`, and changed the unquoted `$FLAGS` expansion to `"${FLAGS[@]}"`  in both python command invocations. This eliminates word splitting and glob expansion risks from the caller-controlled `inputs.analysis` value.

