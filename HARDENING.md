<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.33.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.33.0** was hardened automatically. 2 finding(s) were identified and resolved across 2 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): The 'Install Skylos' step directly interpolates `${{ github.action_path }}` inside a `run:` shell command string: `run: python -m pip install "${{ github.action_path }}"`. Any `${{ ... }}` expression interpolated directly in a `run:` block is a script-injection risk because the value is substituted into the shell command before the shell parses it.

Locations:

- `action.yml:59`

### script-injection (severity: high)

Sub-rule (b): The variable `$FLAGS` is expanded unquoted in two `run:` blocks (lines 91 and 130). `$FLAGS` is constructed from `$SKYLOS_ANALYSIS`, which is sourced from `inputs.analysis` (a caller-controlled input). Unquoted expansion allows shell metacharacters (`;`, `|`, `&`, `$(...)`, etc.) embedded in the input value to be interpreted by the shell. Offending lines: `          $FLAGS \` in the 'Run Skylos Scan' step (line 91) and the 'Upload to Skylos Dashboard' step (line 130). Fix: quote the expansion as `"$FLAGS"`.

Locations:

- `action.yml:91`
- `action.yml:130`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed all three script-injection locations in action.yml:
1. Line 59 ('Install Skylos' step): Moved `${{ github.action_path }}` into an `env:` block as `ACTION_PATH` and referenced it as `"$ACTION_PATH"` in the run command.
2. Lines 91 and 130 ('Run Skylos Scan' and 'Upload to Skylos Dashboard' steps): Replaced the unquoted `$FLAGS` string variable with a bash array (`FLAGS=()`), appending flags with `FLAGS+=(--flag)`, and expanded safely as `"${FLAGS[@]}"`. This eliminates the unquoted expansion injection risk while correctly passing each flag as a separate shell argument.

### Iteration 2

**Fixes applied:** script-injection, github-env-injection, missing-permissions, unpinned-uses

**Notes:**

Fixed all findings across 7 workflow files:

1. corpus.yml: Added `permissions: contents: read` at top level; moved github.base_ref and github.event.pull_request.base.sha into env block (BASE_REF, BASE_SHA) in 'Run curated corpus guard (base)' step.

2. quality-benchmark.yml: Added `permissions: contents: read` at top level; moved github.base_ref and github.event.pull_request.base.sha into env block (BASE_REF, BASE_SHA) in 'Run quality benchmark (base)' step.

3. skylos.yaml: Fixed 'Resolve diff base' step by moving github.event_name, github.base_ref, github.event.before, github.ref_name into env block and adding `tr -d '\n\r'` sanitization before writing to GITHUB_OUTPUT (fixes both script-injection and github-env-injection). Fixed 'Summarize in job log' step by moving steps.scan.outputs.REPORT into env block (SCAN_REPORT).

4. tests.yaml: Moved matrix.install_target into env block in 'Create venv + install deps'; moved matrix.python-version into env block in 'Build image' and 'Check Python runtime'; moved needs results into env block in 'Require matrix success'.

5. publish.yml: Moved github.repository into env block (GH_REPOSITORY) in 'Build and push multi-arch image' step.

6. analyzer-speed.yml: Added `permissions: contents: read` at top level.

7. examples/skylos-plus-claude-security.yml: Moved github.base_ref into env block in 'PR Review Comments'; pinned all 10 action references to full commit SHAs (actions/checkout@v4, actions/setup-python@v5, actions/upload-artifact@v4, anthropics/claude-code-action@main, actions/download-artifact@v4).

8. examples/skylos-tokenless-ci.yml: Moved github.sha into env block (GH_SHA) in 'Scan and upload'; pinned actions/checkout@v4 and actions/setup-python@v5 to full commit SHAs.

