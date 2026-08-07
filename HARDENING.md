<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.33.1

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.33.1** was hardened automatically. 14 finding(s) were identified and resolved across 3 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): ${{ }} expressions are interpolated directly inside run: shell commands. In skylos.yaml 'Resolve diff base' step: `if [ "${{ github.event_name }}" = "pull_request" ]`, `echo "base=origin/${{ github.base_ref || 'main' }}" >> "$GITHUB_OUTPUT"`, `[ -n "${{ github.event.before }}" ]`, `echo "base=${{ github.event.before }}" >> "$GITHUB_OUTPUT"`, `echo "base=origin/${{ github.ref_name || 'main' }}" >> "$GITHUB_OUTPUT"`. These github context values flow through YAML template substitution before the shell parses them, enabling command injection.

Locations:

- `.github/workflows/skylos.yaml:47`

### script-injection (severity: high)

Sub-rule (a): ${{ steps.scan.outputs.REPORT }} is interpolated directly inside a run: shell command in the 'Summarize in job log' step: `echo "Skylos report: ${{ steps.scan.outputs.REPORT }}" >> $GITHUB_STEP_SUMMARY`. A steps.*.outputs.* value is workflow-controllable and must not appear directly in a run: block.

Locations:

- `.github/workflows/skylos.yaml:127`

### script-injection (severity: high)

Sub-rule (a): ${{ matrix.install_target }} is interpolated directly inside a run: shell command in the 'Create venv + install deps' step: `uv pip install --python .venv/bin/python -e "${{ matrix.install_target }}"`; and ${{ matrix.python-version }} in the 'Build image' step: `docker build --build-arg "PYTHON_VERSION=${{ matrix.python-version }}" -t skylos:test .`; and ${{ needs.test_matrix.result }} / ${{ needs.docker_smoke.result }} in the 'Require matrix success' step run block.

Locations:

- `.github/workflows/tests.yaml:36`
- `.github/workflows/tests.yaml:65`
- `.github/workflows/tests.yaml:107`

### script-injection (severity: high)

Sub-rule (a): ${{ github.base_ref }} and ${{ github.event.pull_request.base.sha }} are interpolated directly inside a run: shell command in the 'Run curated corpus guard (base)' step: `git fetch origin "${{ github.base_ref }}" --depth=1` and `git worktree add /tmp/skylos-corpus-base "${{ github.event.pull_request.base.sha }}"`

Locations:

- `.github/workflows/corpus.yml:55`

### script-injection (severity: high)

Sub-rule (a): ${{ github.base_ref }} and ${{ github.event.pull_request.base.sha }} are interpolated directly inside a run: shell command in the 'Run quality benchmark (base)' step: `git fetch origin "${{ github.base_ref }}" --depth=1` and `git worktree add /tmp/skylos-quality-base "${{ github.event.pull_request.base.sha }}"`

Locations:

- `.github/workflows/quality-benchmark.yml:50`

### script-injection (severity: high)

Sub-rule (a): ${{ github.repository }} is interpolated directly inside a run: shell command in the 'Build and push multi-arch image' step: `--label "org.opencontainers.image.url=https://github.com/${{ github.repository }}"` and `--label "org.opencontainers.image.source=https://github.com/${{ github.repository }}"`

Locations:

- `.github/workflows/publish.yml:330`

### script-injection (severity: high)

Sub-rule (a): ${{ github.base_ref }} is interpolated directly inside a run: shell command in the 'PR Review Comments' step: `run: skylos cicd review --input skylos-results.json --diff-base origin/${{ github.base_ref || 'main' }}`

Locations:

- `.github/workflows/examples/skylos-plus-claude-security.yml:50`

### script-injection (severity: high)

Sub-rule (a): ${{ github.sha }} is interpolated directly inside a run: shell command in the 'Scan and upload' step: `run: skylos . --danger --quality --secrets --ai-defects --upload --force --sha "${{ github.sha }}"`

Locations:

- `.github/workflows/examples/skylos-tokenless-ci.yml:40`

### github-env-injection (severity: high)

The 'Resolve diff base' step writes github context values directly to $GITHUB_OUTPUT without sanitization: `echo "base=origin/${{ github.base_ref || 'main' }}" >> "$GITHUB_OUTPUT"`, `echo "base=${{ github.event.before }}" >> "$GITHUB_OUTPUT"`, and `echo "base=origin/${{ github.ref_name || 'main' }}" >> "$GITHUB_OUTPUT"`. These values are attacker-controllable (e.g. via branch names) and are written without the required `printf '%s' ... | tr -d '\n\r'` sanitization step.

Locations:

- `.github/workflows/skylos.yaml:47`

### unpinned-uses (severity: high)

Multiple uses: references use mutable tags instead of full 40-character SHA commit hashes: `actions/checkout@v4`, `actions/setup-python@v5`, `actions/upload-artifact@v4`, `anthropics/claude-code-action@main`, `actions/download-artifact@v4`. The @main ref is especially dangerous as it tracks a mutable branch head.

