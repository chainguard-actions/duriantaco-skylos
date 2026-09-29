<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.22.1

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.22.1** was hardened automatically. 3 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): The 'Install Skylos' step directly interpolates the GitHub Actions expression `${{ github.action_path }}` inside a `run:` shell command string: `run: python -m pip install "${{ github.action_path }}"`.

Any `${{ ... }}` expression interpolated directly into a `run:` block is a script-injection risk because the value is substituted into the shell command string before the shell parses it. Even though `github.action_path` is typically GitHub-controlled, the rule requires that no `${{ ... }}` expression appear directly inside a `run:` block. The fix is to pass the value via an `env:` variable and reference it as `"$ACTION_PATH"` in the script.

Locations:

- `action.yml:56`

### script-injection (severity: high)

Sub-rule (b): In the 'Run Skylos Scan' step, the shell variable `$FLAGS` is expanded unquoted in the `python -m skylos.cli` command line (`$FLAGS \`). `$FLAGS` is built by appending literal strings based on grep matches against `$SKYLOS_ANALYSIS`, which is sourced from `inputs.analysis` (user-controlled). Although the grep filtering limits what ends up in `$FLAGS`, the variable is still unquoted, allowing the shell to word-split and glob-expand its contents. The fix is to quote the expansion: `"$FLAGS"`.

Locations:

- `action.yml:75`

### script-injection (severity: high)

Sub-rule (b): In the 'Upload to Skylos Dashboard' step, the shell variable `$FLAGS` is expanded unquoted in the `python -m skylos.cli` command line (`$FLAGS \`). `$FLAGS` is built by appending literal strings based on grep matches against `$SKYLOS_ANALYSIS`, which is sourced from `inputs.analysis` (user-controlled). Although the grep filtering limits what ends up in `$FLAGS`, the variable is still unquoted, allowing the shell to word-split and glob-expand its contents. The fix is to quote the expansion: `"$FLAGS"`.

Locations:

- `action.yml:99`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed all three script-injection findings in hardened/action/action.yml:
1. 'Install Skylos' step: Moved `${{ github.action_path }}` out of the `run:` block into an `env:` variable `ACTION_PATH`, referenced as `"$ACTION_PATH"` in the shell command.
2. 'Run Skylos Scan' step: Converted `FLAGS` string variable with unquoted `$FLAGS` expansion to a bash array (`FLAGS=()`), using `FLAGS+=("--flag")` for appending and `"${FLAGS[@]}"` for safe expansion.
3. 'Upload to Skylos Dashboard' step: Same bash array fix applied to eliminate the unquoted `$FLAGS` expansion.

