<!-- markdownlint-disable -->

# Hardening Report: duriantaco--skylos/v5.7.0

> This file was generated automatically by the hardening agent.

**Policy SHA:** `d636be7e43ef829af6e853da6b3c7566db9f72fe`

**Test Policy SHA:** `843adf9e4b8f85d0c08b27b9d0b09dd094b54702`

**Harden Agent Version:** `2`

Action **duriantaco--skylos/v5.7.0** was hardened automatically. 3 finding(s) were identified and resolved across 1 iteration(s).

## Findings Fixed

### script-injection (severity: high)

Rule (a): the 'Install Skylos' step puts a GitHub expression straight into a run: script: `run: python -m pip install "${{ github.action_path }}[dart]"`. The value is substituted into the script text before bash parses it. Fix: pass it through env (for example `SKYLOS_ACTION_PATH: ${{ github.action_path }}`) and use `python -m pip install "${SKYLOS_ACTION_PATH}[dart]"`.

Locations:

- `action.yml:130`

### script-injection (severity: high)

Rule (b): in the 'Upload to Skylos Dashboard' step, `$FLAGS` is expanded unquoted (`python -m skylos.cli "$SKYLOS_PATH" --confidence "$SKYLOS_CONFIDENCE" $FLAGS --upload`). FLAGS includes workflow-controlled data: `FLAGS="$FLAGS --verify-model $SKYLOS_VERIFY_MODEL_INPUT"`, which comes from inputs.verify-model. A regex allowlist ([A-Za-z0-9._:/-]{1,100}) limits the risk, but this is a plain string, not an array assignment with a shellcheck directive, so the exemption does not apply. Fix: build FLAGS as a bash array, e.g. FLAGS+=(--verify-model "$SKYLOS_VERIFY_MODEL_INPUT"), and expand it as "${FLAGS[@]}".

Locations:

- `action.yml:369`
- `action.yml:363`

### github-env-injection (severity: high)

In the 'Run Skylos Scan' step, `echo "diff_base=$BASE" >> "$GITHUB_OUTPUT"` writes `BASE="origin/$GITHUB_BASE_REF"` to GITHUB_OUTPUT. GITHUB_BASE_REF is inherited from the workflow environment (github.base_ref). The step does check it against the regex ^[A-Za-z0-9._/-]+$, but the required `printf '%s' ... | tr -d '\n\r'` step does not come right before the write. The value is then read by the Quality Gate step through steps.scan.outputs.diff_base.

Locations:

- `action.yml:257`

## Iteration Notes

### Iteration 1

**Fixes applied:** script-injection, github-env-injection

**Notes:**

I fixed all three findings in action.yml. I haven't run the action to test these changes.

1. Install Skylos step: `github.action_path` now goes through `env: SKYLOS_ACTION_PATH`, and the command is `python -m pip install "${SKYLOS_ACTION_PATH}[dart]"`.
2. Upload to Skylos Dashboard step: FLAGS is now a bash array. Each flag is added with `FLAGS+=(...)`, including `--verify-model "$SKYLOS_VERIFY_MODEL_INPUT"`, and the command uses `"${FLAGS[@]}"`. The arguments the CLI receives are the same as before. The existing check on the allowed characters for verify-model is still there.
3. Run Skylos Scan step: diff_base is now passed through `printf '%s' "$BASE" | tr -d '\n\r'` just before it is written to GITHUB_OUTPUT.

The scan step builds its own FLAGS string the same unquoted way. I left it alone: it only ever holds fixed flags, never input values, and it wasn't one of the findings.

