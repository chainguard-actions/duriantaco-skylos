<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.24.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.24.0** was hardened automatically. 14 finding(s) were identified and resolved across 2 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Rule (a): `${{ github.action_path }}` is interpolated directly inside a `run:` shell command string. Any `${{ ... }}` expression in a run block is a script-injection risk regardless of the context. Offending line: `run: python -m pip install "${{ github.action_path }}"`

Locations:

- `action.yml:57`

### script-injection (severity: high)

Rule (a): GitHub Actions expressions are interpolated directly inside `run:` shell command strings. Offending lines: `git fetch origin "${{ github.base_ref }}" --depth=1` and `git worktree add /tmp/skylos-corpus-base "${{ github.event.pull_request.base.sha }}"`

Locations:

- `.github/workflows/corpus.yml:56`
- `.github/workflows/corpus.yml:57`

### script-injection (severity: high)

Rule (a): GitHub Actions expressions are interpolated directly inside `run:` shell command strings. Offending lines: `git fetch origin "${{ github.base_ref }}" --depth=1` and `git worktree add /tmp/skylos-quality-base "${{ github.event.pull_request.base.sha }}"`

Locations:

- `.github/workflows/quality-benchmark.yml:46`
- `.github/workflows/quality-benchmark.yml:47`

### script-injection (severity: high)

Rule (a): Multiple GitHub Actions expressions are interpolated directly inside `run:` shell command strings. Offending lines include: `if [ "${{ github.event_name }}" = "pull_request" ]`, `echo "base=origin/${{ github.base_ref || 'main' }}" >> "$GITHUB_OUTPUT"`, `[ -n "${{ github.event.before }}" ]`, `echo "base=${{ github.event.before }}" >> "$GITHUB_OUTPUT"`, `echo "base=origin/${{ github.ref_name || 'main' }}" >> "$GITHUB_OUTPUT"`, and `echo "Skylos report: ${{ steps.scan.outputs.REPORT }}" >> $GITHUB_STEP_SUMMARY`

Locations:

- `.github/workflows/skylos.yaml:55`
- `.github/workflows/skylos.yaml:56`
- `.github/workflows/skylos.yaml:57`
- `.github/workflows/skylos.yaml:58`
- `.github/workflows/skylos.yaml:60`
- `.github/workflows/skylos.yaml:96`

### script-injection (severity: high)

Rule (a): GitHub Actions expressions are interpolated directly inside `run:` shell command strings. Offending lines: `uv pip install -e "${{ matrix.install_target }}"` and `if [ "${{ needs.test_matrix.result }}" != "success" ] || [ "${{ needs.docker_smoke.result }}" != "success" ]` and the echo lines referencing those same expressions.

Locations:

- `.github/workflows/tests.yaml:36`
- `.github/workflows/tests.yaml:77`
- `.github/workflows/tests.yaml:78`
- `.github/workflows/tests.yaml:79`

### script-injection (severity: high)

Rule (a): `${{ github.repository }}` is interpolated directly inside a `run:` shell command string in the docker buildx build step. Offending lines: `--label "org.opencontainers.image.url=https://github.com/${{ github.repository }}"` and `--label "org.opencontainers.image.source=https://github.com/${{ github.repository }}"`

Locations:

- `.github/workflows/publish.yml:163`
- `.github/workflows/publish.yml:164`

### script-injection (severity: high)

Rule (a): `${{ github.base_ref || 'main' }}` is interpolated directly inside a `run:` shell command string. Offending line: `run: skylos cicd review --input skylos-results.json --diff-base origin/${{ github.base_ref || 'main' }}`

Locations:

- `.github/workflows/examples/skylos-plus-claude-security.yml:52`

### script-injection (severity: high)

Rule (a): `${{ github.sha }}` is interpolated directly inside a `run:` shell command string. Offending line: `run: skylos . --danger --quality --secrets --upload --force --sha "${{ github.sha }}"`

Locations:

- `.github/workflows/examples/skylos-tokenless-ci.yml:38`

### github-env-injection (severity: high)

Untrusted GitHub context values are written directly to `$GITHUB_OUTPUT` without the required sanitization step (`printf '%s' ... | tr -d '\n\r'`). The `Resolve diff base` step writes `${{ github.base_ref || 'main' }}`, `${{ github.event.before }}`, and `${{ github.ref_name || 'main' }}` directly to `$GITHUB_OUTPUT` via `echo "base=..." >> "$GITHUB_OUTPUT"`. An attacker-controlled branch name containing newlines could inject arbitrary output variables.

Locations:

- `.github/workflows/skylos.yaml:56`
- `.github/workflows/skylos.yaml:58`
- `.github/workflows/skylos.yaml:60`

### missing-permissions (severity: medium)

The workflow file has no top-level `permissions:` key and no job-level `permissions:` key on any job. This means the workflow runs with the default (potentially broad) token permissions.

