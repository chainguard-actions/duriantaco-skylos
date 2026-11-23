<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v5.8.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v5.8.0** was hardened automatically. 2 finding(s) were identified and resolved across 2 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Rule (a): the 'Install Skylos' step puts a GitHub expression straight into a run: script: `run: python -m pip install "${{ github.action_path }}[dart]"`. Fix: move the value into an env: variable (e.g. SKYLOS_ACTION_PATH: ${{ github.action_path }}) and use it as "${SKYLOS_ACTION_PATH}[dart]", or use the $GITHUB_ACTION_PATH environment variable that the runner already sets.

Locations:

- `action.yml:127`

### github-env-injection (severity: high)

The 'Run Skylos Scan' step writes `echo "diff_base=$BASE" >> "$GITHUB_OUTPUT"`. BASE is built from the inherited GITHUB_BASE_REF env var (github.base_ref). Before the write, the value is only checked with the regex ^[A-Za-z0-9._/-]+$. That regex probably already blocks newlines, but the required step `printf '%s' "$BASE" | tr -d '\n\r'` is missing right before the write. Add it, and write the cleaned value instead.

Locations:

- `action.yml:249`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection, github-env-injection

**Notes:**

Fixed both findings in action.yml:
1. Script injection in the 'Install Skylos' step. github.action_path is now passed in through the SKYLOS_ACTION_PATH env var and the script uses "${SKYLOS_ACTION_PATH}[dart]".
2. Output injection in the 'Run Skylos Scan' step. BASE now goes through printf '%s' | tr -d '\n\r', and the cleaned value is what gets written to diff_base in $GITHUB_OUTPUT.
Nothing was run to test these changes.

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

In action.yml's 'Upload to Skylos Dashboard' step, FLAGS is now a bash array instead of a flat string. The verify-model value is added with FLAGS+=(--verify-model "$SKYLOS_VERIFY_MODEL_INPUT"), and the array is expanded as "${FLAGS[@]}". The regex check on verify-model is unchanged. The scan step's FLAGS string was not touched: it only holds fixed flag text and the finding did not mention it. The change has not been run or tested.

