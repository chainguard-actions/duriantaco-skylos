<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v5.3.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v5.3.0** was hardened automatically. 1 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a), direct expression interpolation. The 'Install Skylos' step puts an Actions expression straight into the run: script: `run: python -m pip install "${{ github.action_path }}[dart]"`. Fix: pass the path through env (for example SKYLOS_ACTION_PATH: ${{ github.action_path }}) and use "$SKYLOS_ACTION_PATH[dart]", or use the runner-provided "$GITHUB_ACTION_PATH".

Locations:

- `action.yml:126`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Install Skylos step: moved ${{ github.action_path }} into env SKYLOS_ACTION_PATH; run now uses python -m pip install "${SKYLOS_ACTION_PATH}[dart]" (braces so [dart] isn't parsed as part of the variable; bash shell).

