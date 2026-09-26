<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.30.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.30.0** was hardened automatically. 1 finding(s) were identified and resolved across 2 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): A GitHub Actions expression `${{ github.action_path }}` is directly interpolated inside a `run:` shell command string in the "Install Skylos" step. Any `${{ ... }}` expression inside a run: block is a script-injection risk because the value is substituted into the shell command before the shell parses it. The offending line is: `run: python -m pip install "${{ github.action_path }}"`

Fix: move the value into an env var and reference it as a shell variable instead:
```yaml
env:
  ACTION_PATH: ${{ github.action_path }}
run: python -m pip install "$ACTION_PATH"
```

Locations:

- `action.yml:52`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed script-injection in the 'Install Skylos' step of action.yml (line 52). Moved `${{ github.action_path }}` out of the `run:` shell command string into an `env:` block as `ACTION_PATH`, and updated the run command to reference it as `"$ACTION_PATH"` instead of `"${{ github.action_path }}"`.

### Iteration 2

**Fixes applied:** script-injection

**Notes:**

Fixed unquoted $FLAGS variable in both 'Run Skylos Scan' (line 79) and 'Upload to Skylos Dashboard' (line 113) steps. Converted FLAGS from a plain string variable to a bash array (FLAGS=()), appending flags with FLAGS+=("--flag") syntax, and expanded with "${FLAGS[@]}" to properly quote each element and prevent word-splitting and glob expansion.

