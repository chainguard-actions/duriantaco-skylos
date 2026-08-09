<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.33.2

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.33.2** was hardened automatically. 1 finding(s) were identified and resolved across 2 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): The 'Install Skylos' step directly interpolates a ${{ }} expression inside a run: shell command string. The line `run: python -m pip install "${{ github.action_path }}"` embeds `${{ github.action_path }}` directly into the shell command before the shell ever sees it. Although `github.action_path` is not attacker-controlled, any `${{ ... }}` expression directly inside a run: block is a script-injection finding per the check rules. The safe pattern is to pass the value via an env: variable and reference it as `"$ENV_VAR"` in the shell script.

Locations:

- `action.yml:88`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed the 'Install Skylos' step in action.yml (line 88): moved `${{ github.action_path }}` out of the run: shell command and into an env: block as ACTION_PATH. The shell command now references it as "$ACTION_PATH" instead of directly interpolating the expression.

### Iteration 2

**Fixes applied:** script-injection, missing-permissions, unpinned-uses

**Notes:**

Fixed all 14 findings across 7 workflow files:

**script-injection (8 findings):**
- corpus.yml: Moved github.base_ref and github.event.pull_request.base.sha to env block (BASE_REF, BASE_SHA)
- quality-benchmark.yml: Same pattern for the base benchmark step
- tests.yaml: Moved matrix.install_target (INSTALL_TARGET), matrix.python-version (PYTHON_VERSION for 2 steps), and needs results (TEST_MATRIX_RESULT, DOCKER_SMOKE_RESULT) to env blocks
- skylos.yaml: Moved steps.scan.outputs.REPORT to env block for Summarize step; also fixed unquoted $GITHUB_STEP_SUMMARY
- publish.yml: Added GH_REPOSITORY to existing env block; replaced ${{ github.repository }} inline expressions
- examples/skylos-plus-claude-security.yml: Moved github.base_ref || 'main' to env block as BASE_REF
- examples/skylos-tokenless-ci.yml: Moved github.sha to env block as GH_SHA

**missing-permissions (3 findings):**
- analyzer-speed.yml: Added top-level `permissions: contents: read`
- corpus.yml: Added top-level `permissions: contents: read`
- quality-benchmark.yml: Added top-level `permissions: contents: read`

**unpinned-uses (2 findings, 12 action references total):**
- examples/skylos-plus-claude-security.yml: Pinned actions/checkout@v4→11d5960a, actions/setup-python@v5→a26af69b, actions/upload-artifact@v4→ea165f8d, actions/download-artifact@v4→d3f86a10, anthropics/claude-code-action@main→6b082c41
- examples/skylos-tokenless-ci.yml: Pinned actions/checkout@v4→11d5960a, actions/setup-python@v5→a26af69b

