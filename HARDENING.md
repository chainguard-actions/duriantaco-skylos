<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v5.2.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v5.2.0** was hardened automatically. 2 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): a GitHub Actions expression is interpolated directly into a run: script in the 'Install Skylos' step: `run: python -m pip install "${{ github.action_path }}[dart]"`. Pass it through an env var instead (e.g. SKYLOS_ACTION_PATH: ${{ github.action_path }}) and use "${SKYLOS_ACTION_PATH}[dart]".

Locations:

- `action.yml:126`

### github-env-injection (severity: high)

The 'Run Skylos Image Scan' step writes `echo "report=$REPORT" >> "$GITHUB_OUTPUT"`. REPORT comes from the inherited process env var RUNNER_TEMP (through python tempfile.mkdtemp), which this script did not set, and the value is not sanitized with `printf '%s' ... | tr -d '\n\r'` before the write to GITHUB_OUTPUT.

Locations:

- `action.yml:147`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection, github-env-injection

**Notes:**

I fixed both findings in action.yml. Nothing has been run or re-scanned to confirm them.

1. **script-injection (Install Skylos step):** `${{ github.action_path }}` no longer appears inside the shell command. It now goes in through the step's `env:` block as `SKYLOS_ACTION_PATH`, and the command is `python -m pip install "${SKYLOS_ACTION_PATH}[dart]"`.

2. **github-env-injection (Run Skylos Image Scan step):** before the report path is written to `$GITHUB_OUTPUT`, line breaks are now removed with `printf '%s' "$REPORT" | tr -d '\n\r'` and the cleaned value is written instead. The scan itself still uses the original `$REPORT` path. The two values can only differ if `RUNNER_TEMP` contains a line break, so normal runs behave the same.

