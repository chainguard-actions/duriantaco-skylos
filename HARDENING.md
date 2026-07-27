<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.31.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.31.0** was hardened automatically. 1 finding(s) were identified and resolved across 2 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Sub-rule (a): The 'Install Skylos' step directly interpolates the GitHub Actions expression `${{ github.action_path }}` inside a `run:` shell command string: `run: python -m pip install "${{ github.action_path }}"`.

Any `${{ ... }}` expression interpolated directly into a `run:` block flows through YAML template substitution before the shell processes it, making it a script-injection risk. The value should instead be passed via an environment variable and referenced as `$ACTION_PATH` (or similar) inside the shell script.

Locations:

- `action.yml:59`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed the script injection vulnerability in the 'Install Skylos' step (action.yml line 59). Moved `${{ github.action_path }}` out of the `run:` shell command and into an `env:` block as `ACTION_PATH`. The shell command now uses `"$ACTION_PATH"` instead of `"${{ github.action_path }}"`.

### Iteration 2

**Fixes applied:** script-injection, github-env-injection, missing-permissions, unpinned-uses

**Notes:**

Fixed all 17 findings across 7 workflow files:

**script-injection fixes:**
- skylos.yaml: Moved github.event_name, github.base_ref, github.event.before, github.ref_name, and steps.scan.outputs.REPORT out of run: blocks into env: blocks
- corpus.yml: Moved github.base_ref and github.event.pull_request.base.sha into env: block
- quality-benchmark.yml: Moved github.base_ref and github.event.pull_request.base.sha into env: block
- tests.yaml: Moved matrix.install_target, needs.test_matrix.result, and needs.docker_smoke.result into env: blocks
- publish.yml: Moved github.repository into env: block (GH_REPOSITORY) for docker build labels
- examples/skylos-plus-claude-security.yml: Moved github.base_ref into env: block
- examples/skylos-tokenless-ci.yml: Moved github.sha into env: block

**github-env-injection fixes:**
- skylos.yaml 'Resolve diff base': Added printf '%s' ... | tr -d '\n\r' sanitization for all three GITHUB_OUTPUT writes
- skylos.yaml 'Run Skylos': Added sanitization for REPORT before writing to GITHUB_OUTPUT
- publish.yml 'Resolve release tag input': Added sanitization for $tag before writing to GITHUB_OUTPUT
- publish.yml 'Derive image metadata': Added sanitization for $version, $major, $minor before writing to GITHUB_OUTPUT

**missing-permissions fixes:**
- analyzer-speed.yml: Added top-level `permissions: contents: read`
- corpus.yml: Added top-level `permissions: contents: read`
- quality-benchmark.yml: Added top-level `permissions: contents: read`

**unpinned-uses fixes:**
- examples/skylos-plus-claude-security.yml: Pinned all 8 action references to full commit SHAs (actions/checkout@v4→11d596..., actions/setup-python@v5→a26af6..., actions/upload-artifact@v4→ea165f..., actions/download-artifact@v4→d3f86a..., anthropics/claude-code-action@main→be7b93...)
- examples/skylos-tokenless-ci.yml: Pinned actions/checkout@v4 and actions/setup-python@v5 to full commit SHAs

