# AI Tooling Setup

This section helps you configure Claude, Cursor, and other AI tools with the right permissions and allow lists for this repo.

<!-- copilot-skip -->
## Common checklist

- Allow the agent to **read and write** within this repo, especially `.ai/**` and `.github/**`.
- Allow running **safe local commands** such as:
  - Read-only navigation and inspection:
    - `pwd`
    - `cd <path-within-repo>`
    - `ls`, `ls -R`
    - `find . -maxdepth N ...`
    - `cat`, `head`, `tail`, `less`
    - `rg`, `grep`, `fd` (search only)
  - Read-only GitHub/API queries:
    - `gh api <path> --method GET`
  - Read-only Kubernetes inspection:
    - `kubectl config view`
    - `kubectl get <resource>...`
    - `kubectl describe <resource>...`
    - `kubectl logs <pod>...`
  - Maintenance commands (may write repo state; enable only if you are comfortable with this):
    - `python3 .ai/scripts/sync-rules.py`
    - `git status`, `git diff` within this repo
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
  - Run `python3 .ai/scripts/sync-rules.py` from the repo root (optional, this writes files).
  - Read and update files under `.ai/**` and `.github/**` (writes only if you are comfortable).
- When prompted, you can paste this as context for permissions:

  - Allow shell commands: `pwd`, `cd`, `ls`, `find`, `cat`, `head`, `tail`, `less`, `rg`, `grep`, `fd`, `gh api <path> --method GET`, `kubectl get/describe/logs/config view`, and optionally `python3 .ai/scripts/sync-rules.py`, `git status`, `git diff`.
  - Allow file access: `.ai/**`, `.github/**`, project root.
<!-- /cursor-only -->