Locations:

- `.github/workflows/analyzer-speed.yml:1`

### missing-permissions (severity: medium)

The workflow file has no top-level `permissions:` key and no job-level `permissions:` key on any job. This means the workflow runs with the default (potentially broad) token permissions.

Locations:

- `.github/workflows/corpus.yml:1`

### missing-permissions (severity: medium)

The workflow file has no top-level `permissions:` key and no job-level `permissions:` key on any job. This means the workflow runs with the default (potentially broad) token permissions.

Locations:

- `.github/workflows/quality-benchmark.yml:1`

### unpinned-uses (severity: high)

Multiple `uses:` references are pinned to mutable tags or branch names instead of full 40-character commit SHAs. Failing references: `actions/checkout@v4` (×3), `actions/setup-python@v5` (×2), `actions/upload-artifact@v4` (×2), `actions/download-artifact@v4` (×2), `anthropics/claude-code-action@main` (branch ref — especially dangerous).

Locations:

- `.github/workflows/examples/skylos-plus-claude-security.yml:33`
- `.github/workflows/examples/skylos-plus-claude-security.yml:38`
- `.github/workflows/examples/skylos-plus-claude-security.yml:55`
- `.github/workflows/examples/skylos-plus-claude-security.yml:64`
- `.github/workflows/examples/skylos-plus-claude-security.yml:70`
- `.github/workflows/examples/skylos-plus-claude-security.yml:75`
- `.github/workflows/examples/skylos-plus-claude-security.yml:80`
- `.github/workflows/examples/skylos-plus-claude-security.yml:85`
- `.github/workflows/examples/skylos-plus-claude-security.yml:91`

### unpinned-uses (severity: high)

Multiple `uses:` references are pinned to mutable version tags instead of full 40-character commit SHAs. Failing references: `actions/checkout@v4` and `actions/setup-python@v5`.

Locations:

- `.github/workflows/examples/skylos-tokenless-ci.yml:25`
- `.github/workflows/examples/skylos-tokenless-ci.yml:30`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection, github-env-injection, missing-permissions, unpinned-uses

**Notes:**

Fixed all 13 findings across 8 files:

1. action.yml: Moved `${{ github.action_path }}` to env block (ACTION_PATH) in Install Skylos step.

2. corpus.yml: Added `permissions: contents: read` top-level block. Moved `${{ github.base_ref }}` and `${{ github.event.pull_request.base.sha }}` to env block (BASE_REF, BASE_SHA) in the 'Run curated corpus guard (base)' step.

3. quality-benchmark.yml: Added `permissions: contents: read` top-level block. Moved `${{ github.base_ref }}` and `${{ github.event.pull_request.base.sha }}` to env block (BASE_REF, BASE_SHA) in the 'Run quality benchmark (base)' step.

4. analyzer-speed.yml: Added `permissions: contents: read` top-level block.

5. skylos.yaml: Fixed 'Resolve diff base' step by moving all ${{ }} expressions to env block and adding `printf '%s' ... | tr -d '\n\r'` sanitization before writing to $GITHUB_OUTPUT. Fixed 'Summarize in job log' step by moving `${{ steps.scan.outputs.REPORT }}` to env block.

6. tests.yaml: Moved `${{ matrix.install_target }}` to env block (INSTALL_TARGET) in 'Create venv + install deps'. Moved `${{ needs.test_matrix.result }}` and `${{ needs.docker_smoke.result }}` to env block in 'Require matrix success'.

7. publish.yml: Moved `${{ github.repository }}` to env block (GITHUB_REPOSITORY_NAME) in 'Build and push multi-arch image' step.

8. examples/skylos-plus-claude-security.yml: Pinned all 9 action references to full commit SHAs (checkout@v4, setup-python@v5, upload-artifact@v4 ×2, download-artifact@v4 ×2, anthropics/claude-code-action@main). Moved `${{ github.base_ref || 'main' }}` to env block (BASE_REF).

9. examples/skylos-tokenless-ci.yml: Pinned actions/checkout@v4 and actions/setup-python@v5 to full commit SHAs. Moved `${{ github.sha }}` to env block (COMMIT_SHA).

### Iteration 2

**Fixes applied:** github-env-injection

**Notes:**

Fixed all three github-env-injection findings by adding printf '%s' ... | tr -d '\n\r' sanitization before writing values to $GITHUB_OUTPUT:
1. publish.yml 'Resolve release tag input' step: sanitized 'tag' variable before writing to GITHUB_OUTPUT
2. publish.yml 'Derive image metadata' step: sanitized 'version', 'major', and 'minor' variables before writing to GITHUB_OUTPUT
3. skylos.yaml 'Run Skylos' step: sanitized 'REPORT' variable before writing to GITHUB_OUTPUT

