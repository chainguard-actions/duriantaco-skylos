<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v5.1.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v5.1.0** was hardened automatically. 1 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): the 'Install Skylos' step puts a GitHub Actions expression directly into the run: script: `run: python -m pip install "${{ github.action_path }}[dart]"`. Pass github.action_path through an env: variable (for example SKYLOS_ACTION_PATH) and quote it in the script: `python -m pip install "${SKYLOS_ACTION_PATH}[dart]"`.

Locations:

- `action.yml:126`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed the script-injection finding in action.yml. In the 'Install Skylos' step, github.action_path now goes into the step's env as SKYLOS_ACTION_PATH, and the script uses it quoted: python -m pip install "${SKYLOS_ACTION_PATH}[dart]". The 'Build Skylos Go engine' step already used this pattern. A search of action.yml found no other run: line with an inline ${{ }} expression, but it only matched expressions on the same line as run:, so expressions inside multi-line scripts were not checked. Nothing was run to test the change.

