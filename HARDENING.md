<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos--/v4.26.1

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `1`

Action **duriantaco--skylos--/v4.26.1** was hardened automatically. 14 finding(s) were identified and resolved across 2 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Rule (a): Direct ${{ }} expression interpolation inside run: blocks. The 'Run curated corpus guard (base)' step interpolates ${{ github.base_ref }} and ${{ github.event.pull_request.base.sha }} directly into shell commands: `git fetch origin "${{ github.base_ref }}" --depth=1` and `git worktree add /tmp/skylos-corpus-base "${{ github.event.pull_request.base.sha }}"`.

Locations:

- `.github/workflows/corpus.yml:52`

### script-injection (severity: high)

Rule (a): Direct ${{ }} expression interpolation inside run: blocks. The 'Run quality benchmark (base)' step interpolates ${{ github.base_ref }} and ${{ github.event.pull_request.base.sha }} directly into shell commands: `git fetch origin "${{ github.base_ref }}" --depth=1` and `git worktree add /tmp/skylos-quality-base "${{ github.event.pull_request.base.sha }}"`.

Locations:

- `.github/workflows/quality-benchmark.yml:44`

### script-injection (severity: high)

Rule (a): Direct ${{ }} expression interpolation inside run: blocks. The 'Resolve diff base' step interpolates multiple github.* context values directly into shell commands: `if [ "${{ github.event_name }}" = "pull_request" ]`, `echo "base=origin/${{ github.base_ref || 'main' }}" >> "$GITHUB_OUTPUT"`, `[ -n "${{ github.event.before }}" ]`, `echo "base=${{ github.event.before }}" >> "$GITHUB_OUTPUT"`, and `echo "base=origin/${{ github.ref_name || 'main' }}" >> "$GITHUB_OUTPUT"`.

Locations:

- `.github/workflows/skylos.yaml:56`

### script-injection (severity: high)

Rule (a): Direct ${{ }} expression interpolation inside run: block. The 'Summarize in job log' step interpolates ${{ steps.scan.outputs.REPORT }} (a steps.*.outputs.* context value) directly into a shell command: `echo "Skylos report: ${{ steps.scan.outputs.REPORT }}" >> $GITHUB_STEP_SUMMARY`.

Locations:

- `.github/workflows/skylos.yaml:113`

### script-injection (severity: high)

Rule (a): Direct ${{ }} expression interpolation inside run: block. The 'Create venv + install deps' step interpolates ${{ matrix.install_target }} directly into a shell command: `uv pip install -e "${{ matrix.install_target }}"`.

Locations:

- `.github/workflows/tests.yaml:43`

### script-injection (severity: high)

Rule (a): Direct ${{ }} expression interpolation inside run: block. The 'Build and push multi-arch image' step interpolates ${{ github.repository }} directly into docker build label arguments: `--label "org.opencontainers.image.url=https://github.com/${{ github.repository }}"`.

Locations:

- `.github/workflows/publish.yml:228`

### script-injection (severity: high)

Rule (a): Direct ${{ }} expression interpolation inside run: block. The 'PR Review Comments' step interpolates ${{ github.base_ref || 'main' }} directly into a shell command: `run: skylos cicd review --input skylos-results.json --diff-base origin/${{ github.base_ref || 'main' }}`.

Locations:

- `.github/workflows/examples/skylos-plus-claude-security.yml:55`

### script-injection (severity: high)

Rule (a): Direct ${{ }} expression interpolation inside run: block. The 'Scan and upload' step interpolates ${{ github.sha }} directly into a shell command: `run: skylos . --danger --quality --secrets --upload --force --sha "${{ github.sha }}"`.

Locations:

- `.github/workflows/examples/skylos-tokenless-ci.yml:41`

### github-env-injection (severity: high)

