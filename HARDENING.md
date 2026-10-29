<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v5.1.5

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v5.1.5** was hardened automatically. 2 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): a GitHub Actions expression is pasted straight into the run: script of the 'Install Skylos' step: `run: python -m pip install "${{ github.action_path }}[dart]"`. Pass it through an env: variable instead (for example SKYLOS_ACTION_PATH: ${{ github.action_path }}) and use `python -m pip install "${SKYLOS_ACTION_PATH}[dart]"`.

Locations:

- `action.yml:126`

### github-env-injection (severity: high)

The 'Run Skylos Image Scan' step builds REPORT from REPORT_DIR, which comes from the inherited process env var RUNNER_TEMP. Nothing in the same script sets RUNNER_TEMP. REPORT is then written to $GITHUB_OUTPUT with `echo "report=$REPORT" >> "$GITHUB_OUTPUT"` and no `printf '%s' "$REPORT" | tr -d '\n\r'` step first. The check treats any env var a composite action inherits as untrusted. Strip newlines from the value before writing it.

Locations:

- `action.yml:147`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection, github-env-injection

**Notes:**

Both findings are fixed in action.yml. Nothing was run to test the changes.

- **script-injection (Install Skylos step):** `github.action_path` is now passed in through the step's `env:` block as `SKYLOS_ACTION_PATH`. The install command reads it as `python -m pip install "${SKYLOS_ACTION_PATH}[dart]"` instead of having the expression pasted into the script.
- **github-env-injection (Run Skylos Image Scan step):** newlines and carriage returns are now stripped from `REPORT` (`printf '%s' "$REPORT" | tr -d '\n\r'`) before it is written as `report=` to `$GITHUB_OUTPUT`. The script still uses the original `REPORT` value for the scan's output path and later file checks, so the report goes where it did before.

The only behaviour change is when the `RUNNER_TEMP` path itself contains a newline, which normally never happens. In that case the `report` output path would no longer match the real file, and the image report upload step would not find it.

