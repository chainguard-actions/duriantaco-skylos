<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v5.0.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v5.0.0** was hardened automatically. 2 finding(s) were identified and resolved across 2 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): a GitHub Actions expression is placed directly inside a run: script in the 'Install Skylos' step: `run: python -m pip install "${{ github.action_path }}[dart]"`. Fix: map it to an env var (e.g. SKYLOS_ACTION_PATH: ${{ github.action_path }}) and use "${SKYLOS_ACTION_PATH}[dart]". The 'Build Skylos Go engine' step already does this.

Locations:

- `action.yml:126`

### github-env-injection (severity: high)

The 'Run Skylos Image Scan' step writes `echo "report=$REPORT" >> "$GITHUB_OUTPUT"`. REPORT is built from REPORT_DIR, which comes from the inherited process env var RUNNER_TEMP. That variable is not set inside this run: script, so under the composite-action rule it counts as workflow-controlled. The value is written without the `printf '%s' ... | tr -d '\n\r'` sanitization step.

Locations:

- `action.yml:147`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection, github-env-injection

**Notes:**

Install Skylos step: moved github.action_path into env SKYLOS_ACTION_PATH and used "${SKYLOS_ACTION_PATH}[dart]". Image scan step: the report path is now cleaned with printf '%s' | tr -d '\n\r' before it is written to GITHUB_OUTPUT. The step still uses the original REPORT variable everywhere else.

### Iteration 2

**Fixes applied:** script-injection

**Notes:**

Install Skylos step: moved ${{ github.action_path }} into env SKYLOS_ACTION_PATH and referenced it as "${SKYLOS_ACTION_PATH}[dart]" in the bash run script.

