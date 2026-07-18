<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.27.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.27.0** was hardened automatically. 3 finding(s) were identified and resolved across 3 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): The 'Install Skylos' step directly interpolates `${{ github.action_path }}` inside a `run:` shell command string: `run: python -m pip install "${{ github.action_path }}"`. Any `${{ ... }}` expression directly inside a `run:` block is a script-injection risk because YAML template substitution occurs before the shell ever sees the value, bypassing shell quoting.

Locations:

- `action.yml:55`

### script-injection (severity: high)

Sub-rule (b): In the 'Run Skylos Scan' step, the shell variable `$FLAGS` is used unquoted in the `python -m skylos.cli` invocation (`$FLAGS \`). `FLAGS` is constructed from `$SKYLOS_ANALYSIS`, which is sourced from `inputs.analysis` (an untrusted caller-controlled input). Unquoted expansion allows an attacker to inject shell metacharacters (`;`, `|`, `&`, `$(...)`, etc.) via the `analysis` input.

Locations:

- `action.yml:80`

### script-injection (severity: high)

Sub-rule (b): In the 'Upload to Skylos Dashboard' step, the shell variable `$FLAGS` is used unquoted in the `python -m skylos.cli` invocation (`$FLAGS \`). `FLAGS` is constructed from `$SKYLOS_ANALYSIS`, which is sourced from `inputs.analysis` (an untrusted caller-controlled input). Unquoted expansion allows an attacker to inject shell metacharacters via the `analysis` input.

Locations:

- `action.yml:109`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed all three script-injection findings in hardened/action/action.yml:
1. 'Install Skylos' step (line 55): Moved `${{ github.action_path }}` into an `env:` block as `ACTION_PATH` and referenced it as `"$ACTION_PATH"` in the run command, eliminating direct YAML template interpolation in the shell string.
2. 'Run Skylos Scan' step (line 80): Replaced the unquoted string variable `$FLAGS` with a bash array (`FLAGS=()`; `FLAGS+=("--flag")`; `"${FLAGS[@]}"`). Each flag is now a separate, properly-quoted array element, preventing shell metacharacter injection via the `analysis` input.
3. 'Upload to Skylos Dashboard' step (line 109): Applied the same bash-array fix as finding 2 to the identical FLAGS pattern in the upload step.

### Iteration 1

**Fixes applied:** script-injection, github-env-injection, missing-permissions, unpinned-uses

**Notes:**

Fixed all 14 findings across 7 workflow files:

1. corpus.yml: Added `permissions: contents: read`; moved github.base_ref and github.event.pull_request.base.sha to env: block in 'Run curated corpus guard (base)' step.

2. quality-benchmark.yml: Added `permissions: contents: read`; moved github.base_ref and github.event.pull_request.base.sha to env: block in 'Run quality benchmark (base)' step.

3. analyzer-speed.yml: Added `permissions: contents: read`.

4. skylos.yaml: Fixed 'Resolve diff base' step by moving all 4 github expressions (event_name, base_ref, event.before, ref_name) to env: block and adding `printf '%s' ... | tr -d '\n\r'` sanitization before each `echo >> $GITHUB_OUTPUT`. Fixed 'Run Skylos' step by adding sanitization before writing REPORT to GITHUB_OUTPUT. Fixed 'Summarize in job log' step by moving steps.scan.outputs.REPORT to env: block.

5. tests.yaml: Moved matrix.install_target to env: block in 'Create venv + install deps' step. Moved needs.test_matrix.result and needs.docker_smoke.result to env: block in 'Require matrix success' step.

6. publish.yml: Added GH_REPOSITORY env var and replaced ${{ github.repository }} with $GH_REPOSITORY in 'Build and push multi-arch image' step.

7. examples/skylos-plus-claude-security.yml: Pinned all 5 unpinned actions to full SHA commits; moved github.base_ref to env: block in 'PR Review Comments' step.

8. examples/skylos-tokenless-ci.yml: Pinned actions/checkout and actions/setup-python to full SHA commits; moved github.sha to env: block in 'Scan and upload' step.

### Iteration 2

**Fixes applied:** github-env-injection, github-env-injection

**Notes:**

Fixed two github-env-injection findings in hardened/action/.github/workflows/publish.yml:
1. 'Resolve release tag input' step (line ~63): Added `safe_tag="$(printf '%s' "$tag" | tr -d '\n\r')"` before writing to GITHUB_OUTPUT, replacing `echo "tag=$tag"` with `echo "tag=$safe_tag"`.
2. 'Derive image metadata' step (line ~253): Added `safe_version="$(printf '%s' "$version" | tr -d '\n\r')"` and used it throughout; also added `safe_major` and `safe_minor` sanitization before writing major/minor to GITHUB_OUTPUT. All caller-controlled values are now stripped of newlines before being written to the output file.

