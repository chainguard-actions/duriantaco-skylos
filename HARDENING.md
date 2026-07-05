<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos--/v4.27.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `1`

Action **duriantaco--skylos--/v4.27.0** was hardened automatically. 17 finding(s) were identified and resolved across 2 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Rule (a): Direct expression interpolation in run: blocks. action.yml 'Install Skylos' step interpolates ${{ github.action_path }} directly in a shell command: `python -m pip install "${{ github.action_path }}"`.

Locations:

- `action.yml:59`

### script-injection (severity: high)

Rule (a): Direct expression interpolation in run: blocks. corpus.yml 'Run curated corpus guard (base)' step interpolates ${{ github.base_ref }} and ${{ github.event.pull_request.base.sha }} directly in shell commands: `git fetch origin "${{ github.base_ref }}"` and `git worktree add /tmp/skylos-corpus-base "${{ github.event.pull_request.base.sha }}"`.

Locations:

- `.github/workflows/corpus.yml:49`

### script-injection (severity: high)

Rule (a): Direct expression interpolation in run: blocks. quality-benchmark.yml 'Run quality benchmark (base)' step interpolates ${{ github.base_ref }} and ${{ github.event.pull_request.base.sha }} directly in shell commands.

Locations:

- `.github/workflows/quality-benchmark.yml:42`

### script-injection (severity: high)

Rule (a): Direct expression interpolation in run: blocks. skylos.yaml 'Resolve diff base' step interpolates ${{ github.event_name }}, ${{ github.base_ref || 'main' }}, ${{ github.event.before }}, and ${{ github.ref_name || 'main' }} directly in shell commands.

Locations:

- `.github/workflows/skylos.yaml:52`

### script-injection (severity: high)

Rule (a): Direct expression interpolation in run: blocks. skylos.yaml 'Summarize in job log' step interpolates ${{ steps.scan.outputs.REPORT }} directly in a shell command: `echo "Skylos report: ${{ steps.scan.outputs.REPORT }}" >> $GITHUB_STEP_SUMMARY`.

Locations:

- `.github/workflows/skylos.yaml:148`

### script-injection (severity: high)

Rule (a): Direct expression interpolation in run: blocks. tests.yaml 'Create venv + install deps' step interpolates ${{ matrix.install_target }} directly in a shell command: `uv pip install -e "${{ matrix.install_target }}"`.

Locations:

- `.github/workflows/tests.yaml:33`

### script-injection (severity: high)

Rule (a): Direct expression interpolation in run: blocks. tests.yaml 'Require matrix success' step interpolates ${{ needs.test_matrix.result }} and ${{ needs.docker_smoke.result }} directly in shell commands.

Locations:

- `.github/workflows/tests.yaml:72`

### script-injection (severity: high)

Rule (a): Direct expression interpolation in run: blocks. publish.yml 'Build and push multi-arch image' step interpolates ${{ github.repository }} directly in shell commands used as Docker labels.

Locations:

- `.github/workflows/publish.yml:183`

### script-injection (severity: high)

Rule (a): Direct expression interpolation in run: blocks. examples/skylos-plus-claude-security.yml 'PR Review Comments' step interpolates ${{ github.base_ref || 'main' }} directly in a shell command: `skylos cicd review --input skylos-results.json --diff-base origin/${{ github.base_ref || 'main' }}`.

Locations:

- `.github/workflows/examples/skylos-plus-claude-security.yml:47`

### script-injection (severity: high)

Rule (a): Direct expression interpolation in run: blocks. examples/skylos-tokenless-ci.yml 'Scan and upload' step interpolates ${{ github.sha }} directly in a shell command: `skylos . --danger --quality --secrets --ai-defects --upload --force --sha "${{ github.sha }}"`.

Locations:

- `.github/workflows/examples/skylos-tokenless-ci.yml:32`

### github-env-injection (severity: high)

skylos.yaml 'Resolve diff base' step writes github.base_ref, github.event.before, and github.ref_name directly to $GITHUB_OUTPUT without the required sanitization (printf '%s' ... | tr -d '\n\r'). Example: `echo "base=origin/${{ github.base_ref || 'main' }}" >> "$GITHUB_OUTPUT"`.

Locations:

- `.github/workflows/skylos.yaml:52`

### github-env-injection (severity: high)

skylos.yaml 'Run Skylos' step sets env var REPORT from ${{ github.run_number }} and ${{ github.sha }}, then writes it to $GITHUB_OUTPUT without sanitization: `echo "REPORT=$REPORT" >> "$GITHUB_OUTPUT"`.

Locations:

- `.github/workflows/skylos.yaml:72`

### permissions (severity: medium)