Locations:

- `.github/workflows/examples/skylos-plus-claude-security.yml:1`

### unpinned-uses (severity: high)

Multiple uses: references use mutable tags instead of full 40-character SHA commit hashes: `actions/checkout@v4`, `actions/setup-python@v5`.

Locations:

- `.github/workflows/examples/skylos-tokenless-ci.yml:1`

### permissions (severity: medium)

missing-permissions: The workflow has no top-level permissions: key and the single job (corpus) also has no job-level permissions: key. Without explicit permissions, the workflow inherits the repository default (which may be write-all for older repositories), granting unnecessary access.

Locations:

- `.github/workflows/corpus.yml:1`

### permissions (severity: medium)

missing-permissions: The workflow has no top-level permissions: key and the single job (analyzer-speed) also has no job-level permissions: key. Without explicit permissions, the workflow inherits the repository default.

Locations:

- `.github/workflows/analyzer-speed.yml:1`

### permissions (severity: medium)

missing-permissions: The workflow has no top-level permissions: key and the single job (quality-benchmark) also has no job-level permissions: key. Without explicit permissions, the workflow inherits the repository default.

Locations:

- `.github/workflows/quality-benchmark.yml:1`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection, github-env-injection, unpinned-uses, permissions

**Notes:**

Fixed all 14 findings across 7 workflow files:

1. skylos.yaml: Fixed 'Resolve diff base' step by moving github.event_name, github.base_ref, github.event.before, github.ref_name to env block and sanitizing values with printf/tr before writing to GITHUB_OUTPUT (fixes both script-injection and github-env-injection). Fixed 'Summarize in job log' step by moving steps.scan.outputs.REPORT to env block.

2. tests.yaml: Fixed 'Create venv + install deps' (matrix.install_target→env), 'Build image' (matrix.python-version→env), 'Check Python runtime' (matrix.python-version→env), and 'Require matrix success' (needs results→env).

3. corpus.yml: Added top-level permissions: contents: read. Fixed 'Run curated corpus guard (base)' by moving github.base_ref and github.event.pull_request.base.sha to env block.

4. quality-benchmark.yml: Added top-level permissions: contents: read. Fixed 'Run quality benchmark (base)' by moving github.base_ref and github.event.pull_request.base.sha to env block.

5. publish.yml: Fixed 'Build and push multi-arch image' by adding GITHUB_REPOSITORY_URL to env block and replacing inline ${{ github.repository }} references.

6. examples/skylos-plus-claude-security.yml: Fixed 'PR Review Comments' script injection (github.base_ref→env). Pinned all actions: actions/checkout@v4→SHA 11d5960a..., actions/setup-python@v5→SHA a26af69b..., actions/upload-artifact@v4→SHA ea165f8d..., anthropics/claude-code-action@main→SHA 1623c367..., actions/download-artifact@v4→SHA d3f86a10...

7. examples/skylos-tokenless-ci.yml: Fixed 'Scan and upload' script injection (github.sha→env as GIT_SHA). Pinned actions/checkout@v4→SHA 11d5960a... and actions/setup-python@v5→SHA a26af69b...

8. analyzer-speed.yml: Added top-level permissions: contents: read.

### Iteration 2

**Fixes applied:** script-injection

**Notes:**

Fixed all three script-injection findings in hardened/action/action.yml:
1. 'Install Skylos' step (line 97): Moved `${{ github.action_path }}` out of the run shell string into an `env:` block as `SKYLOS_ACTION_PATH`, then referenced it as `"$SKYLOS_ACTION_PATH"` in the pip install command.
2. 'Run Skylos Scan' step (line 131): Converted `FLAGS` from an unquoted string variable to a bash array (`FLAGS=()`), using `FLAGS+=(--flag)` to append elements, and expanded it safely as `"${FLAGS[@]}"` in the python invocation.
3. 'Upload to Skylos Dashboard' step (line 155): Applied the same bash array pattern as fix #2 to eliminate the unquoted `$FLAGS` expansion.

### Iteration 3

**Fixes applied:** github-env-injection

**Notes:**

Fixed all github-env-injection findings by adding `printf '%s' ... | tr -d '\n\r'` sanitization before writes to $GITHUB_OUTPUT:
1. publish.yml (line ~63): Sanitized `$tag` (derived from `inputs.ref`) before writing to GITHUB_OUTPUT.
2. publish.yml (lines ~196/200/201): Sanitized `$version`, `$major`, and `$minor` (derived from `RELEASE_TAG`/`needs.build.outputs.release_tag`) before writing to GITHUB_OUTPUT.
3. skylos.yaml (line ~80): Sanitized `$REPORT` (derived from `github.run_number` and `github.sha`) before writing to GITHUB_OUTPUT.

