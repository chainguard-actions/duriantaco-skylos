<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v5.6.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v5.6.0** was hardened automatically. 1 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Rule (a): the 'Install Skylos' step puts a GitHub Actions expression straight into a run: shell command: `run: python -m pip install "${{ github.action_path }}[dart]"`. The value is substituted into the script text before the shell parses it. Move it into env (e.g. SKYLOS_ACTION_PATH: ${{ github.action_path }}) and use "${SKYLOS_ACTION_PATH}[dart]", or use the runner-provided "$GITHUB_ACTION_PATH" instead.

Locations:

- `action.yml:126`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

In the 'Install Skylos' step, github.action_path is now passed in through env as SKYLOS_ACTION_PATH, and the command uses "${SKYLOS_ACTION_PATH}[dart]". The step's shell is bash, so this form of reference works.