The 'Resolve diff base' step writes untrusted github.* context values directly to $GITHUB_OUTPUT without sanitization: `echo "base=origin/${{ github.base_ref || 'main' }}" >> "$GITHUB_OUTPUT"`, `echo "base=${{ github.event.before }}" >> "$GITHUB_OUTPUT"`, and `echo "base=origin/${{ github.ref_name || 'main' }}" >> "$GITHUB_OUTPUT"`. No `printf '%s' ... | tr -d '\n\r'` sanitization is applied before the writes.

Locations:

- `.github/workflows/skylos.yaml:56`

### missing-permissions (severity: medium)

The workflow has no top-level permissions: key and no job-level permissions: key on any job. This means the workflow runs with the default (potentially broad) GITHUB_TOKEN permissions.

Locations:

- `.github/workflows/analyzer-speed.yml:1`

### missing-permissions (severity: medium)

The workflow has no top-level permissions: key and no job-level permissions: key on any job. This means the workflow runs with the default (potentially broad) GITHUB_TOKEN permissions.

Locations:

- `.github/workflows/corpus.yml:1`

### missing-permissions (severity: medium)

The workflow has no top-level permissions: key and no job-level permissions: key on any job. This means the workflow runs with the default (potentially broad) GITHUB_TOKEN permissions.

Locations:

- `.github/workflows/quality-benchmark.yml:1`

### unpinned-uses (severity: high)

Multiple uses: references are pinned to mutable tags instead of full 40-character commit SHAs: `actions/checkout@v4`, `actions/setup-python@v5`, `actions/upload-artifact@v4` (multiple occurrences), `anthropics/claude-code-action@main`, `actions/download-artifact@v4` (multiple occurrences).

Locations:

- `.github/workflows/examples/skylos-plus-claude-security.yml:34`

### unpinned-uses (severity: high)

Multiple uses: references are pinned to mutable tags instead of full 40-character commit SHAs: `actions/checkout@v4`, `actions/setup-python@v5`.

Locations:

- `.github/workflows/examples/skylos-tokenless-ci.yml:27`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection, github-env-injection, missing-permissions, unpinned-uses

**Notes:**

Fixed all findings across 7 workflow files:
1. corpus.yml: Added 'permissions: contents: read' and moved github.base_ref/github.event.pull_request.base.sha to env block in 'Run curated corpus guard (base)' step.
2. quality-benchmark.yml: Added 'permissions: contents: read' and moved github.base_ref/github.event.pull_request.base.sha to env block in 'Run quality benchmark (base)' step.
3. analyzer-speed.yml: Added 'permissions: contents: read'.
4. skylos.yaml: Fixed 'Resolve diff base' step by moving all github.* context values to env block and sanitizing with printf/tr before writing to GITHUB_OUTPUT. Fixed 'Summarize in job log' step by moving steps.scan.outputs.REPORT to env block.
5. tests.yaml: Moved matrix.install_target to env block in 'Create venv + install deps' step.
6. publish.yml: Moved github.repository to env block (GH_REPOSITORY) in 'Build and push multi-arch image' step.
7. examples/skylos-plus-claude-security.yml: Pinned all actions to full SHAs (actions/checkout@v4, actions/setup-python@v5, actions/upload-artifact@v4, anthropics/claude-code-action@main, actions/download-artifact@v4) and moved github.base_ref to env block in 'PR Review Comments' step.
8. examples/skylos-tokenless-ci.yml: Pinned actions/checkout@v4 and actions/setup-python@v5 to full SHAs, and moved github.sha to env block in 'Scan and upload' step.

### Iteration 2

**Fixes applied:** script-injection

**Notes:**

Fixed two script-injection findings:
1. action.yml (line 52): Moved `${{ github.action_path }}` into an `env:` block as `ACTION_PATH` and replaced the inline interpolation with `"$ACTION_PATH"` in the run command.
2. .github/workflows/tests.yaml (line 76): Moved `${{ needs.test_matrix.result }}` and `${{ needs.docker_smoke.result }}` into an `env:` block as `TEST_MATRIX_RESULT` and `DOCKER_SMOKE_RESULT`, replacing all inline interpolations with plain environment variable references in the shell script.

