<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos--/v4.28.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `1`

Action **duriantaco--skylos--/v4.28.0** was hardened automatically. 4 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### unpinned-uses (severity: high)

Multiple unpinned action references found in example workflow files. In .github/workflows/examples/skylos-plus-claude-security.yml: actions/checkout@v4, actions/setup-python@v5, anthropics/claude-code-action@main, actions/upload-artifact@v4, actions/download-artifact@v4. In .github/workflows/examples/skylos-tokenless-ci.yml: actions/checkout@v4, actions/setup-python@v5. These use mutable tags/branches instead of full 40-character commit SHAs, making them vulnerable to supply-chain attacks.

Locations:

- `.github/workflows/examples/skylos-plus-claude-security.yml:33`
- `.github/workflows/examples/skylos-tokenless-ci.yml:27`

### permissions (severity: medium)

missing-permissions: These workflow files have no top-level permissions: key and no job-level permissions: key on any job, granting default (potentially write) permissions to all jobs.

Locations:

- `.github/workflows/analyzer-speed.yml:1`
- `.github/workflows/corpus.yml:1`
- `.github/workflows/quality-benchmark.yml:1`

### script-injection (severity: high)

Sub-rule (a): GitHub Actions expressions are directly interpolated inside run: shell command strings across multiple files. skylos.yaml 'Resolve diff base' step: ${{ github.event_name }}, ${{ github.base_ref || 'main' }}, ${{ github.event.before }}, ${{ github.ref_name || 'main' }} interpolated directly in shell. skylos.yaml 'Summarize in job log' step: ${{ steps.scan.outputs.REPORT }} interpolated directly in run: block. corpus.yml 'Run curated corpus guard (base)' step: ${{ github.base_ref }} and ${{ github.event.pull_request.base.sha }} interpolated directly. quality-benchmark.yml 'Run quality benchmark (base)' step: ${{ github.base_ref }} and ${{ github.event.pull_request.base.sha }} interpolated directly. tests.yaml 'Create venv + install deps' step: ${{ matrix.install_target }} interpolated directly. tests.yaml 'Require matrix success' step: ${{ needs.test_matrix.result }} and ${{ needs.docker_smoke.result }} interpolated directly. publish.yml 'Build and push multi-arch image' step: ${{ github.repository }} interpolated directly in shell labels. action.yml 'Install Skylos' step: ${{ github.action_path }} interpolated directly. skylos-plus-claude-security.yml 'PR Review Comments' step: ${{ github.base_ref || 'main' }} interpolated directly. skylos-tokenless-ci.yml 'Scan and upload' step: ${{ github.sha }} interpolated directly.

Locations:

- `.github/workflows/skylos.yaml:49`
- `.github/workflows/skylos.yaml:130`
- `.github/workflows/corpus.yml:50`
- `.github/workflows/quality-benchmark.yml:47`
- `.github/workflows/tests.yaml:30`
- `.github/workflows/tests.yaml:72`
- `.github/workflows/publish.yml:120`
- `action.yml:57`
- `.github/workflows/examples/skylos-plus-claude-security.yml:52`
- `.github/workflows/examples/skylos-tokenless-ci.yml:42`

### github-env-injection (severity: high)

In skylos.yaml 'Resolve diff base' step, untrusted github context values (${{ github.base_ref }}, ${{ github.event.before }}, ${{ github.ref_name }}) are written directly to $GITHUB_OUTPUT without sanitization (no printf '%s' ... | tr -d '\n\r' applied before the write). In skylos.yaml 'Run Skylos' step, the REPORT env var is set from ${{ github.run_number }}_${{ github.sha }} in the env: block and then written to $GITHUB_OUTPUT via echo "REPORT=$REPORT" without sanitization.

Locations:

- `.github/workflows/skylos.yaml:50`
- `.github/workflows/skylos.yaml:62`

## Iteration Notes

### Iteration 1

**Fixes applied:** unpinned-uses, permissions, script-injection, github-env-injection

**Notes:**

Fixed all findings: (1) Pinned 5 unpinned action references in example workflows to full commit SHAs (actions/checkout@34e114876b0b11c390a56381ad16ebd13914f8d5, actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065, anthropics/claude-code-action@58a2944bbcf1a73b1ae7960995fffca4fa29b113, actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02, actions/download-artifact@d3f86a106a0bac45b974a628896c90dbdf5c8093). (2) Added top-level 'permissions: contents: read' to analyzer-speed.yml, corpus.yml, and quality-benchmark.yml. (3) Fixed script injection in 9 locations by moving all ${{ }} expressions into env: blocks and referencing them as plain shell variables. (4) Fixed github-env-injection in skylos.yaml by sanitizing values before writing to GITHUB_OUTPUT using printf '%s' ... | tr -d '\n\r'.

