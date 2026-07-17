<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.24.2

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.24.2** was hardened automatically. 1 finding(s) were identified and resolved across 2 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Rule (a) violation: The 'Install Skylos' step directly interpolates `${{ github.action_path }}` inside a `run:` shell command string: `run: python -m pip install "${{ github.action_path }}"`.

Per the check rules, ANY `${{ ... }}` expression directly inside a `run:` block is a script-injection finding, regardless of which context it reads from (including `github.*`). The expression is substituted by the Actions runner before the shell ever sees the command, meaning a malicious value could inject shell metacharacters. The fix is to pass the value via an `env:` variable and reference it as a quoted shell variable: set `ACTION_PATH: ${{ github.action_path }}` in an `env:` block and use `"$ACTION_PATH"` in the run script.

Locations:

- `action.yml:60`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed script injection in the 'Install Skylos' step of action.yml (line 60). Moved `${{ github.action_path }}` out of the `run:` shell string and into an `env:` block as `ACTION_PATH: ${{ github.action_path }}`. The shell command now uses `"$ACTION_PATH"` instead of `"${{ github.action_path }}"`.

### Iteration 1

**Fixes applied:** script-injection, github-env-injection, unpinned-uses, missing-permissions

**Notes:**

Fixed all four finding types across 7 workflow files:

1. script-injection: Moved all ${{ }} expressions from run: shell strings into env: blocks in corpus.yml, quality-benchmark.yml, skylos.yaml, tests.yaml, publish.yml, examples/skylos-plus-claude-security.yml, and examples/skylos-tokenless-ci.yml. Shell scripts now reference plain environment variables.

2. github-env-injection: In skylos.yaml 'Resolve diff base' step, all three GITHUB_OUTPUT writes now sanitize values with `printf '%s' ... | tr -d '\n\r'` before writing, preventing newline injection attacks from attacker-controlled branch names or event payloads.

3. unpinned-uses: Pinned all mutable action references in example files to full 40-character commit SHAs: actions/checkout@v4→34e114876b0b11c390a56381ad16ebd13914f8d5, actions/setup-python@v5→a26af69be951a213d495a4c3e4e4022e16d87065, actions/upload-artifact@v4→ea165f8d65b6e75b540449e92b4886f43607fa02, anthropics/claude-code-action@main→700e7f8316990de46bed556429765647af760efc, actions/download-artifact@v4→d3f86a106a0bac45b974a628896c90dbdf5c8093.

4. missing-permissions: Added `permissions: contents: read` top-level block to analyzer-speed.yml, corpus.yml, and quality-benchmark.yml.

