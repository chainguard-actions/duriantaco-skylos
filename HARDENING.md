<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.29.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `1`

Action **duriantaco--skylos/v4.29.0** was hardened automatically. 3 finding(s) were identified and resolved across 3 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Rule (a): The 'Install Skylos' step interpolates ${{ github.action_path }} directly inside a run: shell command string: `run: python -m pip install "${{ github.action_path }}"`  Any ${{ ... }} expression inside a run: block is a script-injection risk regardless of the context it reads from.

Locations:

- `action.yml:55`

### script-injection (severity: high)

Rule (b): In the 'Run Skylos Scan' step, the variable $FLAGS is built from $SKYLOS_ANALYSIS (which holds inputs.analysis, a workflow-controllable value) and then expanded unquoted in the shell command: `python -m skylos.cli "$SKYLOS_PATH" \ --confidence "$SKYLOS_CONFIDENCE" \ $FLAGS \ --json`. An unquoted shell variable expansion allows shell metacharacter injection.

Locations:

- `action.yml:79`

### script-injection (severity: high)

Rule (b): In the 'Upload to Skylos Dashboard' step, the variable $FLAGS is built from $SKYLOS_ANALYSIS (which holds inputs.analysis, a workflow-controllable value) and then expanded unquoted in the shell command: `python -m skylos.cli "$SKYLOS_PATH" \ --confidence "$SKYLOS_CONFIDENCE" \ $FLAGS \ --upload`. An unquoted shell variable expansion allows shell metacharacter injection.

Locations:

- `action.yml:113`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed all three script-injection findings in hardened/action/action.yml:
1. 'Install Skylos' step: moved `${{ github.action_path }}` into an env var `ACTION_PATH` and referenced it as `"$ACTION_PATH"` in the run command.
2. 'Run Skylos Scan' step: converted `FLAGS` from a string variable (expanded unquoted) to a bash array (`FLAGS=()`), building it with `FLAGS+=(--flag)` and expanding safely as `"${FLAGS[@]}"`.
3. 'Upload to Skylos Dashboard' step: same bash array conversion applied — `FLAGS=()` with `FLAGS+=(--flag)` entries and `"${FLAGS[@]}"` expansion, eliminating the unquoted variable expansion risk.

### Iteration 2

**Fixes applied:** script-injection, github-env-injection, missing-permissions, unpinned-uses

**Notes:**

Fixed all 14 findings across 7 workflow files:

1. corpus.yml: Added `permissions: contents: read`; moved github.base_ref and github.event.pull_request.base.sha to env block in 'Run curated corpus guard (base)' step.

2. quality-benchmark.yml: Added `permissions: contents: read`; moved github.base_ref and github.event.pull_request.base.sha to env block in 'Run quality benchmark (base)' step.

3. analyzer-speed.yml: Added `permissions: contents: read`.

4. skylos.yaml: Fixed 'Resolve diff base' step by moving all github context values (event_name, base_ref, event.before, ref_name) to env block and sanitizing all GITHUB_OUTPUT writes with `printf '%s' ... | tr -d '\n\r'`. Fixed 'Summarize in job log' step by moving steps.scan.outputs.REPORT to env block.

5. publish.yml: Moved github.repository to env block as GH_REPOSITORY in 'Build and push multi-arch image' step.

6. skylos-plus-claude-security.yml: Moved github.base_ref to env block in 'PR Review Comments' step. Pinned all unpinned actions to full SHA digests: actions/checkout@v4→34e114876b0b11c390a56381ad16ebd13914f8d5, actions/setup-python@v5→a26af69be951a213d495a4c3e4e4022e16d87065, actions/upload-artifact@v4→ea165f8d65b6e75b540449e92b4886f43607fa02, anthropics/claude-code-action@main→536f2c32a39763739000b0e1ac69ca2647d97ce9, actions/download-artifact@v4→d3f86a106a0bac45b974a628896c90dbdf5c8093.

7. skylos-tokenless-ci.yml: Moved github.sha to env block in 'Scan and upload' step. Pinned actions/checkout@v4 and actions/setup-python@v5 to full SHA digests.

8. tests.yaml: Moved matrix.install_target to env block in 'Create venv + install deps' step. Moved needs.test_matrix.result and needs.docker_smoke.result to env block in 'Require matrix success' step.

### Iteration 3

**Fixes applied:** github-env-injection

**Notes:**

Fixed two github-env-injection findings in .github/workflows/publish.yml:
1. 'Resolve release tag input' step (line 63): Added `safe_tag=$(printf '%s' "$tag" | tr -d '\n\r')` before writing to GITHUB_OUTPUT, replacing the direct `echo "tag=$tag"` with `echo "tag=$safe_tag"`.
2. 'Derive image metadata' step (line 230): Added sanitization for `version`, `major`, and `minor` variables using `printf '%s' ... | tr -d '\n\r'` before writing each to GITHUB_OUTPUT. Also updated the `*-*` check and IFS split to use `safe_version` for consistency.

