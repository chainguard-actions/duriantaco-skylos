<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v4.28.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v4.28.0** was hardened automatically. 3 finding(s) were identified and resolved across 2 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Rule (a): The 'Install Skylos' step interpolates `${{ github.action_path }}` directly inside a `run:` shell command string: `run: python -m pip install "${{ github.action_path }}"`. Any `${{ ... }}` expression inside a `run:` block flows through YAML template substitution before the shell processes it, making it a script-injection risk.

Locations:

- `action.yml:54`

### script-injection (severity: high)

Rule (b): The variable `$FLAGS` is expanded unquoted in the `python -m skylos.cli` invocation in the 'Run Skylos Scan' step. `FLAGS` is built from `$SKYLOS_ANALYSIS`, which is sourced from `inputs.analysis` (an attacker-controllable input via `env: SKYLOS_ANALYSIS: ${{ inputs.analysis }}`). The unquoted expansion `$FLAGS` allows shell metacharacters embedded in the input to be interpreted by the shell, enabling command injection. Offending line: `          $FLAGS \`

Locations:

- `action.yml:79`

### script-injection (severity: high)

Rule (b): The variable `$FLAGS` is expanded unquoted in the `python -m skylos.cli` invocation in the 'Upload to Skylos Dashboard' step. `FLAGS` is built from `$SKYLOS_ANALYSIS`, which is sourced from `inputs.analysis` (an attacker-controllable input via `env: SKYLOS_ANALYSIS: ${{ inputs.analysis }}`). The unquoted expansion `$FLAGS` allows shell metacharacters embedded in the input to be interpreted by the shell, enabling command injection. Offending line: `          $FLAGS \`

Locations:

- `action.yml:113`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection

**Notes:**

Fixed all three script injection findings in hardened/action/action.yml:
1. 'Install Skylos' step: moved `${{ github.action_path }}` into an `env:` block as `ACTION_PATH` and referenced it as `"$ACTION_PATH"` in the run command.
2. 'Run Skylos Scan' step: replaced unquoted string `$FLAGS` expansion with a bash array (`FLAGS=()`, `FLAGS+=(--flag)`, `"${FLAGS[@]}"`), preventing shell metacharacter injection from the attacker-controllable `inputs.analysis` value.
3. 'Upload to Skylos Dashboard' step: same bash array fix applied to eliminate the unquoted `$FLAGS` expansion.

### Iteration 1

**Fixes applied:** missing-permissions, unpinned-uses, script-injection, github-env-injection

**Notes:**

Fixed all four finding types across 7 workflow files:

1. missing-permissions: Added `permissions: contents: read` to analyzer-speed.yml, corpus.yml, and quality-benchmark.yml.

2. unpinned-uses: Pinned all mutable action refs in examples/skylos-plus-claude-security.yml and examples/skylos-tokenless-ci.yml using full commit SHAs (actions/checkout@11d5960..., actions/setup-python@a26af69..., anthropics/claude-code-action@fa7e2f0..., actions/upload-artifact@ea165f8..., actions/download-artifact@d3f86a1...).

3. script-injection: Moved all ${{ }} expressions from run: blocks into env: blocks across corpus.yml, quality-benchmark.yml, skylos.yaml, tests.yaml, publish.yml, and both example files. Shell scripts now reference plain environment variables.

4. github-env-injection: In skylos.yaml's 'Resolve diff base' step, all values written to $GITHUB_OUTPUT are now sanitized with `printf '%s' ... | tr -d '\n\r'` before writing, preventing newline injection.

