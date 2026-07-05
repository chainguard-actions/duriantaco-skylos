<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos--/v4.28.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `1`

Action **duriantaco--skylos--/v4.28.0** was hardened automatically. 15 finding(s) were identified and resolved across 3 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): Direct expression interpolation in run: blocks. In action.yml, `${{ github.action_path }}` is interpolated directly in a run: shell command: `run: python -m pip install "${{ github.action_path }}"`.

Locations:

- `action.yml:52`

### script-injection (severity: high)

Sub-rule (a): Direct expression interpolation in run: blocks. `${{ github.base_ref }}` and `${{ github.event.pull_request.base.sha }}` are interpolated directly in shell commands: `git fetch origin "${{ github.base_ref }}" --depth=1` and `git worktree add /tmp/skylos-corpus-base "${{ github.event.pull_request.base.sha }}"`.

Locations:

- `.github/workflows/corpus.yml:55`

### script-injection (severity: high)

Sub-rule (a): Direct expression interpolation in run: blocks. `${{ github.base_ref }}` and `${{ github.event.pull_request.base.sha }}` are interpolated directly in shell commands: `git fetch origin "${{ github.base_ref }}" --depth=1` and `git worktree add /tmp/skylos-quality-base "${{ github.event.pull_request.base.sha }}"`.

Locations:

- `.github/workflows/quality-benchmark.yml:43`

### script-injection (severity: high)

Sub-rule (a): Direct expression interpolation in run: blocks. Multiple github context values are interpolated directly in shell commands in the 'Resolve diff base' step: `if [ "${{ github.event_name }}" = "pull_request" ]`, `echo "base=origin/${{ github.base_ref || 'main' }}" >> "$GITHUB_OUTPUT"`, `elif [ -n "${{ github.event.before }}" ]`, `echo "base=${{ github.event.before }}" >> "$GITHUB_OUTPUT"`, and `echo "base=origin/${{ github.ref_name || 'main' }}" >> "$GITHUB_OUTPUT"`.

Locations:

- `.github/workflows/skylos.yaml:48`

### script-injection (severity: high)

Sub-rule (a): Direct expression interpolation in run: blocks. `${{ matrix.install_target }}` is interpolated directly in a shell command: `uv pip install -e "${{ matrix.install_target }}"`.

Locations:

- `.github/workflows/tests.yaml:43`

### script-injection (severity: high)

Sub-rule (a): Direct expression interpolation in run: blocks. `${{ needs.test_matrix.result }}` and `${{ needs.docker_smoke.result }}` are interpolated directly in shell commands: `if [ "${{ needs.test_matrix.result }}" != "success" ] || [ "${{ needs.docker_smoke.result }}" != "success" ]`.

Locations:

- `.github/workflows/tests.yaml:76`

### script-injection (severity: high)

Sub-rule (a): Direct expression interpolation in run: blocks. `${{ github.repository }}` is interpolated directly in a docker buildx shell command: `--label "org.opencontainers.image.url=https://github.com/${{ github.repository }}"`.

Locations:

- `.github/workflows/publish.yml:253`

### script-injection (severity: high)

Sub-rule (a): Direct expression interpolation in run: blocks. `${{ github.base_ref || 'main' }}` is interpolated directly in a shell command: `run: skylos cicd review --input skylos-results.json --diff-base origin/${{ github.base_ref || 'main' }}`.

Locations:

- `.github/workflows/examples/skylos-plus-claude-security.yml:55`

### script-injection (severity: high)

Sub-rule (a): Direct expression interpolation in run: blocks. `${{ github.sha }}` is interpolated directly in a shell command: `run: skylos . --danger --quality --secrets --ai-defects --upload --force --sha "${{ github.sha }}"`.

Locations:

- `.github/workflows/examples/skylos-tokenless-ci.yml:43`

### github-env-injection (severity: high)

The 'Resolve diff base' step writes values derived from untrusted github context expressions directly to $GITHUB_OUTPUT without sanitization: `echo "base=origin/${{ github.base_ref || 'main' }}" >> "$GITHUB_OUTPUT"`, `echo "base=${{ github.event.before }}" >> "$GITHUB_OUTPUT"`, and `echo "base=origin/${{ github.ref_name || 'main' }}" >> "$GITHUB_OUTPUT"`. No `printf '%s' ... | tr -d '\n\r'` sanitization is applied before the writes.

Locations:

- `.github/workflows/skylos.yaml:49`

### permissions (severity: medium)

missing-permissions: The workflow file has no top-level `permissions:` key and no job-level `permissions:` key on any job. This grants the default (potentially write) permissions to the GITHUB_TOKEN.

