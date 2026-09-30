<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.43.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.43.0** was hardened automatically. 1 finding(s) were identified and resolved across 2 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): The 'Install Skylos' step interpolates `${{ github.action_path }}` directly inside a `run:` shell command string: `run: python -m pip install "${{ github.action_path }}". Any ${{ ... }} expression directly inside a run: block is a script-injection risk because the value is substituted into the shell command before the shell parses it. The safe pattern is to assign the value to an env: variable and reference that variable in the run: script instead.

Locations:

- `action.yml:96`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed the 'Install Skylos' step in action.yml (line 96): moved `${{ github.action_path }}` from the `run:` shell command string into an `env:` block as `SKYLOS_ACTION_PATH`, and updated the run command to reference `"$SKYLOS_ACTION_PATH"` instead. This eliminates the script-injection risk by ensuring the expression value is assigned to an environment variable before the shell parses the command.

### Iteration 2

**Fixes applied:** script-injection

**Notes:**

Fixed unquoted $FLAGS shell variable expansion in two run: blocks in action.yml. In both the 'Run Skylos Scan' step and the 'Upload to Skylos Dashboard' step, converted FLAGS from a string variable (FLAGS="" / FLAGS="$FLAGS --flag" / $FLAGS) to a bash array (FLAGS=() / FLAGS+=(--flag) / "${FLAGS[@]}"). In the upload step, also fixed the --verify-model argument to use FLAGS+=(--verify-model "$SKYLOS_VERIFY_MODEL_INPUT") so the flag and its value are separate properly-quoted array elements. These changes prevent injection of shell metacharacters through the inputs.analysis and inputs.verify-model inputs.

