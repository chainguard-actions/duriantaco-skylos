<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.48.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.48.0** was hardened automatically. 1 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): The `${{ github.action_path }}` expression is directly interpolated inside a `run:` shell command string in the 'Install Skylos' step. Any `${{ ... }}` expression inside a `run:` block is a script-injection risk because the value is substituted into the shell command before the shell parses it. The offending line is: `run: python -m pip install "${{ github.action_path }}[dart]"`. The safe fix is to use the pre-set `$GITHUB_ACTION_PATH` environment variable instead: `run: python -m pip install "$GITHUB_ACTION_PATH[dart]"`

Locations:

- `action.yml:96`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed script-injection in the 'Install Skylos' step (action.yml line 96): replaced `${{ github.action_path }}` with `$GITHUB_ACTION_PATH` in the pip install command. The `$GITHUB_ACTION_PATH` environment variable is pre-set by the GitHub Actions runner and is equivalent in value but safe from script injection since it is not interpolated into the shell command string before parsing.

