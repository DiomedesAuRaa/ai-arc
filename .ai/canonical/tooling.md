# AI Tooling Setup

This section helps you configure Claude, Cursor, and other AI tools with the right permissions and allow lists for this repo.

<!-- copilot-skip -->
## Common checklist

- Allow the agent to **read and write** within this repo, especially `.ai/**` and `.github/**`.
- Allow running **safe local commands** such as:
  - `python3 .ai/scripts/sync-rules.py`
  - `git status`, `git diff`, `git add`, `git commit` within this repo
- Prefer running commands **from the repo root** so relative paths like `.ai/...` resolve correctly.
<!-- /copilot-skip -->

<!-- claude-only -->
## Claude-specific notes

- In any workflow or project configuration, include a note that:
  - Canonical AI rules live in `.ai/canonical/`.
  - The main maintenance command is: `python3 .ai/scripts/sync-rules.py`.
- If the workflow supports **tool allow lists**, add:
  - Shell commands limited to this repo.
  - Git commands for basic status/diff/add/commit.
<!-- /claude-only -->

<!-- cursor-only -->
## Cursor-specific notes

- Ensure the agent is allowed to:
  - Run `python3 .ai/scripts/sync-rules.py` from the repo root.
  - Read and update files under `.ai/**` and `.github/**`.
- When prompted, you can paste this as context for permissions:

  - Allow shell commands: `python3 .ai/scripts/sync-rules.py`, `git status`, `git diff`, `git add`, `git commit`.
  - Allow file access: `.ai/**`, `.github/**`, project root.
<!-- /cursor-only -->

