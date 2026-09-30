<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.22.1

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.22.1** was hardened automatically. 2 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Rule (a): A ${{ }} expression is directly interpolated inside a run: shell command. The step 'Install Skylos' uses `run: python -m pip install "${{ github.action_path }}"`. Any ${{ ... }} expression inside a run: block is a script-injection risk because the value is substituted into the shell command string before the shell parses it. Even though github.action_path is GitHub-controlled, the pattern is flagged by the check.

Locations:

- `action.yml:59`

### script-injection (severity: high)

Rule (b): The shell variable $FLAGS is used unquoted in two run: blocks. $FLAGS is built from $SKYLOS_ANALYSIS, which is sourced from inputs.analysis (an untrusted caller-controlled input mapped via env:). Unquoted expansion of $FLAGS allows shell metacharacter injection (e.g., semicolons, pipes, command substitution) if inputs.analysis contains malicious content. Offending lines: `$FLAGS \` in the 'Run Skylos Scan' step and `$FLAGS \` in the 'Upload to Skylos Dashboard' step. Fix: quote the variable as "$FLAGS" or restructure to pass flags as an array.

Locations:

- `action.yml:88`
- `action.yml:124`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed three script-injection issues in action.yml: (1) Moved `${{ github.action_path }}` in the 'Install Skylos' step into an env: block as ACTION_PATH, referenced as "$ACTION_PATH" in the run: command. (2) Replaced unquoted string-based $FLAGS variable in 'Run Skylos Scan' with a bash array (FLAGS=()), populated with FLAGS+=("--flag") conditionals, and expanded as "${FLAGS[@]}" to prevent shell metacharacter injection from the caller-controlled inputs.analysis value while preserving correct argument splitting. (3) Applied the same bash array fix to the 'Upload to Skylos Dashboard' step.

