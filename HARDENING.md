<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.24.1

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.24.1** was hardened automatically. 3 finding(s) were identified and resolved across 3 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Rule (a): The 'Install Skylos' step directly interpolates `${{ github.action_path }}` inside a `run:` shell command string: `run: python -m pip install "${{ github.action_path }}"`. Any `${{ ... }}` expression interpolated directly into a run block is a script-injection risk because the value is substituted into the shell command before the shell parses it.

Locations:

- `action.yml:43`

### script-injection (severity: high)

Rule (b): The variable `$FLAGS` is used unquoted in the 'Run Skylos Scan' step: `python -m skylos.cli "$SKYLOS_PATH" --confidence "$SKYLOS_CONFIDENCE" $FLAGS`. `$FLAGS` is built from `$SKYLOS_ANALYSIS`, which is sourced from `inputs.analysis` (an attacker-controllable input). Unquoted shell variable expansion allows shell metacharacters (`;`, `|`, `&`, `$(...)`, etc.) embedded in the input to be interpreted by the shell, enabling command injection.

Locations:

- `action.yml:68`

### script-injection (severity: high)

Rule (b): The variable `$FLAGS` is used unquoted in the 'Upload to Skylos Dashboard' step: `python -m skylos.cli "$SKYLOS_PATH" --confidence "$SKYLOS_CONFIDENCE" $FLAGS`. `$FLAGS` is built from `$SKYLOS_ANALYSIS`, which is sourced from `inputs.analysis` (an attacker-controllable input). Unquoted shell variable expansion allows shell metacharacters embedded in the input to be interpreted by the shell, enabling command injection.

Locations:

- `action.yml:95`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed all three script-injection findings in action.yml:
1. 'Install Skylos' step (line 43): Moved `${{ github.action_path }}` into an `env:` block as `ACTION_PATH` and referenced it as `"$ACTION_PATH"` in the run command, eliminating direct expression interpolation in the shell string.
2. 'Run Skylos Scan' step (line 68): Replaced unquoted `$FLAGS` string variable with a bash array (`FLAGS=()`), appending flags with `FLAGS+=(--flag)` and expanding safely as `"${FLAGS[@]}"`. This prevents shell metacharacters in `inputs.analysis` from being interpreted by the shell.
3. 'Upload to Skylos Dashboard' step (line 95): Applied the same bash array fix as finding 2.

### Iteration 2

**Fixes applied:** script-injection, github-env-injection, missing-permissions, unpinned-uses

**Notes:**

Fixed all 12 findings across 7 workflow files:

1. corpus.yml: Added `permissions: contents: read`; moved `github.base_ref` and `github.event.pull_request.base.sha` to env block in 'Run curated corpus guard (base)' step.

2. quality-benchmark.yml: Added `permissions: contents: read`; moved `github.base_ref` and `github.event.pull_request.base.sha` to env block in 'Run quality benchmark (base)' step.

3. analyzer-speed.yml: Added `permissions: contents: read`.

4. skylos.yaml: Fixed 'Resolve diff base' step by moving all four github context values (`github.event_name`, `github.base_ref`, `github.event.before`, `github.ref_name`) to env block and added `printf '%s' ... | tr -d '\n\r'` sanitization before each `>> $GITHUB_OUTPUT` write.

5. examples/skylos-plus-claude-security.yml: Pinned all 5 unpinned actions to full commit SHAs (actions/checkout@v4→11d5960a, actions/setup-python@v5→a26af69b, anthropics/claude-code-action@main→b76a0776, actions/upload-artifact@v4→ea165f8d, actions/download-artifact@v4→d3f86a10); moved `github.base_ref` to env block in 'PR Review Comments' step.

6. examples/skylos-tokenless-ci.yml: Pinned actions/checkout@v4→11d5960a and actions/setup-python@v5→a26af69b; moved `github.sha` to env block as `GIT_SHA` in 'Scan and upload' step.

7. publish.yml: Moved `github.repository` to env block as `GITHUB_REPOSITORY_NAME` in 'Build and push multi-arch image' step.

### Iteration 3

**Fixes applied:** script-injection, github-env-injection

**Notes:**

Fixed all four findings across two workflow files:

1. tests.yaml line 38: Moved `${{ matrix.install_target }}` to env block as INSTALL_TARGET, referenced as "$INSTALL_TARGET" in shell.

2. tests.yaml line 72: Moved `${{ needs.test_matrix.result }}` and `${{ needs.docker_smoke.result }}` to env block as TEST_MATRIX_RESULT and DOCKER_SMOKE_RESULT, referenced as plain env vars in shell.

3. skylos.yaml line 100: Moved `${{ steps.scan.outputs.REPORT }}` to env block as SCAN_REPORT, referenced as "$SCAN_REPORT" in shell. Also quoted $GITHUB_STEP_SUMMARY.

4. skylos.yaml line 76: Added sanitization before writing REPORT to $GITHUB_OUTPUT: `safe_report=$(printf '%s' "$REPORT" | tr -d '\n\r')` then `echo "REPORT=$safe_report" >> "$GITHUB_OUTPUT"`.

