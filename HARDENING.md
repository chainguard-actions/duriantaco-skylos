<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.31.1

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.31.1** was hardened automatically. 2 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): The 'Install Skylos' step interpolates `${{ github.action_path }}` directly inside a `run:` shell command string: `run: python -m pip install "${{ github.action_path }}"`.

Any `${{ ... }}` expression directly inside a `run:` block is a script-injection risk because the value is substituted into the shell command string before the shell parses it. Even though `github.action_path` is typically GitHub-controlled, the rules require that no `${{ ... }}` expression appear inside a `run:` block. The safe pattern is to pass the value via an `env:` variable and reference it as `"$ENV_VAR"` in the script.

Locations:

- `action.yml:59`

### script-injection (severity: high)

Sub-rule (b): In both the 'Run Skylos Scan' step (line 91) and the 'Upload to Skylos Dashboard' step (line 130), the shell variable `$FLAGS` is used unquoted in the `python -m skylos.cli` invocation: `$FLAGS \`. `$FLAGS` is built from `$SKYLOS_ANALYSIS`, which is sourced from `inputs.analysis` — a workflow-controllable input. Unquoted shell variable expansion allows the shell to parse metacharacters (`;`, `|`, `&`, whitespace, glob chars) out of the value. The safe pattern is to use an array (`FLAGS=(); FLAGS+=(--danger)`) and expand it as `"${FLAGS[@]}"`.

Locations:

- `action.yml:91`
- `action.yml:130`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed three script-injection issues in hardened/action/action.yml:
1. 'Install Skylos' step (line 59): Moved `${{ github.action_path }}` into an `env:` block as `ACTION_PATH` and referenced it as `"$ACTION_PATH"` in the run command.
2. 'Run Skylos Scan' step (line 91): Converted `FLAGS` string variable with unquoted `$FLAGS` expansion to a bash array (`FLAGS=()`, `FLAGS+=(--flag)`) expanded safely as `"${FLAGS[@]}"`.
3. 'Upload to Skylos Dashboard' step (line 130): Same bash array conversion applied, replacing unquoted `$FLAGS` with `"${FLAGS[@]}"`.

