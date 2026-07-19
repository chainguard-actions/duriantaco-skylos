<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.23.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.23.0** was hardened automatically. 4 finding(s) were identified and resolved across 3 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): ${{ }} expressions are directly interpolated inside run: shell command strings. In action.yml the 'Install Skylos' step uses `python -m pip install "${{ github.action_path }}"`. In corpus.yml the 'Run curated corpus guard (base)' step uses `git fetch origin "${{ github.base_ref }}"` and `git worktree add ... "${{ github.event.pull_request.base.sha }}"`  directly in the shell. In quality-benchmark.yml the 'Run quality benchmark (base)' step has the same pattern. In skylos.yaml the 'Resolve diff base' step interpolates ${{ github.event_name }}, ${{ github.base_ref }}, ${{ github.event.before }}, and ${{ github.ref_name }} directly in the shell, and the 'Summarize in job log' step interpolates ${{ steps.scan.outputs.REPORT }}. In tests.yaml the 'Create venv + install deps' step uses `uv pip install -e "${{ matrix.install_target }}"` and the 'Require matrix success' step uses ${{ needs.test_matrix.result }} and ${{ needs.docker_smoke.result }} directly in shell conditionals and echo statements. In publish.yml the 'Build and push multi-arch image' step uses ${{ github.repository }} directly in --label arguments. In the example workflows, skylos-plus-claude-security.yml uses ${{ github.base_ref || 'main' }} directly in a run: command, and skylos-tokenless-ci.yml uses ${{ github.sha }} directly in a run: command.

Locations:

- `action.yml:55`
- `.github/workflows/corpus.yml:56`
- `.github/workflows/quality-benchmark.yml:47`
- `.github/workflows/skylos.yaml:57`
- `.github/workflows/skylos.yaml:100`
- `.github/workflows/tests.yaml:35`
- `.github/workflows/tests.yaml:80`
- `.github/workflows/publish.yml:220`
- `.github/workflows/examples/skylos-plus-claude-security.yml:57`
- `.github/workflows/examples/skylos-tokenless-ci.yml:40`

### github-env-injection (severity: high)

In skylos.yaml the 'Resolve diff base' step writes github context values directly to $GITHUB_OUTPUT without sanitization. Specifically: `echo "base=origin/${{ github.base_ref || 'main' }}" >> "$GITHUB_OUTPUT"`, `echo "base=${{ github.event.before }}" >> "$GITHUB_OUTPUT"`, and `echo "base=origin/${{ github.ref_name || 'main' }}" >> "$GITHUB_OUTPUT"`. An attacker who can control branch names or commit SHAs (e.g. via a pull request) could inject newlines to poison $GITHUB_OUTPUT. The required sanitization step (`printf '%s' ... | tr -d '\n\r'`) is absent before each write.

Locations:

- `.github/workflows/skylos.yaml:57`

### missing-permissions (severity: medium)

The following workflow files have no top-level `permissions:` key and no job-level `permissions:` key on any job. Without explicit permissions, the GITHUB_TOKEN is granted its default (potentially broad) permissions: analyzer-speed.yml, corpus.yml, and quality-benchmark.yml all lack any permissions declaration.

Locations:

- `.github/workflows/analyzer-speed.yml:1`
- `.github/workflows/corpus.yml:1`
- `.github/workflows/quality-benchmark.yml:1`

### unpinned-uses (severity: high)

The example workflow files reference GitHub Actions by mutable tag or branch instead of a full 40-character commit SHA, making them vulnerable to supply-chain attacks if the upstream action is compromised. skylos-plus-claude-security.yml uses: actions/checkout@v4 (×4), actions/setup-python@v5 (×2), actions/upload-artifact@v4 (×2), actions/download-artifact@v4 (×2), and anthropics/claude-code-action@main. skylos-tokenless-ci.yml uses: actions/checkout@v4 and actions/setup-python@v5.

