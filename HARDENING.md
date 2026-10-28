<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v5.1.2

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v5.1.2** was hardened automatically. 1 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a), direct expression interpolation: the 'Install Skylos' step puts a GitHub Actions expression straight into the run: shell command: `run: python -m pip install "${{ github.action_path }}[dart]"`. Fix: pass it through env, e.g. `SKYLOS_ACTION_PATH: ${{ github.action_path }}`, and use `python -m pip install "${SKYLOS_ACTION_PATH}[dart]"`.

Locations:

- `action.yml:126`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

In action.yml, the 'Install Skylos' step had `${{ github.action_path }}` written directly into its shell command. I moved it to `env: SKYLOS_ACTION_PATH`, and the command now reads `python -m pip install "${SKYLOS_ACTION_PATH}[dart]"`. The path is still one quoted argument, so pip receives the same value as before. A search found no other `${{ }}` expressions on `run:` lines in action.yml. Nothing was run to test the change.