Locations:

- `.github/workflows/analyzer-speed.yml:1`

### permissions (severity: medium)

missing-permissions: The workflow file has no top-level `permissions:` key and no job-level `permissions:` key on any job. This grants the default (potentially write) permissions to the GITHUB_TOKEN.

Locations:

- `.github/workflows/corpus.yml:1`

### permissions (severity: medium)

missing-permissions: The workflow file has no top-level `permissions:` key and no job-level `permissions:` key on any job. This grants the default (potentially write) permissions to the GITHUB_TOKEN.

Locations:

- `.github/workflows/quality-benchmark.yml:1`

### unpinned-uses (severity: high)

Multiple `uses:` references are pinned to mutable tags instead of full 40-character commit SHAs: `actions/checkout@v4` (lines 34, 62, 87), `actions/setup-python@v5` (lines 39, 91), `actions/upload-artifact@v4` (line 64), `anthropics/claude-code-action@main` (line 68), `actions/download-artifact@v4` (lines 96, 101).

Locations:

- `.github/workflows/examples/skylos-plus-claude-security.yml:34`

### unpinned-uses (severity: high)

Multiple `uses:` references are pinned to mutable tags instead of full 40-character commit SHAs: `actions/checkout@v4` (line 27), `actions/setup-python@v5` (line 32).

Locations:

- `.github/workflows/examples/skylos-tokenless-ci.yml:27`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection, github-env-injection, permissions, unpinned-uses

**Notes:**

Fixed all findings across 8 files:
1. action.yml: Moved ${{ github.action_path }} to env block (ACTION_PATH).
2. .github/workflows/corpus.yml: Added top-level permissions: contents: read; moved ${{ github.base_ref }} and ${{ github.event.pull_request.base.sha }} to env block (BASE_REF, BASE_SHA).
3. .github/workflows/quality-benchmark.yml: Added top-level permissions: contents: read; moved ${{ github.base_ref }} and ${{ github.event.pull_request.base.sha }} to env block (BASE_REF, BASE_SHA).
4. .github/workflows/analyzer-speed.yml: Added top-level permissions: contents: read.
5. .github/workflows/skylos.yaml: Fixed 'Resolve diff base' step - moved all github context expressions (event_name, base_ref, event.before, ref_name) to env block and added printf/tr sanitization before writing to $GITHUB_OUTPUT.
6. .github/workflows/tests.yaml: Moved ${{ matrix.install_target }} to env block (INSTALL_TARGET); moved ${{ needs.test_matrix.result }} and ${{ needs.docker_smoke.result }} to env block (TEST_MATRIX_RESULT, DOCKER_SMOKE_RESULT).
7. .github/workflows/publish.yml: Moved ${{ github.repository }} to env block (GH_REPOSITORY) in the docker buildx step.
8. .github/workflows/examples/skylos-plus-claude-security.yml: Moved ${{ github.base_ref || 'main' }} to env block (BASE_REF); pinned actions/checkout@v4, actions/setup-python@v5, actions/upload-artifact@v4, anthropics/claude-code-action@main, and actions/download-artifact@v4 to full commit SHAs.
9. .github/workflows/examples/skylos-tokenless-ci.yml: Moved ${{ github.sha }} to env block (GH_SHA); pinned actions/checkout@v4 and actions/setup-python@v5 to full commit SHAs.

### Iteration 2

**Fixes applied:** script-injection

**Notes:**

Fixed the 'Summarize in job log' step in .github/workflows/skylos.yaml: moved `${{ steps.scan.outputs.REPORT }}` out of the `run:` shell string and into an `env:` block as `REPORT: ${{ steps.scan.outputs.REPORT }}`, then referenced it as `$REPORT` in the shell script. Also added quotes around `$GITHUB_STEP_SUMMARY` for robustness.

### Iteration 3

**Fixes applied:** github-env-injection

**Notes:**

Fixed two github-env-injection findings in .github/workflows/publish.yml:
1. 'Resolve release tag input' step (line 63): Added `safe_tag="$(printf '%s' "$tag" | tr -d '\n\r')"` before writing to GITHUB_OUTPUT, replacing the unsanitized `$tag` with `$safe_tag`.
2. 'Derive image metadata' step (line 236): Added sanitization for all user-derived values written to GITHUB_OUTPUT — `version` is sanitized via `safe_version`, and `major`/`minor` are sanitized via `safe_major`/`safe_minor` using `printf '%s' ... | tr -d '\n\r'`. The `stable` output uses hardcoded string literals and requires no sanitization.

