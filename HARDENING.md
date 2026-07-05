<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos--/v4.26.1

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `1`

Action **duriantaco--skylos--/v4.26.1** was hardened automatically. 14 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Rule (a): ${{ github.action_path }} is interpolated directly inside a run: shell command string in the 'Install Skylos' step: `run: python -m pip install "${{ github.action_path }}"`

Locations:

- `action.yml:57`

### script-injection (severity: high)

Rule (a): GitHub context expressions are interpolated directly inside run: shell command strings. In the 'Run curated corpus guard (base)' step: `git fetch origin "${{ github.base_ref }}" --depth=1` and `git worktree add /tmp/skylos-corpus-base "${{ github.event.pull_request.base.sha }}"`

Locations:

- `.github/workflows/corpus.yml:57`

### script-injection (severity: high)

Rule (a): GitHub context expressions are interpolated directly inside run: shell command strings. In the 'Run quality benchmark (base)' step: `git fetch origin "${{ github.base_ref }}" --depth=1` and `git worktree add /tmp/skylos-quality-base "${{ github.event.pull_request.base.sha }}"`

Locations:

- `.github/workflows/quality-benchmark.yml:47`

### script-injection (severity: high)

Rule (a): GitHub context expressions are interpolated directly inside run: shell command strings. In the 'Resolve diff base' step: `if [ "${{ github.event_name }}" = "pull_request" ]`, `echo "base=origin/${{ github.base_ref || 'main' }}" >> "$GITHUB_OUTPUT"`, `[ -n "${{ github.event.before }}" ]`, `echo "base=${{ github.event.before }}" >> "$GITHUB_OUTPUT"`, `echo "base=origin/${{ github.ref_name || 'main' }}" >> "$GITHUB_OUTPUT"`. Also in 'Summarize in job log': `echo "Skylos report: ${{ steps.scan.outputs.REPORT }}" >> $GITHUB_STEP_SUMMARY`

Locations:

- `.github/workflows/skylos.yaml:56`
- `.github/workflows/skylos.yaml:113`

### script-injection (severity: high)

Rule (a): ${{ github.base_ref }} is interpolated directly inside a run: shell command string in the 'PR Review Comments' step: `run: skylos cicd review --input skylos-results.json --diff-base origin/${{ github.base_ref || 'main' }}`

Locations:

- `.github/workflows/examples/skylos-plus-claude-security.yml:52`

### script-injection (severity: high)

Rule (a): ${{ github.sha }} is interpolated directly inside a run: shell command string in the 'Scan and upload' step: `run: skylos . --danger --quality --secrets --upload --force --sha "${{ github.sha }}"`

Locations:

- `.github/workflows/examples/skylos-tokenless-ci.yml:37`

### script-injection (severity: high)

Rule (a): ${{ github.repository }} is interpolated directly inside a run: shell command string in the 'Build and push multi-arch image' step: `--label "org.opencontainers.image.url=https://github.com/${{ github.repository }}"` and `--label "org.opencontainers.image.source=https://github.com/${{ github.repository }}"`

Locations:

- `.github/workflows/publish.yml:196`

### script-injection (severity: high)

Rule (a): ${{ matrix.install_target }} is interpolated directly inside a run: shell command string in the 'Create venv + install deps' step: `uv pip install -e "${{ matrix.install_target }}"`. Also ${{ needs.test_matrix.result }} and ${{ needs.docker_smoke.result }} are interpolated in the 'Require matrix success' step.

Locations:

- `.github/workflows/tests.yaml:36`
- `.github/workflows/tests.yaml:73`

### github-env-injection (severity: high)

The 'Resolve diff base' step writes github.base_ref, github.event.before, and github.ref_name directly to $GITHUB_OUTPUT without the required sanitization step (printf '%s' ... | tr -d '\n\r'). For example: `echo "base=origin/${{ github.base_ref || 'main' }}" >> "$GITHUB_OUTPUT"` and `echo "base=${{ github.event.before }}" >> "$GITHUB_OUTPUT"`

