<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.36.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.36.0** was hardened automatically. 1 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): The 'Install Skylos' step directly interpolates `${{ github.action_path }}` inside a `run:` shell command string: `python -m pip install "${{ github.action_path }}"`.

Any `${{ ... }}` expression interpolated directly in a `run:` block is a script-injection risk because the value is substituted into the shell command string before the shell parses it. Even though `github.action_path` is typically controlled by GitHub, the rule requires that no `${{ ... }}` expression appear directly inside a `run:` block.

Fix: Move the value into an `env:` variable and reference it as a quoted shell variable:
```yaml
env:
  ACTION_PATH: ${{ github.action_path }}
run: python -m pip install "$ACTION_PATH"
```

Locations:

- `action.yml:97`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed the script-injection finding in the 'Install Skylos' step of action.yml. Moved `${{ github.action_path }}` from the `run:` block into an `env:` variable `ACTION_PATH: ${{ github.action_path }}`, and updated the shell command from `python -m pip install "${{ github.action_path }}"` to `python -m pip install "$ACTION_PATH"`. This prevents the GitHub Actions expression from being interpolated directly into the shell command string.