missing-permissions: analyzer-speed.yml has no top-level permissions: key and no job-level permissions: key on any job. This grants the default (potentially broad) token permissions.

Locations:

- `.github/workflows/analyzer-speed.yml:1`

### permissions (severity: medium)

missing-permissions: corpus.yml has no top-level permissions: key and no job-level permissions: key on any job. This grants the default (potentially broad) token permissions.

Locations:

- `.github/workflows/corpus.yml:1`

### permissions (severity: medium)

missing-permissions: quality-benchmark.yml has no top-level permissions: key and no job-level permissions: key on any job. This grants the default (potentially broad) token permissions.

Locations:

- `.github/workflows/quality-benchmark.yml:1`

### unpinned-uses (severity: high)

Multiple unpinned uses: references found using tags or branch names instead of full SHA digests: actions/checkout@v4 (3 occurrences), actions/setup-python@v5 (2 occurrences), actions/upload-artifact@v4, anthropics/claude-code-action@main (branch ref), actions/download-artifact@v4 (2 occurrences).

Locations:

- `.github/workflows/examples/skylos-plus-claude-security.yml:34`
- `.github/workflows/examples/skylos-plus-claude-security.yml:61`
- `.github/workflows/examples/skylos-plus-claude-security.yml:68`

### unpinned-uses (severity: high)

Multiple unpinned uses: references found using tags instead of full SHA digests: actions/checkout@v4, actions/setup-python@v5.

Locations:

- `.github/workflows/examples/skylos-tokenless-ci.yml:20`
- `.github/workflows/examples/skylos-tokenless-ci.yml:25`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection, github-env-injection, permissions, unpinned-uses

**Notes:**

Fixed all 17 findings across 8 files:

1. action.yml: Moved github.action_path to env block (ACTION_PATH) in 'Install Skylos' step.

2. corpus.yml: Added 'permissions: contents: read' at top level. Moved github.base_ref and github.event.pull_request.base.sha to env block in 'Run curated corpus guard (base)' step.

3. quality-benchmark.yml: Added 'permissions: contents: read' at top level. Moved github.base_ref and github.event.pull_request.base.sha to env block in 'Run quality benchmark (base)' step.

4. analyzer-speed.yml: Added 'permissions: contents: read' at top level.

5. skylos.yaml: (a) 'Resolve diff base' step - moved all four github context expressions (event_name, base_ref, event.before, ref_name) to env block and sanitized all values written to GITHUB_OUTPUT with printf/tr. (b) 'Run Skylos' step - sanitized REPORT before writing to GITHUB_OUTPUT. (c) 'Summarize in job log' step - moved steps.scan.outputs.REPORT to env block as SCAN_REPORT.

6. tests.yaml: Moved matrix.install_target to env block in 'Create venv + install deps'. Moved needs.test_matrix.result and needs.docker_smoke.result to env block in 'Require matrix success'.

7. publish.yml: Moved github.repository to env block as GITHUB_REPOSITORY_NAME in 'Build and push multi-arch image'.

8. examples/skylos-plus-claude-security.yml: Moved github.base_ref to env block in 'PR Review Comments'. Pinned all unpinned actions: actions/checkout@v4→34e114876b0b11c390a56381ad16ebd13914f8d5, actions/setup-python@v5→a26af69be951a213d495a4c3e4e4022e16d87065, actions/upload-artifact@v4→ea165f8d65b6e75b540449e92b4886f43607fa02, anthropics/claude-code-action@main→58a2944bbcf1a73b1ae7960995fffca4fa29b113, actions/download-artifact@v4→d3f86a106a0bac45b974a628896c90dbdf5c8093.

9. examples/skylos-tokenless-ci.yml: Moved github.sha to env block as GIT_SHA in 'Scan and upload'. Pinned actions/checkout@v4→34e114876b0b11c390a56381ad16ebd13914f8d5 and actions/setup-python@v5→a26af69be951a213d495a4c3e4e4022e16d87065.

### Iteration 2

**Fixes applied:** github-env-injection

**Notes:**

Fixed two github-env-injection findings in .github/workflows/publish.yml:
1. 'Resolve release tag input' step: Added `safe_tag=$(printf '%s' "$tag" | tr -d '\n\r')` before writing to GITHUB_OUTPUT, replacing the direct use of `$tag`.
2. 'Derive image metadata' step: Added sanitization for `version` (`safe_version`), `major` (`safe_major`), and `minor` (`safe_minor`) using `printf '%s' ... | tr -d '\n\r'` before each write to GITHUB_OUTPUT. The sanitized variables are also used in the `*-*` check and IFS split to maintain consistency.