Locations:

- `.github/workflows/skylos.yaml:57`

### unpinned-uses (severity: high)

Multiple uses: references are pinned to mutable tags or branches instead of full 40-character commit SHAs: actions/checkout@v4, actions/setup-python@v5, actions/upload-artifact@v4, anthropics/claude-code-action@main, actions/download-artifact@v4

Locations:

- `.github/workflows/examples/skylos-plus-claude-security.yml:32`

### unpinned-uses (severity: high)

Multiple uses: references are pinned to mutable tags instead of full 40-character commit SHAs: actions/checkout@v4, actions/setup-python@v5

Locations:

- `.github/workflows/examples/skylos-tokenless-ci.yml:24`

### missing-permissions (severity: medium)

Workflow has no top-level permissions: key and no job-level permissions: key on any job, granting default (potentially broad) permissions to all jobs.

Locations:

- `.github/workflows/analyzer-speed.yml:1`

### missing-permissions (severity: medium)

Workflow has no top-level permissions: key and no job-level permissions: key on any job, granting default (potentially broad) permissions to all jobs.

Locations:

- `.github/workflows/corpus.yml:1`

### missing-permissions (severity: medium)

Workflow has no top-level permissions: key and no job-level permissions: key on any job, granting default (potentially broad) permissions to all jobs.

Locations:

- `.github/workflows/quality-benchmark.yml:1`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection, github-env-injection, unpinned-uses, missing-permissions

**Notes:**

Fixed all 14 findings across 9 files:

1. action.yml: Moved github.action_path to env block (ACTION_PATH) to prevent script injection.

2. corpus.yml: Added 'permissions: contents: read' at top level. Moved github.base_ref and github.event.pull_request.base.sha to env block (BASE_REF, BASE_SHA) in 'Run curated corpus guard (base)' step.

3. quality-benchmark.yml: Added 'permissions: contents: read' at top level. Moved github.base_ref and github.event.pull_request.base.sha to env block (BASE_REF, BASE_SHA) in 'Run quality benchmark (base)' step.

4. skylos.yaml: Fixed 'Resolve diff base' step by moving all github context expressions (event_name, base_ref, event.before, ref_name) to env block and sanitizing values with printf/tr before writing to GITHUB_OUTPUT (fixes both script-injection and github-env-injection). Fixed 'Summarize in job log' step by moving steps.scan.outputs.REPORT to env block.

5. examples/skylos-plus-claude-security.yml: Moved github.base_ref to env block (BASE_REF) in 'PR Review Comments' step. Pinned all unpinned actions: actions/checkout@v4 -> @34e114876b0b11c390a56381ad16ebd13914f8d5, actions/setup-python@v5 -> @a26af69be951a213d495a4c3e4e4022e16d87065, actions/upload-artifact@v4 -> @ea165f8d65b6e75b540449e92b4886f43607fa02, anthropics/claude-code-action@main -> @58a2944bbcf1a73b1ae7960995fffca4fa29b113, actions/download-artifact@v4 -> @d3f86a106a0bac45b974a628896c90dbdf5c8093.

6. examples/skylos-tokenless-ci.yml: Pinned actions/checkout@v4 and actions/setup-python@v5 to full SHAs. Moved github.sha to env block (GITHUB_SHA_VAL) in 'Scan and upload' step.

7. publish.yml: Moved github.repository to env block (GH_REPOSITORY) in 'Build and push multi-arch image' step.

8. tests.yaml: Moved matrix.install_target to env block (INSTALL_TARGET) in 'Create venv + install deps' step. Moved needs.test_matrix.result and needs.docker_smoke.result to env block (TEST_MATRIX_RESULT, DOCKER_SMOKE_RESULT) in 'Require matrix success' step.

9. analyzer-speed.yml: Added 'permissions: contents: read' at top level.