Locations:

- `.github/workflows/examples/skylos-plus-claude-security.yml:35`
- `.github/workflows/examples/skylos-tokenless-ci.yml:27`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection, github-env-injection, missing-permissions, unpinned-uses

**Notes:**

Fixed all 4 findings across 10 files:

**script-injection** (10 locations):
- action.yml: Moved `github.action_path` to env block (ACTION_PATH)
- corpus.yml: Moved `github.base_ref` and `github.event.pull_request.base.sha` to env block (BASE_REF, BASE_SHA)
- quality-benchmark.yml: Same pattern as corpus.yml
- skylos.yaml 'Resolve diff base': Moved EVENT_NAME, BASE_REF, EVENT_BEFORE, REF_NAME to env block
- skylos.yaml 'Summarize in job log': Moved `steps.scan.outputs.REPORT` to env block (SCAN_REPORT)
- tests.yaml 'Create venv + install deps': Moved `matrix.install_target` to env block (INSTALL_TARGET)
- tests.yaml 'Require matrix success': Moved `needs.test_matrix.result` and `needs.docker_smoke.result` to env block
- publish.yml: Replaced `${{ github.repository }}` with built-in `${GITHUB_REPOSITORY}` env var
- skylos-plus-claude-security.yml: Moved `github.base_ref || 'main'` to env block (BASE_REF)
- skylos-tokenless-ci.yml: Moved `github.sha` to env block (GITHUB_SHA_VALUE)

**github-env-injection** (skylos.yaml):
- Added sanitization using `printf '%s' "$VAR" | tr -d '\n\r'` before each write to $GITHUB_OUTPUT in the 'Resolve diff base' step

**missing-permissions** (3 files):
- Added `permissions: contents: read` top-level block to analyzer-speed.yml, corpus.yml, and quality-benchmark.yml

**unpinned-uses** (example workflows):
- skylos-plus-claude-security.yml: Pinned actions/checkout@v4→34e114876b0b11c390a56381ad16ebd13914f8d5, actions/setup-python@v5→a26af69be951a213d495a4c3e4e4022e16d87065, actions/upload-artifact@v4→ea165f8d65b6e75b540449e92b4886f43607fa02, actions/download-artifact@v4→d3f86a106a0bac45b974a628896c90dbdf5c8093, anthropics/claude-code-action@main→af0559ee4f514d1ef21826982bed13f7edc3c35e
- skylos-tokenless-ci.yml: Pinned actions/checkout@v4 and actions/setup-python@v5 to same SHAs

### Iteration 1

**Fixes applied:** github-env-injection

**Notes:**

Fixed all three github-env-injection findings by adding the required `printf '%s' ... | tr -d '\n\r'` sanitization before writing untrusted values to $GITHUB_OUTPUT:
1. skylos.yaml 'Run Skylos' step: sanitized REPORT (contains github.run_number and github.sha) before writing to $GITHUB_OUTPUT.
2. publish.yml 'Resolve release tag input' step: sanitized `tag` (derived from inputs.ref) before writing to $GITHUB_OUTPUT.
3. publish.yml 'Derive image metadata' step: sanitized `version`, `major`, and `minor` (derived from needs.build.outputs.release_tag) before writing to $GITHUB_OUTPUT. The `stable` value is a hardcoded literal string so no sanitization was needed for it.

### Iteration 2

**Fixes applied:** script-injection

**Notes:**

Fixed unquoted $FLAGS variable expansion in two run: blocks in action.yml. Replaced the string-based FLAGS variable with a bash array (FLAGS=()) in both the 'Run Skylos Scan' step (~line 90) and the 'Upload to Skylos Dashboard' step (~line 120). Flags are now appended as array elements (FLAGS+=(--danger), etc.) and expanded with "${FLAGS[@]}" which is properly quoted and prevents shell metacharacter injection from the caller-controlled inputs.analysis value.

