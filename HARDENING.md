<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v5.1.3

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v5.1.3** was hardened automatically. 1 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): the 'Install Skylos' step puts a GitHub expression straight into its run: script: `run: python -m pip install "${{ github.action_path }}[dart]"`. The value is substituted into the script text before the shell parses it. Fix: pass it in through env (e.g. SKYLOS_ACTION_PATH: ${{ github.action_path }}) and use `python -m pip install "${SKYLOS_ACTION_PATH}[dart]"`.

Locations:

- `action.yml:126`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Install Skylos step: moved ${{ github.action_path }} into env as SKYLOS_ACTION_PATH. The step now runs `python -m pip install "${SKYLOS_ACTION_PATH}[dart]"`, so nothing else about the install changes. I made no other changes.

