<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v5.5.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v5.5.0** was hardened automatically. 2 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Rule (a): the 'Install Skylos' step puts a GitHub expression directly inside a run: script: `run: python -m pip install "${{ github.action_path }}[dart]"`. Pass github.action_path through an env: variable, e.g. SKYLOS_ACTION_PATH, and use "${SKYLOS_ACTION_PATH}[dart]" instead.

Locations:

- `action.yml:120`

### script-injection (severity: high)

Rule (b): the 'Upload to Skylos Dashboard' step adds workflow-controlled input to a string and expands it unquoted. The code is `FLAGS="$FLAGS --verify-model $SKYLOS_VERIFY_MODEL_INPUT"`, then `$FLAGS \` is passed unquoted to `python -m skylos.cli`. SKYLOS_VERIFY_MODEL_INPUT comes from inputs.verify-model. A regex allowlist (^[A-Za-z0-9._:/-]{1,100}$) limits the risk, but the check still requires workflow data to be expanded quoted. Build the flags as a bash array (FLAGS+=(--verify-model "$SKYLOS_VERIFY_MODEL_INPUT")) and expand it as "${FLAGS[@]}".

Locations:

- `action.yml:306`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed both script-injection findings in action.yml. Nothing has been run or re-scanned yet.

1. 'Install Skylos' step: `github.action_path` is now passed in through `env:` as `SKYLOS_ACTION_PATH`, and the step runs `python -m pip install "${SKYLOS_ACTION_PATH}[dart]"`.

2. 'Upload to Skylos Dashboard' step: the flags that were joined into one string are now a bash array. `--verify-model` and its value go in as separate entries, with the value double-quoted. The array is expanded as `${FLAGS[@]+"${FLAGS[@]}"}`, so an empty array is still safe on bash 3.2 (macOS). The verify-model allowlist check is unchanged.

I left the 'Run Skylos Scan' step's unquoted `$FLAGS` as it was. It only ever holds fixed flag names written in the action itself, and it wasn't flagged.

