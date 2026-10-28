<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v5.1.1

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v5.1.1** was hardened automatically. 1 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Rule (a), direct expression interpolation: the 'Install Skylos' step puts a GitHub Actions expression straight into its run: script: `run: python -m pip install "${{ github.action_path }}[dart]"`. The template is filled in before the shell runs, so the value is never treated as plain data. Fix: set `SKYLOS_ACTION_PATH: ${{ github.action_path }}` under the step's env: and run `python -m pip install "${SKYLOS_ACTION_PATH}[dart]"`.

Locations:

- `action.yml:118`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

In action.yml, the 'Install Skylos' step now takes github.action_path from env (SKYLOS_ACTION_PATH) and runs `python -m pip install "${SKYLOS_ACTION_PATH}[dart]"`. The step is bash, quoting is unchanged, and the install does the same thing as before. Not verified by running the action or a new analysis pass. A follow-up search of action.yml for run: lines containing ${{ returned one match, but the text at that position was the fixed step with no expression in its run: line; the search was not re-run to confirm the result was stale.

