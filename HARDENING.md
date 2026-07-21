<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.30.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.30.0** was hardened automatically. 1 finding(s) were identified and resolved across 3 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): The 'Install Skylos' step directly interpolates `${{ github.action_path }}` inside a `run:` shell command string: `run: python -m pip install "${{ github.action_path }}"`.

Any `${{ ... }}` expression interpolated directly into a `run:` block is a script-injection risk because the value is substituted into the shell command string before the shell parses it. The safe pattern is to pass the value via an `env:` variable and reference it as a quoted shell variable (e.g., `env: ACTION_PATH: ${{ github.action_path }}` then `run: python -m pip install "$ACTION_PATH"`).

Locations:

- `action.yml:55`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed script injection in the 'Install Skylos' step of action.yml (line 55). Moved `${{ github.action_path }}` out of the `run:` shell string and into an `env:` block as `ACTION_PATH`, then referenced it as `"$ACTION_PATH"` in the shell command. This prevents the expression value from being substituted directly into the shell command string before parsing.

### Iteration 2

**Fixes applied:** script-injection, github-env-injection, missing-permissions, unpinned-uses

**Notes:**

Fixed all 15 findings across 7 workflow files:

1. corpus.yml: Added `permissions: contents: read`; moved github.base_ref and github.event.pull_request.base.sha into env vars BASE_REF/BASE_SHA in 'Run curated corpus guard (base)' step.

2. quality-benchmark.yml: Added `permissions: contents: read`; moved github.base_ref and github.event.pull_request.base.sha into env vars BASE_REF/BASE_SHA in 'Run quality benchmark (base)' step.

3. analyzer-speed.yml: Added `permissions: contents: read`.

4. skylos.yaml 'Resolve diff base': Moved all four github context expressions (event_name, base_ref, event.before, ref_name) into env vars; sanitized all three GITHUB_OUTPUT writes with `printf '%s' ... | tr -d '\n\r'` to fix both script-injection and github-env-injection findings.

5. skylos.yaml 'Summarize in job log': Moved steps.scan.outputs.REPORT into env var REPORT.

6. tests.yaml 'Create venv + install deps': Moved matrix.install_target into env var INSTALL_TARGET.

7. tests.yaml 'Require matrix success': Moved needs.test_matrix.result and needs.docker_smoke.result into env vars TEST_MATRIX_RESULT/DOCKER_SMOKE_RESULT.

8. publish.yml 'Build and push multi-arch image': Replaced ${{ github.repository }} with the built-in $GITHUB_REPOSITORY environment variable (already set by GitHub Actions runner).

9. examples/skylos-plus-claude-security.yml: Pinned all 5 action references to full SHAs (actions/checkout@11d5960a..., actions/setup-python@a26af69b..., anthropics/claude-code-action@b76a0776..., actions/upload-artifact@ea165f8d..., actions/download-artifact@d3f86a10...); moved github.base_ref into env var BASE_REF in 'PR Review Comments' step.

10. examples/skylos-tokenless-ci.yml: Pinned actions/checkout and actions/setup-python to full SHAs; moved github.sha into env var GIT_SHA in 'Scan and upload' step.

### Iteration 3

**Fixes applied:** github-env-injection

**Notes:**

Fixed all three github-env-injection findings:

1. publish.yml (line ~63, 'Resolve release tag input' step): Added `safe_tag=$(printf '%s' "$tag" | tr -d '\n\r')` before `echo "tag=$safe_tag" >> "$GITHUB_OUTPUT"` to sanitize the tag derived from `inputs.ref`.

2. publish.yml (line ~222, 'Derive image metadata' step): Added sanitization for `version`, `major`, and `minor` using `printf '%s' ... | tr -d '\n\r'` before each write to `$GITHUB_OUTPUT`. These values are derived from `RELEASE_TAG` which comes from `needs.build.outputs.release_tag`.

3. skylos.yaml (line ~73, 'Run Skylos' step): Added `safe_report=$(printf '%s' "$REPORT" | tr -d '\n\r')` before `echo "REPORT=$safe_report" >> "$GITHUB_OUTPUT"` to sanitize the report filename derived from `github.run_number` and `github.sha` context values.

