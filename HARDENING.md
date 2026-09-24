<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.39.1

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.39.1** was hardened automatically. 1 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): A GitHub Actions expression `${{ github.action_path }}` is interpolated directly inside a `run:` shell command string in the 'Install Skylos' step. The expression `${{ github.action_path }}` is substituted by the YAML template engine before the shell ever sees the value, meaning any special characters in the path could be interpreted by the shell. The offending line is: `run: python -m pip install "${{ github.action_path }}"`

The safe pattern is to pass the value via an `env:` variable and reference it as a quoted shell variable, e.g.:
```yaml
env:
  ACTION_PATH: ${{ github.action_path }}
run: python -m pip install "$ACTION_PATH"
```

Locations:

- `action.yml:93`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed the 'Install Skylos' step in action.yml (line 93): moved `${{ github.action_path }}` out of the `run:` shell string and into an `env:` block as `ACTION_PATH`. The shell command now uses `"$ACTION_PATH"` instead of `"${{ github.action_path }}"`.

